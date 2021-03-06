from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
import zomatopy
import json
import requests
import ast
import re

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ActionSearchRestaurants(Action):
        def name(self):
                return 'action_search_restaurants'

                
        def run(self, dispatcher, tracker, domain):

                #creating custom function to accomodate sort,order,start,limit
                def restaurant_search_custom(query="", latitude="", longitude="", cuisines="", limit=20, start=0, sort="", order=""):
                    """
                    Takes either query, latitude and longitude or cuisine as input.
                    Returns a list of Restaurant IDs.
                    """
                    cuisines = "%2C".join(cuisines.split(","))
                    base_url="https://developers.zomato.com/api/v2.1/"
                    if str(limit).isalpha() == True:
                        raise ValueError('LimitNotInteger')
                    headers = {'Accept': 'application/json', 'user-key': "279658393d35002cb45c944d0dd06691"}
                    r = (requests.get(base_url + "search?"+ "count=" + str(limit) + "&lat=" + str(latitude) + "&lon=" + str(longitude) + "&cuisines=" + str(cuisines) + "&sort=" + str(sort) + "&order=" + str(order)+ "&start=" + str(start) , headers=headers).content).decode("utf-8")
                    #return r
                    #a = ast.literal_eval(r)
                    
                    jsonParsed  = json.loads(r)
                    return jsonParsed['restaurants']
                        
                #filtering retaurants by rating, budget
                def restraunt_search_rating_order(latitude="", longitude="", cuisines="", lowercost=0, highercost=999999):

                    restaurants = []
                    start = 0
                    sort = "rating"
                    order = "desc"
                    stopsearchcounter = 0 
                    # Allowing max 5 tries (20*5 = 100 restuarants) in order to avoid timeout error
                    while((len(restaurants) < 10) and (stopsearchcounter < 5)):
                            returnList = restaurant_search_custom("", lat, lon, str(cuisines_dict.get(cuisine)), 20,start,sort,order)
                            # iterate list to add items if fall in category
                            for returnItem in returnList:
                                    #jsonParsed  = json.loads(returnItem)
                                    if((len(restaurants) < 10) and (lowercost <= returnItem['restaurant']['average_cost_for_two']) and (returnItem['restaurant']['average_cost_for_two'] <= highercost)):
                                            restaurants.append(returnItem)
                            start = start + 20
                            stopsearchcounter = stopsearchcounter + 1               

                    return restaurants 
                
                #Init zomato object
                config={ "user_key":"279658393d35002cb45c944d0dd06691"} #New Generated id added
                zomato = zomatopy.initialize_app(config)
               
                #Get location, cuisine, budget slot
                loc = tracker.get_slot('location')
                cuisine = tracker.get_slot('cuisine')
                budget = tracker.get_slot('budget')

                # Get lat and lon values for given city to use in api
                location_detail=zomato.get_location(loc, 1)
                d1 = json.loads(location_detail)
                lat=d1["location_suggestions"][0]["latitude"]
                lon=d1["location_suggestions"][0]["longitude"]
                                     
                # This dictionary is created from CusineIdCode.ipynb file
                cuisines_dict={'Chinese':25,'Mexican':73,'Italian':55,'American':1,'South Indian':85,'North Indian':50}

                #assigning lowercost and higher cost based on budget        
                if(budget=='low'):
                        lowercost = 0
                        highercost = 300
                elif(budget == 'medium'):
                        lowercost = 300
                        highercost = 700
                elif(budget == 'high'):
                        lowercost = 700
                        highercost = 999999
                else:
                        lowercost = 0
                        highercost = 999999

                
                results = restraunt_search_rating_order(lat, lon, str(cuisines_dict.get(cuisine)),lowercost, highercost)
                response_utter=""
                response_email=""
                if (len(results) == 0):
                        response_utter= "No results found for given location and cusine selection in this budget"
                else:
                        count = 1
                        response_utter = "Showing you top rated " + cuisine+" restaurants in "+loc+" :\n\n"
                        response_email = "Showing you top rated " + cuisine+" restaurants in "+loc+" :\n\n"
                        for restaurant in results:
                                if(count <= 10):
                                        response_email=response_email+str(count)+". "+ "    Name: "+restaurant['restaurant']['name']+ "     Address: "+ restaurant['restaurant']['location']['address']+"     Rating: "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"     Budget for two: Rs"+ str(restaurant['restaurant']['average_cost_for_two'])+"\n"
                                        if(count <= 5):
                                                response_utter=response_utter+str(count)+". "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+ restaurant['restaurant']['user_rating']['aggregate_rating']+"\n"
                                        count =  count + 1
                
                dispatcher.utter_message(response_utter)
                return [SlotSet('emailcontent',response_email)]

class ActionVerifyLocation(Action):
	def name(self):
		return 'action_verify_location'

	def run(self, dispatcher, tracker, domain):
		city = tracker.get_slot('location')

		tier1_cities = ['Ahmedabad', 'Bengaluru', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune']
		tier2_cities = [ 'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 
						'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Dindigul', 'Erode', 
						'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 'Hamirpur', 'Hubli–Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 
						'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Karnal', 'Kochi', 'Kolhapur', 'Kollam', 
						'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai',
			 			'Malappuram', 'Mathura', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 
						'Patna', 'Pondicherry', 'Purulia', 'Prayagraj', 'Raipur', 'Rajkot',
		  				'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Surat', 'Thanjavur', 'Thiruvananthapuram', 'Thrissur',
		 				'Tiruchirappalli', 'Tirunelveli', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']

		tier1_cities = [name.lower() for name in tier1_cities]
		tier2_cities = [name.lower() for name in tier2_cities]

		if (city.lower() not in tier1_cities) and (city.lower() not in tier2_cities):
			dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location?")
			city = None

		return [SlotSet('location',city)]

class ActionSendDetailsToEmail(Action):
	def name(self):
		return 'action_send_details_to_email'

	def run(self, dispatcher, tracker, domain):
		# Get slot of email id of user
		email = tracker.get_slot('email')
		# check if email id is of proper format
		pattern = '([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)'
		emailformatOk = True
		if (re.search(pattern, email)):
			emailformatOk = True
		else:
			emailformatOk = False
        
		if emailformatOk == False:
			dispatcher.utter_message("Please provide correct email address in format xxxxxxx@abc.com/co.in")
			email = None
		else:
			#The mail addresses and password
			sender_address = 'anshumanshriwas.dml17@iiitb.net'
			sender_pass = 'anshu_5492'
			receiver_address = email

			#Get email content
			mail_content = tracker.get_slot('emailcontent')

			#Setup the MIME
			message = MIMEMultipart()
			message['From'] = sender_address
			message['To'] = receiver_address
			message['Subject'] = 'Restaurant Details from Foodie!!'
			#The body and the attachments for the mail
			message.attach(MIMEText(mail_content, 'plain'))
			#Create SMTP session for sending the mail
			#use gmail with port
			session = smtplib.SMTP('smtp.gmail.com', 587) 
			#enable security
			session.starttls() 
			#login with mail_id and password
			session.login(sender_address, sender_pass)
			#convert whole message as simple string
			text = message.as_string()
			session.sendmail(sender_address, receiver_address, text)
			session.quit()
			dispatcher.utter_message("Email sent to " + email)

		return [SlotSet('email',email)]

class ActionVerifyCuisine(Action):
	def name(self):
		return 'action_verify_cuisine'

	def run(self, dispatcher, tracker, domain):
		# Get Cuisine               
		cuisine = tracker.get_slot('cuisine')
		cuisine_option_list = ['chinese', 'mexican', 'italian', 'american', 'south indian', 'north indian']
		if cuisine.lower() not in cuisine_option_list:
			cuisine = None        
			dispatcher.utter_message("Please select from options 1. chinese 2.mexican 3.italian 4. american 5.south indian 6.north indian")

		return [SlotSet('cuisine',cuisine)]
		                          
class ActionResetAllSlots(Action):
	def name(self):
		return 'action_reset_allslots'

	def run(self, dispatcher, tracker, domain):
		return [AllSlotsReset()]




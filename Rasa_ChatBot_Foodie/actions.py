from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
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

		# retreive 200 restaurants for given location and cuisine
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 200)
		d = json.loads(results)
		response=""

		# create a restaurant list of all found restaurants
		restaurant_found_list = []
		if d['results_found'] == 0:
			response= "No results found for given location and cusine selection"
			dispatcher.utter_message("-----"+response+"-----")
		else:
			for restaurant in d['restaurants']:
				restaurant_found_list.append(
					{
						"Restauran_Name" : restaurant['restaurant']['name'],
						"Address" : restaurant['restaurant']['location']['address'],
						"Rating" : restaurant['restaurant']['user_rating']['aggregate_rating'],
						"Budget" : restaurant['restaurant']['average_cost_for_two']
					}
				)

			# Filter first for budget		
			restaurant_filtered_list = []
			for restaurant in restaurant_found_list:
				if ((budget == 'low') and (restaurant['Budget'] < 300)):
					restaurant_filtered_list.append(restaurant)
				elif ((budget == 'medium') and (restaurant['Budget'] >= 300) and (restaurant['Budget'] < 700)):
					restaurant_filtered_list.append(restaurant)
				elif ((budget == 'high') and (restaurant['Budget'] > 700)):
					restaurant_filtered_list.append(restaurant)

			# Get number of restaurants filtered
			number_of_restaurants_filtered = len(restaurant_filtered_list)

			# Check and create dispatch message
			if number_of_restaurants_filtered == 0:
				response= "No results found for given location and cusine selection for this budget"
				dispatcher.utter_message("-----"+response+"-----")
			else:
				count = 0
				for restaurantdetail in sorted(restaurant_filtered_list, key=lambda x: float(x['Rating']), reverse=True):
					if(count < 10):	
						response = response + restaurantdetail['Restauran_Name'] + ' in ' + restaurantdetail['Address'] + ' has been rated ' + str(restaurantdetail['Rating'])  + '\n'
						count =  count + 1
						if(count == 5):
							dispatcher.utter_message(response)

		return [SlotSet('emailcontent',response)]

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
			dispatcher.utter_message("We do not operate in that area yet")
			city = None

		return [SlotSet('location',city)]

class ActionSendDetailsToEmail(Action):
	def name(self):
		return 'action_send_details_to_email'

	def run(self, dispatcher, tracker, domain):
		# Get slot of email id of user
		email = tracker.get_slot('email')
		# check if email id is of proper format
		emailformatOk = True
		
		if emailformatOk == False:
			dispatcher.utter_message("Please provide correct email address in form xxxxxxx@abc.com")
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


		return




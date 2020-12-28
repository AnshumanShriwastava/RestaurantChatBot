## Path 1 - Sample_story_email_directly_given
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 2 - Sample_story_LocationWrong_email_directly_given
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
	- action_verify_location
	- slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- action_verify_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 3 - Sample_story_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 4 - Sample_story_LocationWrong_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Muzaffarpur"}
    - slot{"location": "Muzaffarpur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
	- action_verify_location
	- slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 5 - Sample_story_email_sent_deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_verify_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots

## Path 6 - Sample_story_LocationWrong_email_sent_deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mirzapur"}
    - slot{"location": "mirzapur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 7 - Sample_story_Cuisine_Wrong_Email_Given_Directly
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

# Path 8 - Sample_story_Cuisine_Wrong_Location_Wrong_Email_Given_Directly
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
	- action_verify_location
	- slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mughal"}
    - slot{"cuisine": "Mughal"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- action_verify_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 9 - Sample_story_Cuisine_Wrong_Email_send_confirmed
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North"}
    - slot{"cuisine": "North"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 10 - Sample_story_Cuisine_Wrong_Location_Wrong_Email_sent_Confirmed
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Muzaffarpur"}
    - slot{"location": "Muzaffarpur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
	- action_verify_location
	- slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Parsi"}
    - slot{"cuisine": "Parsi"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 11 - Sample_story_Cuisine_Wrong_Email_Deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_verify_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "punjabi"}
    - slot{"cuisine": "punjabi"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 12 - Sample_story_Cuisine_Wrong_Location_Wrong_Email_Deny
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mirzapur"}
    - slot{"location": "mirzapur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "punjabi"}
    - slot{"cuisine": "punjabi"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots

## Path 13 - Sample_story(Location)_email_directly_given
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 14 - Sample_story(Location)_LocationWrong_email_directly_given
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
	- action_verify_location
	- slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- action_verify_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 15 - Sample_story(Location)_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 16 - Sample_story(Location)_LocationWrong_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search{"location": "Muzaffarpur"}
    - slot{"location": "Muzaffarpur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
	- action_verify_location
	- slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 17 - Sample_story(Location)_email_sent_deny
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_verify_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 18 - Sample_story(Location)_LocationWrong_email_sent_deny
* greet
    - utter_greet
* restaurant_search{"location": "mirzapur"}
    - slot{"location": "mirzapur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 19 - Sample_story(Location)_Cuisine_Wrong_Email_Given_Directly
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

# Path 20 - Sample_story(Location)_Cuisine_Wrong_Location_Wrong_Email_Given_Directly
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
	- action_verify_location
	- slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mughal"}
    - slot{"cuisine": "Mughal"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- action_verify_cuisine
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 21 - Sample_story(Location)_Cuisine_Wrong_Email_send_confirmed
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North"}
    - slot{"cuisine": "North"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "North Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 22 - Sample_story(Location)_Cuisine_Wrong_Location_Wrong_Email_sent_Confirmed
* greet
    - utter_greet
* restaurant_search{"location": "Muzaffarpur"}
    - slot{"location": "Muzaffarpur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
	- action_verify_location
	- slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Parsi"}
    - slot{"cuisine": "Parsi"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 23 - Sample_story(Location)_Cuisine_Wrong_Email_Deny
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_verify_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "punjabi"}
    - slot{"cuisine": "punjabi"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
	- utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 24 - Sample_story(Location)_Cuisine_Wrong_Location_Wrong_Email_Deny
* greet
    - utter_greet
* restaurant_search{"location": "mirzapur"}
    - slot{"location": "mirzapur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "punjabi"}
    - slot{"cuisine": "punjabi"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 25 - Sample_story(Cuisine)_email_directly_given
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 26 - Sample_story(Cuisine)_LocationWrong_email_directly_given
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
	- action_verify_location
	- slot{"location": "Prayagraj"}
	- utter_ask_budget	
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 27 - Sample_story(Cuisine)_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 28 - Sample_story(Cuisine)_LocationWrong_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
    - utter_ask_location
* restaurant_search{"location": "Muzaffarpur"}
    - slot{"location": "Muzaffarpur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
	- action_verify_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 29 - Sample_story(Cuisine)_email_sent_deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_verify_location
	- slot{"location": "delhi"}
	- utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 30 - Sample_story(Cuisine)_LocationWrong_email_sent_deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
    - utter_ask_location
* restaurant_search{"location": "mirzapur"}
    - slot{"location": "mirzapur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 31 - Sample_story(Cuisine)_Cuisine_Wrong_Email_Given_Directly
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_location
* restaurant_search{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

# Path 32 - Sample_story(Cuisine)_Cuisine_Wrong_Location_Wrong_Email_Given_Directly
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
	- action_verify_location
	- slot{"location": "Prayagraj"}
	- utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 33 - Sample_story(Cuisine)_Cuisine_Wrong_Email_send_confirmed
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 34 - Sample_story(Cuisine)_Cuisine_Wrong_Location_Wrong_Email_sent_Confirmed
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_location
* restaurant_search{"location": "Muzaffarpur"}
    - slot{"location": "Muzaffarpur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
	- action_verify_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 35 - Sample_story(Cuisine)_Cuisine_Wrong_Email_Deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_verify_location
	- slot{"location": "delhi"}
	- utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots

## Path 36 - Sample_story(Cuisine)_Cuisine_Wrong_Location_Wrong_Email_Deny
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
	- utter_ask_location
* restaurant_search{"location": "mirzapur"}
    - slot{"location": "mirzapur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 37 - Sample_story(Budget)_email_directly_given
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 38 - Sample_story(Budget)_LocationWrong_email_directly_given
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
	- action_verify_location
	- slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- action_verify_cuisine
	- slot{"cuisine": "Mexican"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 39 - Sample_story(Budget)_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "North Indian"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 40 - Sample_story(Budget)_LocationWrong_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "Muzaffarpur"}
    - slot{"location": "Muzaffarpur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
	- action_verify_location
	- slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 41 - Sample_story(Budget)_email_sent_deny
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_verify_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 42 - Sample_story(Budget)_LocationWrong_email_sent_deny
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "mirzapur"}
    - slot{"location": "mirzapur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 43 - Sample_story(Budget)_Cuisine_Wrong_Email_Given_Directly
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

# Path 44 - Sample_story(Budget)_Cuisine_Wrong_Location_Wrong_Email_Given_Directly
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
	- action_verify_location
	- slot{"location": "Prayagraj"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mughal"}
    - slot{"cuisine": "Mughal"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
	- action_verify_cuisine
	- slot{"cuisine": "Mexican"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 45 - Sample_story(Budget)_Cuisine_Wrong_Email_send_confirmed
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North"}
    - slot{"cuisine": "North"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "North Indian"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 46 - Sample_story(Budget)_Cuisine_Wrong_Location_Wrong_Email_sent_Confirmed
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "Muzaffarpur"}
    - slot{"location": "Muzaffarpur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
	- action_verify_location
	- slot{"location": "Kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Parsi"}
    - slot{"cuisine": "Parsi"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 47 - Sample_story(Budget)_Cuisine_Wrong_Email_Deny
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_verify_location
	- slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "punjabi"}
    - slot{"cuisine": "punjabi"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
	- action_verify_cuisine
	- slot{"cuisine": "American"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 48 - Sample_story(Budget)_Cuisine_Wrong_Location_Wrong_Email_Deny
* greet
    - utter_greet
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - utter_ask_location
* restaurant_search{"location": "mirzapur"}
    - slot{"location": "mirzapur"}
	- action_verify_location
	- slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
	- action_verify_location
	- slot{"location": "Mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "punjabi"}
    - slot{"cuisine": "punjabi"}
	- action_verify_cuisine
	- slot{"cuisine": null}
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
	- action_verify_cuisine
	- slot{"cuisine": "South Indian"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye
	- action_reset_allslots
	
## Path 49 - Sample_story(Loc_Cus)_email_directly_given
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai"}
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
    - action_verify_location
	- action_verify_cuisine
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 50 - Sample_story(Loc_Cus)_LocationWrong_email_directly_given
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai"}
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
    - action_verify_location
	- action_verify_cuisine
	- slot{"location": null}
	- slot{"cuisine": "Mexican"}
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
	- action_verify_location
	- slot{"location": "Prayagraj"}
	- utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 51 - Sample_story(Loc_Cus)_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai"}
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
    - action_verify_location
	- action_verify_cuisine
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 52 - Sample_story(Loc_Cus)_LocationWrong_email_sent_confirmed
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai"}
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
    - action_verify_location
	- action_verify_cuisine
	- slot{"location": null}
	- slot{"cuisine": "Mexican"}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
	- action_verify_location
	- slot{"location": "Kolkata"}
	- utter_ask_budget
* restaurant_search{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 53 - happyPath1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai", "budget": "high"}
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
    - action_verify_location
	- action_verify_cuisine
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 54 - happyPath2
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai", "budget": "high"}
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
    - action_verify_location
	- action_verify_cuisine
	- slot{"location": "Mumbai"}
	- slot{"cuisine": "Mexican"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 55 - Details Budget and Cuisine 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "budget": "high"}
	- slot{"cuisine": "Chinese"}
	- slot{"budget": "high"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Delhi"}
	- slot{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 56 - Details Budget and Cuisine 2
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "budget": "high"}
	- slot{"cuisine": "Chinese"}
	- slot{"budget": "high"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
	- slot{"budget": "high"}
	- utter_ask_location
* restaurant_search{"location": "Delhi"}
	- slot{"location": "Delhi"}
	- action_verify_location
	- slot{"location": "Delhi"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 57 - Budget and Location 1
* greet
    - utter_greet
* restaurant_search{"location": "Delhi", "budget": "high"}
	- slot{"location": "Delhi"}
	- slot{"budget": "high"}
	- action_verify_location
	- slot{"location": "Delhi"}
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
    - action_search_restaurants
	- utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots
	
## Path 58 - Budget and Location 2
* greet
    - utter_greet
* restaurant_search{"location": "Delhi", "budget": "high"}
	- slot{"location": "Delhi"}
	- slot{"budget": "high"}
	- action_verify_location
	- slot{"location": "Delhi"}
	- slot{"budget": "high"}
	- utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
	- action_verify_cuisine
	- slot{"cuisine": "Chinese"}
    - action_search_restaurants
	- utter_email_request
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm OR goodbye
	- utter_goodbye
	- action_reset_allslots

## Path 59 - Interactive story 1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai"}
    - slot{"cuisine": "Thai"}
    - action_verify_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_verify_cuisine
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - action_verify_location
    - slot{"location": "Chennai"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"emailcontent": "Showing you top rated Mexican restaurants in Chennai :\n\n1.     Name: Mamagoto     Address: Shop 9, Oyster Building, Khader Nawaz Khan Road, Nungambakkam, Chennai     Rating: 4.5     Budget for two: Rs1200\n2.     Name: Coal Barbecues     Address: 40, 2nd Floor, Bazullah Road, T. Nagar, Chennai     Rating: 4.4     Budget for two: Rs1400\n3.     Name: Cafe De Paris     Address: 24, Cenotaph Road, Opposite Lanson Toyota, Teynampet, Chennai     Rating: 4.4     Budget for two: Rs900\n4.     Name: Joker's Kitchen     Address: 94/1, Door 211/1, TTK Road, Near Ethiraj Kalayana Mandapam, Alwarpet, Chennai     Rating: 4.4     Budget for two: Rs800\n5.     Name: Little Italy     Address: E-50, 17th Cross Street, Near Spencers Daily, Besant Nagar, Chennai     Rating: 4.4     Budget for two: Rs1500\n6.     Name: BurgerMan     Address: 31, 4th Main Road, Besant Nagar, Chennai     Rating: 4.4     Budget for two: Rs800\n7.     Name: Cream Centre     Address: 55, 2nd Main Road, Near Kaliappa Hospital, RA Puram, Chennai     Rating: 4.4     Budget for two: Rs1600\n8.     Name: The Bark     Address: 40, Maharaja Surya Rao Road, Dutch Village, Alwarpet, Chennai     Rating: 4.3     Budget for two: Rs1000\n9.     Name: Gastronomer By Double Roti     Address: 4/27, Cenotaph, 1st Street, Teynampet, Chennai     Rating: 4.3     Budget for two: Rs900\n10.     Name: The Cycle Gap     Address: 125, 3rd Floor, 3rd Avenue, W Block, Anna Nagar West, Chennai     Rating: 4.3     Budget for two: Rs1500\n"}
    - utter_email_request
* deny
    - utter_goodbye
	- action_reset_allslots

## Path 60 - Interactive story 2
* greet
    - utter_greet
* restaurant_search{"location": "Delhi", "budget": "low"}
    - slot{"budget": "low"}
    - slot{"location": "Delhi"}
    - action_verify_location
    - slot{"location": "Delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Gujrati"}
    - slot{"cuisine": "Gujrati"}
    - action_verify_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_verify_cuisine
    - slot{"cuisine": "Mexican"}
    - action_search_restaurants
    - slot{"emailcontent": "Showing you top rated Mexican restaurants in Delhi :\n\n1.     Name: Bistro 57     Address: Jawahar Nagar, Kamla Nagar, New Delhi     Rating: 4.4     Budget for two: Rs250\n"}
    - utter_email_request
* deny
    - utter_goodbye
	- action_reset_allslots
	
## Path 61 - Interactive story 3
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Rishikesh", "budget": "high"}
    - slot{"budget": "high"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Rishikesh"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - action_verify_cuisine
    - slot{"cuisine": "North Indian"}
    - action_search_restaurants
    - slot{"emailcontent": "Showing you top rated North Indian restaurants in Mumbai :\n\n1.     Name: Pa Pa Ya     Address: Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai     Rating: 4.9     Budget for two: Rs2000\n2.     Name: Shree Thaker Bhojanalay     Address: 31, Dadisheth Agyari Lane, Off Kalbadevi Road, Kalbadevi, Mumbai     Rating: 4.9     Budget for two: Rs1300\n3.     Name: Peshawri - ITC Maratha     Address: ITC Maratha, Sahar Road, Chakala, Mumbai     Rating: 4.9     Budget for two: Rs5000\n4.     Name: Bastian     Address: B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai     Rating: 4.8     Budget for two: Rs4200\n5.     Name: Masala Library     Address: Ground Floor, First International Financial Centre, Bandra Kurla Complex, Mumbai     Rating: 4.8     Budget for two: Rs3500\n6.     Name: JW Café - JW Marriott Mumbai Sahar     Address: IA Project Road, Chhatrapati Shivaji International Airport, Chakala, Mumbai     Rating: 4.8     Budget for two: Rs4000\n7.     Name: Burma  Burma     Address: Near Mumbai University, Kothari House, Allana Centre Lane, MG Road, Fort, Mumbai     Rating: 4.7     Budget for two: Rs1600\n8.     Name: Bayroute     Address: Minoo Manor Building, Captain Prakash Pethe Marg, Badhwar Park, Apollo Bandar, Cuffe Parade, Mumbai     Rating: 4.7     Budget for two: Rs3000\n9.     Name: Taj Mahal Tea House     Address: 36-A, Ground Floor, Sanatan Pereira Bungalow, St. John Baptist Road, Reclamation, Bandra West, Mumbai     Rating: 4.7     Budget for two: Rs900\n10.     Name: The Fusion Kitchen     Address: Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC Colony, Borivali West, Mumbai     Rating: 4.6     Budget for two: Rs1600\n"}
    - utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
    - action_send_details_to_email
    - slot{"email": "anshu5492@gmail.com"}
* affirm
    - utter_goodbye
	- action_reset_allslots
	
## Path 62 - Interactive story 4
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian", "location": "Rishikesh", "budget": "high"}
    - slot{"budget": "high"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Rishikesh"}
    - action_verify_location
	- action_verify_cuisine
    - slot{"cuisine": "North Indian"}
    - slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_verify_location
    - slot{"location": "Mumbai"}
    - action_search_restaurants
    - slot{"emailcontent": "Showing you top rated North Indian restaurants in Mumbai :\n\n1.     Name: Pa Pa Ya     Address: Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai     Rating: 4.9     Budget for two: Rs2000\n2.     Name: Shree Thaker Bhojanalay     Address: 31, Dadisheth Agyari Lane, Off Kalbadevi Road, Kalbadevi, Mumbai     Rating: 4.9     Budget for two: Rs1300\n3.     Name: Peshawri - ITC Maratha     Address: ITC Maratha, Sahar Road, Chakala, Mumbai     Rating: 4.9     Budget for two: Rs5000\n4.     Name: Bastian     Address: B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai     Rating: 4.8     Budget for two: Rs4200\n5.     Name: Masala Library     Address: Ground Floor, First International Financial Centre, Bandra Kurla Complex, Mumbai     Rating: 4.8     Budget for two: Rs3500\n6.     Name: JW Café - JW Marriott Mumbai Sahar     Address: IA Project Road, Chhatrapati Shivaji International Airport, Chakala, Mumbai     Rating: 4.8     Budget for two: Rs4000\n7.     Name: Burma  Burma     Address: Near Mumbai University, Kothari House, Allana Centre Lane, MG Road, Fort, Mumbai     Rating: 4.7     Budget for two: Rs1600\n8.     Name: Bayroute     Address: Minoo Manor Building, Captain Prakash Pethe Marg, Badhwar Park, Apollo Bandar, Cuffe Parade, Mumbai     Rating: 4.7     Budget for two: Rs3000\n9.     Name: Taj Mahal Tea House     Address: 36-A, Ground Floor, Sanatan Pereira Bungalow, St. John Baptist Road, Reclamation, Bandra West, Mumbai     Rating: 4.7     Budget for two: Rs900\n10.     Name: The Fusion Kitchen     Address: Shop 1, Opposite Veda Building, Near Bhavdevi Garage, Holy Cross Road, IC Colony, Borivali West, Mumbai     Rating: 4.6     Budget for two: Rs1600\n"}
    - utter_email_request
* deny
    - utter_goodbye
	- action_reset_allslots
	
## Path 63- Interactive story 5
* greet
    - utter_greet
* restaurant_search{"location": "warangal", "cuisine": "Chinese", "budget": "medium"}
    - slot{"budget": "medium"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "warangal"}
    - action_verify_location
    - slot{"location": "warangal"}
    - action_verify_cuisine
    - slot{"cuisine": "Chinese"}
    - action_search_restaurants
    - slot{"emailcontent": "Showing you top rated Chinese restaurants in warangal :\n\n1.     Name: Bayleaf Multi Cuisine Family Restaurant     Address: 1st Floor, Jakotia Grand Shopping Mall, MG Road, Pochamma Maidan, Behind Reliance Digital, Girmajipet, Warangal     Rating: 4.3     Budget for two: Rs400\n2.     Name: The Mirchiesz     Address: House 11-25-92, Mg Road, Pochamaidan, Girmajipet, Warangal     Rating: 4.3     Budget for two: Rs450\n3.     Name: Green Park Biryani House     Address: Near Nit, Opposite Tara Gardens, Hanumakonda, Near Hanamakonda, Warangal     Rating: 4.2     Budget for two: Rs500\n4.     Name: Green Bawarchi Restaurant     Address: Hanamakonda Main Road, Bus Stand Road, Beside State Bank Of India, Hanamkonda, Warangal     Rating: 4.1     Budget for two: Rs500\n5.     Name: Papadams Blue Restaurant     Address: 1-8-592/593, Nakkalagutta, Opposite Vidyuth Bhavan, Hanamakonda, Warangal     Rating: 4.1     Budget for two: Rs300\n6.     Name: Kadai Restaurant     Address: Door No 2-5-835, Circuit House Road, Hanamkonda, Warangal - 506001, Beside DCB Bank, Hanamakonda, Warangal     Rating: 4.0     Budget for two: Rs500\n7.     Name: Junoon Restaurant     Address: 2-10-944/1, Near Rec Petrol Pump, Hanamakonda, Warangal     Rating: 4.0     Budget for two: Rs300\n8.     Name: Bommarillu     Address: 2-5-365/1, Nakkala Gutta, Hanamkonda, Opposite to Zilla Parishad, Hanamakonda, Warangal     Rating: 3.9     Budget for two: Rs500\n9.     Name: Daawat Multi Cuisine Family Restaurant     Address: 2-10-816, Subedari, Hanamkonda, Warangal - 506001, Opp Forest Office, Hanamakonda, Warangal     Rating: 3.9     Budget for two: Rs500\n10.     Name: Sri Kalinga Restaurant     Address: #1-1-507/1, Near N.I.T, Chaitanya Puri Colony, Kazipet Main Road, Hanamakonda ,Warangal     Rating: 3.9     Budget for two: Rs400\n"}
    - utter_email_request
* deny
    - utter_goodbye
	- action_reset_allslots

## Path 64 - Interactive story 6
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "muzaffarpur"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "muzaffarpur"}
    - action_verify_location
	- action_verify_cuisine
    - slot{"location": null}
	- slot{"cuisine": "mexican"}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_verify_location
    - slot{"location": "mumbai"}
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"emailcontent": "Showing you top rated mexican restaurants in mumbai :\n\n1.     Name: Pa Pa Ya     Address: Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai     Rating: 4.9     Budget for two: Rs2000\n2.     Name: Shree Thaker Bhojanalay     Address: 31, Dadisheth Agyari Lane, Off Kalbadevi Road, Kalbadevi, Mumbai     Rating: 4.9     Budget for two: Rs1300\n3.     Name: Peshawri - ITC Maratha     Address: ITC Maratha, Sahar Road, Chakala, Mumbai     Rating: 4.9     Budget for two: Rs5000\n4.     Name: Bastian     Address: B/1, New Kamal Building, Opposite National College, Linking Road, Bandra West, Mumbai     Rating: 4.8     Budget for two: Rs4200\n5.     Name: Masala Library     Address: Ground Floor, First International Financial Centre, Bandra Kurla Complex, Mumbai     Rating: 4.8     Budget for two: Rs3500\n6.     Name: JW Café - JW Marriott Mumbai Sahar     Address: IA Project Road, Chhatrapati Shivaji International Airport, Chakala, Mumbai     Rating: 4.8     Budget for two: Rs4000\n7.     Name: Wasabi By Morimoto - The Taj Mahal Palace     Address: The Taj Mahal Palace & Tower, Apollo Bunder, Colaba, Mumbai     Rating: 4.8     Budget for two: Rs10000\n8.     Name: Burma  Burma     Address: Near Mumbai University, Kothari House, Allana Centre Lane, MG Road, Fort, Mumbai     Rating: 4.7     Budget for two: Rs1600\n9.     Name: Hakkasan     Address: 206, 2nd Floor, Krystal, Waterfield Road, Linking Road, Bandra West, Mumbai     Rating: 4.7     Budget for two: Rs2600\n10.     Name: Bombay Salad Co.     Address: Shop 1, 16th Road, Linking Road, Bandra West, Mumbai     Rating: 4.7     Budget for two: Rs900\n"}
    - utter_email_request
* email_id_send{"email": "anshu5492@gmai.com"}
    - slot{"email": "anshu5492@gmai.com"}
    - action_send_details_to_email
    - slot{"email": "anshu5492@gmai.com"}
* affirm
    - utter_goodbye
	- action_reset_allslots

## Path 65 - Interactive story 7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chappra"}
    - slot{"location": "chappra"}
    - action_verify_location
    - slot{"location": null}
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_verify_location
    - slot{"location": "kolkata"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - action_verify_cuisine
    - slot{"cuisine": null}
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_verify_cuisine
    - slot{"cuisine": "Mexican"}
	- utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_search_restaurants
    - slot{"emailcontent": "Showing you top rated Mexican restaurants in kolkata :\n\n1.     Name: The Grid     Address: 86A, Haute Street, Corporate Park, Topsia Road (South), Topsia, Kolkata     Rating: 4.7     Budget for two: Rs2000\n2.     Name: Hard Rock Cafe     Address: 57, Park Mansion, Near Reliance Digital, Park Street Area, Kolkata     Rating: 4.5     Budget for two: Rs2500\n3.     Name: Snacking     Address: 188/60/2, Lake Gardens, Kolkata     Rating: 4.5     Budget for two: Rs900\n4.     Name: Carpe Diem     Address: 18M, Park Street Area, Kolkata     Rating: 4.5     Budget for two: Rs1000\n5.     Name: Chili's Grill & Bar     Address: 1858, Acropolis Mall, Rajdanga Main Road, Kasba, Kolkata     Rating: 4.5     Budget for two: Rs1200\n6.     Name: Chili's Grill & Bar     Address: 375, 2nd Floor, South City Mall, Prince Anwar Shah Road, Kolkata     Rating: 4.5     Budget for two: Rs1200\n7.     Name: Tamara - Pipal Tree Hotel     Address: PRGM-AS/465, Hatiara, Major Arterial Road, New Town, Kolkata     Rating: 4.5     Budget for two: Rs1800\n8.     Name: Chili's Grill & Bar     Address: 33, 4th Floor, Quest Mall, Syed Ali Amir Avenue, Ballygunge, Kolkata     Rating: 4.4     Budget for two: Rs1200\n9.     Name: 10 Downing Street     Address: Plot G2, Block GP, Ground Floor, PS Srijan Corporate Park, Sector 5, Salt Lake, Kolkata     Rating: 4.4     Budget for two: Rs1600\n10.     Name: Cafe Mezzuna     Address: 375, 2nd Floor, South City Mall, Prince Anwar Shah Road, Kolkata     Rating: 4.4     Budget for two: Rs1600\n"}
    - utter_email_request
* deny
    - utter_goodbye
	- action_reset_allslots


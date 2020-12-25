## Path 1 - Sample stories1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	  - action_verify_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	  - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
	  - utter_email_request
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	  - action_send_details_to_email
* affirm
	  - utter_goodbye






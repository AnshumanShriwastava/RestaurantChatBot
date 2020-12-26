## Path 1 - Sample stories
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

## Path 2 - Sample stories
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
* affirm
	- utter_ask_email_id
* email_id_send{"email": "anshu5492@gmail.com"}
    - slot{"email": "anshu5492@gmail.com"}
	- action_send_details_to_email
* affirm
	- utter_goodbye

## Path 3 - Sample stories
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
* deny
	- utter_goodbye

## Path 4 - 1ask path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi", "cuisine": "chinese" }
    - slot{"location": "delhi"}
	 - action_verify_location
	 - slot{"cuisine": "chinese"}
	- utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye

## Path 5 - no ask path
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi", "cuisine": "chinese" ,"budget": "medium"}
    - slot{"location": "delhi"}
	 - action_verify_location
	 - slot{"cuisine": "chinese"}
    - slot{"budget": "medium"}
    - action_search_restaurants
	- utter_email_request
* deny
	- utter_goodbye





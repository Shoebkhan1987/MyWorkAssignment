import requests
import pytest
import os
from Utilities.CommonUtilities import *
import logging as logger

# Token required for authorization, better way to pass a token is using a dynamic variable from token API
auth_token = "687ccbe4e07bf7e4cd20e210a8ec9711c3039ad1db87765c48b3a419bf8d64ac"


# Following test case is used to fetch the data from gorest.co.in API and limit for number of records can be fetched is 20
def test_get_request(my_url):
    logger.info("TEst Created to fetch data from API")
    get_response_body = requests.get(my_url)
    assert get_response_body.status_code == 200

    print(get_response_body.status_code)


# Test created to create a new record
def test_post_request(my_url):

    # Go to CommonUtilities.py to see generate_random_name_and_email() function
    name_email_values = generate_random_name_and_email()
    name_value = name_email_values['name']
    email_value = name_email_values['email']

    hed = {'Authorization': 'Bearer '+auth_token}

    payload = {'name':name_value, 'gender':'Male','email':email_value,'status':'Active'}
    get_response_body = requests.post(my_url, headers = hed, data = payload)

    assert get_response_body.status_code == 200
    response = get_response_body.json()
    print(response['data']['id'])

    # created a global variable so that it can be used for fetching specific user data, updating the request and deleting the request
    global response_id 
    response_id = response['data']['id']
    

# Test Case created to fetch the user data for specific id
def test_get_request_specific_user(my_url):

    # Passed the response id global variable to fetch the data for the user created in post request
    get_response_body = requests.get(my_url + "/" + str(response_id))
    assert get_response_body.status_code == 200

    print(get_response_body.json())


# Below Test case is created to update the existing data created in the post request
def test_put_request(my_url):

    # This will create a new values for name and email
    name_email_values = generate_random_name_and_email()
    name_value = name_email_values['name']
    email_value = name_email_values['email']

    hed = {'Authorization': 'Bearer '+auth_token}

    payload = {'name':name_value, 'email':email_value,'status':'Active'}
    get_response_body = requests.put(my_url + "/" + str(response_id), headers = hed, data = payload)
    
    assert get_response_body.status_code == 200
    print(get_response_body.json())

# Test created to delete user data created in the post request
def test_delete_request(my_url):

    hed = {'Authorization': 'Bearer '+auth_token}

    delete_request = requests.delete(my_url + "/" + str(response_id), headers = hed)
    print(delete_request.json())
    response = delete_request.json()
    assert response['data'] == None

    # Below code will verify that the data is successfully removed
    get_response_body = requests.get(my_url + "/" + str(response_id))
    response_from_get_request = get_response_body.json()
    print (response_from_get_request['data']['message'])
    assert response_from_get_request['data']['message'] == "Resource not found"




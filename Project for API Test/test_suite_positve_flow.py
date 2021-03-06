import requests
import pytest
import os
from Utilities.CommonUtilities import *
import logging as logger



# Following test case is used to fetch the data from gorest.co.in API and limit for number of records can be fetched is 20
def test_get_request(my_url):
    logger.info("Test Created to fetch data from API")
    get_response_body = requests.get(my_url)
    assert get_response_body.status_code == 200


# Test created to create a new record
def test_post_request(my_url, hed):

    # Go to CommonUtilities.py to see generate_random_name_and_email() function
    name_email_values = generate_random_name_and_email()
 

    payload = {'name':name_email_values['name'], 'gender':'Male','email':name_email_values['email'],'status':'Active'}
    get_response_body = requests.post(my_url, headers = hed, data = payload)

    assert get_response_body.status_code == 200
    response = get_response_body.json()

    assert response['data']['name'] == name_email_values['name']
    assert response['data']['email'] == name_email_values['email']

    # created a global variable so that it can be used for fetching specific user data, updating the request and deleting the request
    global response_id 
    response_id = response['data']['id']
    

# Test Case created to fetch the user data for specific id
def test_get_request_specific_user(my_url):

    # Passed the response id global variable to fetch the data for the user created in post request
    get_response_body = requests.get(my_url + "/" + str(response_id))
    assert get_response_body.status_code == 200

    response = get_response_body.json()
    assert response['data']['id'] == response_id
        


# Below Test case is created to update the existing data created in the post request
def test_put_request(my_url, hed):

    # This will create a new values for name and email
    name_email_values = generate_random_name_and_email()

    payload = {'name':name_email_values['name'], 'email':name_email_values['email'],'status':'Active'}
    get_response_body = requests.put(my_url + "/" + str(response_id), headers = hed, data = payload)
    
    assert get_response_body.status_code == 200
    response = get_response_body.json()

    assert response['data']['name'] == name_email_values['name']
    assert response['data']['email'] == name_email_values['email']



# Test created to delete user data created in the post request
def test_delete_request(my_url, hed):

    delete_request = requests.delete(my_url + "/" + str(response_id), headers = hed)
    response = delete_request.json()
    assert response['data'] == None

    # Below code will verify that the data is successfully removed
    get_response_body = requests.get(my_url + "/" + str(response_id))
    response_from_get_request = get_response_body.json()

    assert response_from_get_request['data']['message'] == "Resource not found"




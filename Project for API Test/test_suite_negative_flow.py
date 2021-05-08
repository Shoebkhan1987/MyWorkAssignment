import pytest
import requests
import os
from Utilities.CommonUtilities import *

# Token is required for authorization
auth_token = "687ccbe4e07bf7e4cd20e210a8ec9711c3039ad1db87765c48b3a419bf8d64ac"
@pytest.mark.negative
def test_invalid_genderValue_post_request(my_url):

    name_email_values = generate_random_name_and_email()
    name_value = name_email_values['name']
    email_value = name_email_values['email']

    hed = {'Authorization': 'Bearer '+auth_token}

    payload = {'name':name_value, 'gender':'Test','email':email_value,'status':'Active'}
    get_response_body = requests.post(my_url, headers = hed, data = payload)

    assert get_response_body.status_code == 200
    response = get_response_body.json()
    response_data = response['data'][0]
    print(response_data['message'])
    assert response_data['message'] == 'can be Male or Female'

@pytest.mark.negative
def test_invalid_emailValue_post_request(my_url):

    name_email_values = generate_random_name_and_email()
    name_value = name_email_values['name']

    hed = {'Authorization': 'Bearer '+auth_token}

    payload = {'name':name_value, 'gender':'Male','email':'Test','status':'Active'}
    get_response_body = requests.post(my_url, headers = hed, data = payload)

    assert get_response_body.status_code == 200
    response = get_response_body.json()
    response_data = response['data'][0]
    print(response_data['message'])
    assert response_data['field'] == 'email'
    assert response_data['message'] == 'is invalid'


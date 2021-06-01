import pytest
import requests
import os
from Utilities.CommonUtilities import *


@pytest.mark.negative
def test_invalid_genderValue_post_request(my_url, hed):

    name_email_values = generate_random_name_and_email()

    payload = {'name':name_email_values['name'], 'gender':'Test','email':name_email_values['email'],'status':'Active'}
    get_response_body = requests.post(my_url, headers = hed, data = payload)

    assert get_response_body.status_code == 200
    response = get_response_body.json()
    response_data = response['data'][0]

    assert response_data['message'] == 'can be Male or Female'

@pytest.mark.negative
def test_invalid_emailValue_post_request(my_url, hed):

    name_email_values = generate_random_name_and_email()


    payload = {'name':name_email_values['name'], 'gender':'Male','email':'Test','status':'Active'}
    get_response_body = requests.post(my_url, headers = hed, data = payload)

    assert get_response_body.status_code == 200
    response = get_response_body.json()
    response_data = response['data'][0]

    assert response_data['field'] == 'email'
    assert response_data['message'] == 'is invalid'


@pytest.mark.negative
def test_invalid_statusValue_post_request(my_url, hed):

    name_email_values = generate_random_name_and_email()

    payload = {'name':name_email_values['name'], 'gender':'Male','email':name_email_values['email'],'status':'Test'}
    get_response_body = requests.post(my_url, headers = hed, data = payload)

    assert get_response_body.status_code == 200
    response = get_response_body.json()
    response_data = response['data'][0]

    assert response_data['field'] == 'status'
    assert response_data['message'] == 'can be Active or Inactive'

@pytest.mark.negative
def test_existing_emailValidation_post_request(my_url, hed):

    name_email_values = generate_random_name_and_email()

    payload = {'name':name_email_values['name'], 'gender':'Male','email':'Test1@test123.com','status':'Active'}
    get_response_body = requests.post(my_url, headers = hed, data = payload)

    assert get_response_body.status_code == 200
    response = get_response_body.json()
    response_data = response['data'][0]

    assert response_data['field'] == 'email'
    assert response_data['message'] == 'has already been taken'

@pytest.mark.negative
def test_get_request_specific_user_invalidId(my_url):

    # Passed the invalid Id to fetch the data
    get_response_body = requests.get(my_url + "/" + str(111111))
    assert get_response_body.status_code == 200
    response = get_response_body.json()
    assert response['data']['message'] == 'Resource not found'

# There is no email validation when user is updating the request, hence we can update any value
@pytest.mark.negative
def test_invalid_emailValue_put_request(my_url, hed):
    name_email_values = generate_random_name_and_email()

    payload = {'name':name_email_values['name'], 'email':name_email_values['name'],'status':'Active'}
    get_response_body = requests.put(my_url + "/" + str(123), headers = hed, data = payload)
    
    assert get_response_body.status_code == 200

@pytest.mark.negative
def test_invalid_status_put_request(my_url, hed):
    name_email_values = generate_random_name_and_email()

    payload = {'name':name_email_values['name'], 'email':name_email_values['email'],'status':'Test'}
    get_response_body = requests.put(my_url + "/" + str(246), headers = hed, data = payload)
    
    assert get_response_body.status_code == 200
    response = get_response_body.json()
    response_data = response['data'][0]

    assert response_data['field'] == 'status'
    assert response_data['message'] == 'can be Active or Inactive'

@pytest.mark.negative
def test_invalid_Id_delete_request(my_url, hed):

    delete_request = requests.delete(my_url + "/" + str(111111), headers = hed)
    response = delete_request.json()

    assert response['data']['message'] == "Resource not found"


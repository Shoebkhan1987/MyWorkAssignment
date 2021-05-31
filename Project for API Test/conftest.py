import pytest

@pytest.fixture(scope='module')
def my_url():
    url = "https://gorest.co.in/public-api/users"
    return url

@pytest.fixture(scope='module')
def hed():
    # Token required for authorization, better way to pass a token is using a dynamic variable from token API
    auth_token = "687ccbe4e07bf7e4cd20e210a8ec9711c3039ad1db87765c48b3a419bf8d64ac"
    hed_token = {'Authorization': 'Bearer '+auth_token}
    return hed_token
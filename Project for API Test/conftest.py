import pytest

@pytest.fixture(scope='module')
def my_url():
    url = "https://gorest.co.in/public-api/users"
    return url
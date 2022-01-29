# file for fixtures
import pytest
import requests
from configuration import SERVICE_URL_2


@pytest.fixture
def do_request():
    return requests.get(SERVICE_URL_2)
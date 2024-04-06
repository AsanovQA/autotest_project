import pytest
import requests
import os
from dotenv import load_dotenv
from api.api_source.apisource import ApiSource
from data.apidata import ApiData

load_dotenv()
api = ApiSource(os.getenv('BASE_URL'))


@pytest.fixture()
def api_client():
    api.api_login('/login', ApiData.login_body)
    client = requests.Session()
    client.headers.update({'Authorization': f'Bearer {os.getenv("TOKEN")}'})
    yield client
    client.close()


@pytest.fixture()
def unauth_api_client():
    client = requests.Session()
    client.headers.update({'Authorization': f'Bearer {os.getenv("FAIL_TOKEN")}'})
    yield client
    client.close()

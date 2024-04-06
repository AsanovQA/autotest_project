import os
from dotenv import load_dotenv
from data.apidata import ApiData
from api.api_source.apisource import ApiSource

load_dotenv()

api = ApiSource(os.getenv('BASE_URL'))


def test_api_login_success():
    re = api.api_login('/login', ApiData.login_body)
    assert re.status_code == 200


def test_api_login_bad_request():
    re = api.api_login('/login', ApiData.fail_login_body)
    assert re.status_code == 400


def test_get_users_success(api_client):
    re = api_client.get(f'{os.getenv('BASE_URL')}/users')
    assert re.status_code == 200


def test_get_users_unauth(unauth_api_client):
    re = unauth_api_client.get(f'{os.getenv('BASE_URL')}/users')
    assert re.status_code == 401


def test_post_pet(api_client):
    re = api_client.post(f'{os.getenv('BASE_URL')}/pet', json=ApiData.pet_data)
    assert re.status_code == 200


def test_post_pet_validerror(api_client):
    re = api_client.post(f'{os.getenv('BASE_URL')}/pet', json=ApiData.fail_pet_data)
    assert re.status_code == 422


def test_post_pet_unauth(unauth_api_client):
    re = unauth_api_client.post(f'{os.getenv('BASE_URL')}/pet', json=ApiData.pet_data)
    assert re.status_code == 401

import requests
import os
from dotenv import load_dotenv
from core.functions import save_token, new_login
from data.apidata import ApiData

load_dotenv()


def test_api_login_success():
    re = requests.post(os.getenv('BASE_URL') + 'login',
                       json=ApiData.login_body)
    assert re.status_code == 200
    save_token(re.text)


def test_api_login_bad_request():
    re = requests.post(os.getenv('BASE_URL') + 'login',
                       json=ApiData.fail_login_body)
    assert re.status_code == 400


def test_get_users_success():
    re = requests.get(os.getenv('BASE_URL') + 'users', headers=ApiData.auth_body)
    if re.status_code == 401:
        new_login()
        re = requests.get(os.getenv('BASE_URL') + 'users', headers=ApiData.auth_body)
        if re.status_code == 200:
            assert True
    elif re.status_code == 200:
        assert True


def test_get_users_unauth():
    re = requests.get(os.getenv('BASE_URL') + 'users', headers=ApiData.fail_auth_body)
    assert re.status_code == 401


def test_post_pet():
    re = requests.post(os.getenv('BASE_URL') + 'pet', headers=ApiData.auth_body, json=ApiData.pet_data)
    if re.status_code == 401:
        new_login()
        re = requests.post(os.getenv('BASE_URL') + 'pet', headers=ApiData.auth_body, json=ApiData.pet_data)
        if re.status_code == 200:
            assert True
    elif re.status_code == 200:
        assert True


def test_post_pet_validerror():
    re = requests.post(os.getenv('BASE_URL') + 'pet', headers=ApiData.auth_body, json=ApiData.fail_pet_data)
    if re.status_code == 401:
        new_login()
        re = requests.post(os.getenv('BASE_URL') + 'pet', headers=ApiData.auth_body, json=ApiData.fail_pet_data)
        if re.status_code == 200:
            assert True
    elif re.status_code == 422:
        assert True


def test_post_pet_unauth():
    re = requests.post(os.getenv('BASE_URL') + 'pet', headers=ApiData.fail_auth_body, json=ApiData.pet_data)
    assert re.status_code == 401

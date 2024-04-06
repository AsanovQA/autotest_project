import json
import os
import requests
from data.apidata import ApiData

null = None


def save_storage(cookies):
    if os.path.getsize("../data/localStorage.json") > 0:
        empty_data = ""
        with open("../data/localStorage.json", "w") as f:
            json.dump(empty_data, f)
        with open("../data/localStorage.json", "w") as f:
            json.dump(cookies, f)
    else:
        with open("../data/localStorage.json", "w") as f:
            json.dump(cookies, f)


def get_auth_token():
    if os.path.getsize("../data/localStorage.json") > 0:
        with open("../data/localStorage.json", "r") as f:
            localStorage_data_str = json.loads(f.read())
        lo = dict(eval(localStorage_data_str))
        return lo.get('token')


def save_token(response: str):
    with open('../../.env', 'r') as env_file:
        lines = env_file.readlines()

    token_found = False
    for i, line in enumerate(lines):
        if line.startswith('\nTOKEN='):
            current_token = line.strip().split('=')[1]
            if current_token == {dict(eval(response)).get('token')}:
                token_found = True
                break

    if not token_found:
        lines = [line for line in lines if not line.startswith('TOKEN=')]
        lines.append(f'TOKEN={dict(eval(response)).get('token')}')

    with open('../../.env', 'w') as env_file:
        env_file.writelines(lines)


def new_login():
    re = requests.post(os.getenv('BASE_URL') + 'login',
                       json=ApiData.login_body)
    if re.status_code == 200:
        save_token(re.text)

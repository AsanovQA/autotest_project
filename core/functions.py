import json
import os

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


print(get_auth_token())

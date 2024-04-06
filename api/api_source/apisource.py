import requests
from dotenv import load_dotenv
from core.functions import save_token
import json

load_dotenv()


class ApiSource:
    def __init__(self, base_url):
        self.base_url = base_url

    def api_login(self, url, body):
        re = requests.post(self.base_url + url,
                           json=body)
        if re.status_code == 200:
            save_token(re.text)
        return re

    def get_users(self, url, headers):
        re = requests.get(self.base_url + url, headers=headers)
        return re

    def post_pet(self, url, headers, body):
        re = requests.post(self.base_url + url, headers=headers, json=body)
        return re

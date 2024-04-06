import os
from dotenv import load_dotenv

load_dotenv()


class ApiData:
    login_body = {"email": os.getenv('USERNAME'), "password": os.getenv('PASSWORD')}
    fail_login_body = {"email": os.getenv('FAIL_USERNAME'), "password": os.getenv('FAIL_PASSWORD')}

    pet_data = {
          "id": 0,
          "name": "string",
          "type": "string",
          "age": 0,
          "gender": "string",
          "owner_id": 0,
          "pic": "string",
          "owner_name": "string",
          "likes_count": 0,
          "liked_by_user": True}

    fail_pet_data = {
        'gav': 'no'}


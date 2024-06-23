# cat_api.py
import requests
from config import CAT_API_KEY, CAT_API_BASE_URL

headers = {
    'x-api-key': CAT_API_KEY
}

def get_random_cat_image():
    url = f'{CAT_API_BASE_URL}/images/search'
    response = requests.get(url, headers=headers)
    return response.json()[0] if response.status_code == 200 else None
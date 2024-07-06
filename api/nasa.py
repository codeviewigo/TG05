import requests
import random
from datetime import datetime, timedelta

from config import NASA_API_KEY


def get_random_apod():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    random_date = start_date + (end_date - start_date) * random.random()
    date_str = random_date.strftime('%Y-%m-%d')

    response = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={NASA_API_KEY}&date={date_str}')
    data = response.json()

    return data

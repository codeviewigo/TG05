import requests

from config import WT_API


def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': WT_API,
        'units': 'metric',
        'lang': 'ru'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        if data["cod"] == 200:
            main = data["main"]
            weather = data["weather"][0]
            wind = data["wind"]

            weather_info = {
                "city": data["name"],
                "temperature": main["temp"],
                "feels_like": main["feels_like"],
                "weather": weather["description"],
                "humidity": main["humidity"],
                "pressure": main["pressure"],
                "wind_speed": wind["speed"],
                "wind_deg": wind["deg"]
            }
            return weather_info
        else:
            return {"Ошибка": data["message"]}
    except requests.exceptions.HTTPError as http_err:
        return {"Ошибка": f"HTTP ошибка: {http_err}"}
    except Exception as err:
        return {"Ошибка": f"Другая ошибка: {err}"}

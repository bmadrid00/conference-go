import requests
from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY


def getCityPhoto(city, state):
    response = requests.get(
        url=f"https://api.pexels.com/v1/search?query={city},{state} skyline",
        headers={"Authorization": f"{PEXELS_API_KEY}"},
    )
    try:
        photo_url = response.json()["photos"][1]["src"]["original"]
    except (ValueError, IndexError):
        return None
    return photo_url


def get_weather_data(city, state):
    geocoding_params = {
        "q": f"{city},{state},US",
        "limit": 1,
        "appid": OPEN_WEATHER_API_KEY,
    }
    geocoding_url = "http://api.openweathermap.org/geo/1.0/direct"
    response = requests.get(geocoding_url, params=geocoding_params)
    content = response.json()
    try:
        latitude = content[0]["lat"]
        longitude = content[0]["lon"]
    except (KeyError, IndexError):
        return None

    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    weather_response = requests.get(weather_url, params=weather_params)
    try:
        description = weather_response.json()["weather"][0]["description"]
        temperature = weather_response.json()["main"]["temp"]
    except (KeyError, IndexError):
        return None

    return {"description": description, "temp": temperature}

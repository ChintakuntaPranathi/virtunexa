
import requests
API_KEY = "4ee37567f49828101db33139d4cbb793"  # Replace with your OpenWeatherMap API key

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url).json()
        if response.get("cod") != 200:
            return "City not found."
        temp = response["main"]["temp"]
        desc = response["weather"][0]["description"]
        return f"{city.title()}: {temp}°C, {desc}"
    except Exception as e:
        return f"Error: {e}"

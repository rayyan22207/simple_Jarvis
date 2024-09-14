import requests

# WeatherAPI API key and endpoint
API_KEY = "YOUR_WEATHERAPI_API_KEY"  # Replace with your actual API key
WEATHER_URL = "http://api.weatherapi.com/v1/current.json"

# Function to get weather from WeatherAPI
def get_weather():
    # Define the location (city name) you want to get the weather for
    city = "Karachi"  # Replace with your city
    params = {
        'key': API_KEY,
        'q': city
    }
    response = requests.get(WEATHER_URL, params=params)
    data = response.json()
    if response.status_code == 200 and 'current' in data:
        # Extract weather description and temperature
        weather_description = data['current']['condition']['text']
        temperature = data['current']['temp_c']  # Celsius temperature
        return f"Current weather in {city}: {weather_description}, temperature is {temperature}°Celsius."
    else:
        return "I could not retrieve the weather information."

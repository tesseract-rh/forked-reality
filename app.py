from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# OpenWeatherMap API key - will be stored in a .env file
API_KEY = os.getenv("WEATHER_API_KEY")

def fetch_weather(location):
    """
    Fetch weather data for a given location using OpenWeatherMap API
    Location format: "City, Country" (e.g., "New York City, USA")
    """
    try:
        # Parse the location
        parts = location.split(',')
        if len(parts) != 2:
            return None, "Invalid location format. Please use: City, Country"

        city = parts[0].strip()
        country = parts[1].strip()

        # Make API request to OpenWeatherMap
        url = f"https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': f"{city},{country}",
            'appid': API_KEY,
            'units': 'metric'  # Get temperature in Celsius
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            if response.status_code == 401:
                return None, "Invalid API key. Please check your OpenWeatherMap API key."
            elif response.status_code == 404:
                return None, f"Location not found: {location}"
            else:
                return None, f"Error fetching weather data: {response.json().get('message', 'Unknown error')}"

        # Parse the weather data
        data = response.json()
        temp_c = data['main']['temp']
        temp_f = (temp_c * 9/5) + 32  # Convert to Fahrenheit

        weather_data = {
            'temp': round(temp_c, 1),
            'temp_f': round(temp_f, 1),
            'condition': data['weather'][0]['description']
        }

        # Generate warning message based on temperature
        if temp_f < 32 or temp_c > 30:
            warning_message = "DO NOT GO OUT! Temperature is extreme!"
        else:
            warning_message = "Enjoy your day out!"

        return weather_data, warning_message

    except Exception as e:
        return None, f"An error occurred: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    warning_message = None
    location = None
    weather_data = None
    error = None

    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            weather_data, result = fetch_weather(location)
            if weather_data:
                warning_message = result
            else:
                error = result
                warning_message = error

    return render_template('index.html',
                          warning_message=warning_message,
                          location=location,
                          weather_data=weather_data,
                          error=error)

if __name__ == '__main__':
    app.run(debug=True)
# Weather Warning Application

A simple web application that checks the current weather for a given location and provides a warning if the temperature is extreme (below 32°F or above 30°C).

## Features

- Input a location in the format: city, country (e.g., "New York City, USA")
- Fetches real-time weather data using the OpenWeatherMap API
- Displays current temperature in both Celsius and Fahrenheit
- Shows a warning message based on temperature thresholds:
  - "DO NOT GO OUT" if temperature is below 32°F or above 30°C
  - "Enjoy your day out!" if the temperature is within a safe range

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- An OpenWeatherMap API key (get one for free at [OpenWeatherMap](https://openweathermap.org/api))

### Installation

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory:
   ```
   cp .env.example .env
   ```

4. Edit the `.env` file and add your OpenWeatherMap API key:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```

### Running the Application

1. Start the Flask server:
   ```
   python app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Enter a location in the format "City, Country" and click "Check Weather".

## Usage Examples

- "London, UK"
- "Tokyo, Japan"
- "New York City, USA"
- "Sydney, Australia"
- "Moscow, Russia"

## Technical Details

- Built with Flask (Python web framework)
- Uses the OpenWeatherMap API for weather data
- Temperatures are fetched in Celsius and converted to Fahrenheit for display

## Error Handling

The application handles various errors including:
- Invalid location format
- Location not found
- API key issues
- Network problems

## License

MIT

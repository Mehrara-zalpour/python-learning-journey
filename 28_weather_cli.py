"""
Project 28

Weather CLI

A command-line weather application built with Python.

Features:

* Get current weather information by city name
* Display temperature
* Display feels-like temperature
* Display humidity
* Display weather description
* Display wind speed
* Handle invalid or unsuccessful API responses
* Store API key securely using environment variables

Concepts practiced:

* Functions
* User input and validation
* Dictionaries
* Nested dictionaries
* Lists
* Working with JSON data
* HTTP requests
* REST APIs
* API parameters
* API keys
* requests library
* python-dotenv
* Environment variables
* os.getenv()
* HTTP status codes
* Exception and error handling
* f-strings

Libraries:

* requests
* python-dotenv

Project goal:

Practice working with external APIs and learn how to retrieve,
process, and display real-world data in a Python CLI application.
"""

import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Unable to get weather information.")
        return

    data = response.json()

    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print("\n===== WEATHER INFORMATION =====")
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Weather: {description}")
    print(f"Wind speed: {wind_speed} m/s")


def main():
    print("===== WEATHER CLI =====")

    city = input("Enter city name: ").strip()

    if not city:
        print("City name cannot be empty.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()

    

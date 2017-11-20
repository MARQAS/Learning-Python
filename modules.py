# Import the requests module
import requests
# OpenWeatherMap.org provides an API for looking up weather forecasts. So use the URL of it  
url = "http://api.openweathermap.org/data/2.5/weather?q=Orlando,fl&units=imperial&appid=2de143494c0b295cca9337e1e96b00e0"
request = requests.get(url)
# Get the data in JSON format
weather_json = request.json()
print(weather_json)
# Assign the 'main' value of Json data
weather_main = weather_json['main']
# Use the 'temp' value from weather main
temp = weather_main['temp']
# Print the Current Temp
print("The Circus's current temperature is ", temp)
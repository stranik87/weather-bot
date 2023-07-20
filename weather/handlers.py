from telegram import Update
from telegram.ext import CallbackContext
import os
import requests
import datetime
from pprint import pprint


API_KEY = os.environ.get('API_KEY')
URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"

timestamp = datetime.datetime.now()
timezone_offset_seconds = 18000
current_time = datetime.datetime.now()
format_time = current_time.strftime('%D-%H:%M')
print(format_time)



def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f"Hello {update.effective_user.first_name}!\n\nsend me a location and I'll tell you the weather forecast.")

def weather(update: Update, context: CallbackContext) -> None:
    lat = update.message.location.latitude
    lon = update.message.location.longitude
    url = URL.format(lat=lat, lon=lon, API_KEY=API_KEY)
    response = requests.get(url)
    data = response.json()
    pprint(data)
    weather = data['weather'][0]['main']
    print(weather)
    temp = data['main']['temp']-273.15
    
    update.message.reply_text(f"The weather is {weather} and the temperature is {round(temp, 1)}°C at {data['name']} {data['sys']['country']} local time {format_time} ")
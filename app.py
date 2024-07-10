from flask import Flask, render_template, request
from datetime import datetime
import json
import requests
import urllib.request

app = Flask(__name__)
key= "d177b11b2383bfdbfa06065069615e41"

@app.route("/")
def index():
    return render_template("index.html")
 
@app.route("/city/", methods=['GET', 'POST'])
def add_city():
    if request.method == 'POST':
        enter_city = request.form["enter_city"]
        
    url = f"https://api.openweathermap.org/data/2.5/weather?q={enter_city}&appid={key}"
    response = requests.form.get(url)
    data = response.json()
    
    if response.status_code==200:
        name = data["name"]
        temp = data["main"]["temp"]
        lat = data["coord"]["lat"]
        lon = data["coord"]["lon"]
        country = data["sys"]["country"]
        visibility = data["visibility"]
        weather = data["weather"][0]["main"]

        print("*"*10, "Weather Data", "*"*10)
        print("-"*35)
        print(f"City       ----> {name:^20}")
        print(f"Temprature ----> {temp:>11}℃")
        print(f"Latitude   ----> {lat:^20}")
        print(f"Longitude  ----> {lon:^20}")
        print(f"Country    ----> {country:^20}")
        print(f"Visibility ----> {visibility:^20}")
        print(f"Weather    ----> {weather:^20}")

        print("-"*35)
    
    if response.status_code==404:
        msg = "city not found"
        print(msg)

if __name__ == "__main__":
    app.run(debug=True, passthrough_errors=True, use_debugger=False, use_reloader=False)









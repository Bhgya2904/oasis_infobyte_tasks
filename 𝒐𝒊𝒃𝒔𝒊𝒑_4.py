import requests
import json
import os
key = "4175b183fff40967fe22a58fb2332fc7"
baseUrl = "http://api.openweathermap.org/data/2.5/weather?"
loc = input("Enter city/state name : ")
url = baseUrl + "appid=" + key + "&q=" + loc
response = requests.get(url)
res = response.json()
if (res["cod"] == "404"):
	print(" Location Not Found ")
else:
	tempK = res["main"]["temp"]
	feelK = res["main"]["feels_like"]
	pres = res["main"]["pressure"]
	humi = res["main"]["humidity"]
	desc = res["weather"][0]["description"]
	tempC = tempK - 273.15
	feelC = feelK - 273.15
	pres *= 0.0009869233
	print(" Temperature = " + str(round(tempC, 2)) + " °C")
	print(" Feels Like = " + str(round(feelC, 2)) + " °C")
	print(" Pressure = " + str(round(pres, 2)) + " atm")
	print(" Humidity = " + str(humi) + " %")
	print(" Description = " + str(desc))



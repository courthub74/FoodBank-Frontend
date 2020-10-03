from django.shortcuts import render

#HOME
def home(request):
	return render(request, "home.html", {})


#MICHIGAN
def mich(request):
	return render(request, "mich.html", {})

#Farmington
def farm(request):
	# scrape the Farmington stuff here and then call it through the dictionary
	import requests
	import json

	farm = requests.get("https://foodbankapi.herokuapp.com/foodbank/3/?format=json")
	farmington = json.loads(farm.content)

	return render(request, "farm.html", {'farmington': farmington})


from django.shortcuts import render

#HOME
def home(request):
	return render(request, "home.html", {})


#MICHIGAN - List of Cities
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


#Farmington Hills
def farmhills(request):
	import requests
	import json

	fhillsREQ = requests.get("https://foodbankapi.herokuapp.com/foodbank/1/?format=json")
	farmhills1 = json.loads(fhillsREQ.content)

	fhills2REQ = requests.get("https://foodbankapi.herokuapp.com/foodbank/2/?format=json")
	farmhills2 = json.loads(fhills2REQ.content)

	return render(request, "farmhills.html", {'farmhills1': farmhills1, 'farmhills2': farmhills2})



#Livonia
def livonia(request):
	import requests
	import json

	livonia = requests.get("https://foodbankapi.herokuapp.com/foodbank/5/?format=json")
	liv = json.loads(livonia.content)

	return render(request, "livonia.html", {'liv': liv})


#Southfield
def southfield(request):
	import requests
	import json

	southfield = requests.get("https://foodbankapi.herokuapp.com/foodbank/6/?format=json")
	south = json.loads(southfield.content)

	return render(request, "southfield.html", {'south': south})


#ILLINOIS - List of Cities
def illinois(request):
	return render(request, "illinois.html", {})



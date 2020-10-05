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


#Chicago
def chicago(request):
	import requests
	import json

	chicago7 = requests.get("https://foodbankapi.herokuapp.com/foodbank/7/?format=json")
	chi7 = json.loads(chicago7.content)

	chicago8 = requests.get("https://foodbankapi.herokuapp.com/foodbank/8/?format=json")
	chi8 = json.loads(chicago8.content)

	chicago9 = requests.get("https://foodbankapi.herokuapp.com/foodbank/9/?format=json")
	chi9 = json.loads(chicago9.content)

	chicago10 = requests.get("https://foodbankapi.herokuapp.com/foodbank/10/?format=json")
	chi10 = json.loads(chicago10.content)

	chicago11 = requests.get("https://foodbankapi.herokuapp.com/foodbank/11/?format=json")
	chi11 = json.loads(chicago11.content)

	return render(request, "chicago.html", {'chi7': chi7, 'chi8': chi8, 'chi9': chi9, 'chi10': chi10, 'chi11': chi11})



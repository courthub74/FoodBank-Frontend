from django.shortcuts import render

#HOME
def home(request):
	intro = "This Is The:"
	nothingyet = "Choose Your State Above"
	return render(request, "home.html", {'nothingyet': nothingyet, 'intro': intro})


#MICHIGAN - List of Cities
def mich(request):
	return render(request, "mich.html", {})

#Detroit
# def det(request):
# 	import requests
# 	import json

# 	detroit = requests.get("")

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

#North Chicago
def chicagonord(request):
	import requests
	import json

	northchi = requests.get("https://foodbankapi.herokuapp.com/foodbank/15/?format=json")
	nchi1 = json.loads(northchi.content)

	return render(request, "northchicago.html", {'nchi1': nchi1})

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

	chicago19 = requests.get("https://foodbankapi.herokuapp.com/foodbank/19/?format=json")
	chi19 = json.loads(chicago19.content)

	chicago20 = requests.get("https://foodbankapi.herokuapp.com/foodbank/20/?format=json")
	chi20 = json.loads(chicago20.content)

	chicago21 = requests.get("https://foodbankapi.herokuapp.com/foodbank/21/?format=json")
	chi21 = json.loads(chicago21.content)

	chicago22 = requests.get("https://foodbankapi.herokuapp.com/foodbank/22/?format=json")
	chi22 = json.loads(chicago22.content)

	chicago23 = requests.get("https://foodbankapi.herokuapp.com/foodbank/23/?format=json")
	chi23 = json.loads(chicago23.content)

	return render(request, "chicago.html", {'chi7': chi7, 'chi8': chi8, 'chi9': chi9, 'chi10': chi10, 'chi11': chi11, 'chi19': chi19, 'chi20': chi20,
		'chi21': chi21, 'chi22': chi22, 'chi23': chi23})


#West Chicago
def westchi(request):
	import requests
	import json

	westchi = requests.get("http://foodbankapi.courdevelops.com/foodbank/16/?format=json")
	chiwest = json.loads(westchi.content)

	westchi2 = requests.get("http://foodbankapi.courdevelops.com/foodbank/17/?format=json")
	chiwest2 = json.loads(westchi2.content)

	westchi3 = requests.get("http://foodbankapi.courdevelops.com/foodbank/18/?format=json")
	chiwest3 = json.loads(westchi3.content)

	return render(request, "westchi.html", {'chiwest': chiwest, 'chiwest2': chiwest2, 'chiwest3': chiwest3})

	

	


#Oak Park
def oakpark(request):
	import requests
	import json

	oakpark = requests.get("http://foodbankapi.courdevelops.com/foodbank/13/?format=json")
	op1 = json.loads(oakpark.content)

	return render(request, "oakpark.html", {'op1': op1})


#Peoria
def peoria(request):
	import requests
	import json

	peoria1 = requests.get("http://foodbankapi.courdevelops.com/foodbank/14/?format=json")
	peoria = json.loads(peoria1.content)

	return render(request, "peoria.html", {'peoria': peoria})



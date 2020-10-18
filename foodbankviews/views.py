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
def det(request):
	import requests
	import json


	gleaners = requests.get("https://foodbankapi.herokuapp.com/foodbank/25/?format=json")
	det1 = json.loads(gleaners.content)

	covenant = requests.get("https://foodbankapi.herokuapp.com/foodbank/29/?format=json")
	det2 = json.loads(covenant.content)

	witts = requests.get("https://foodbankapi.herokuapp.com/foodbank/30/?format=json")
	det3 = json.loads(witts.content)

	twelfth = requests.get("https://foodbankapi.herokuapp.com/foodbank/31/?format=json")
	det4 = json.loads(twelfth.content)

	scott = requests.get("https://foodbankapi.herokuapp.com/foodbank/32/?format=json")
	det5 = json.loads(scott.content)

	salvation = requests.get("https://foodbankapi.herokuapp.com/foodbank/33/?format=json")
	det6 = json.loads(salvation.content)

	restoration = requests.get("https://foodbankapi.herokuapp.com/foodbank/34/?format=json")
	det7 = json.loads(restoration.content)

	perfecting = requests.get("https://foodbankapi.herokuapp.com/foodbank/35/?format=json")
	det8 = json.loads(perfecting.content)

	fathers = requests.get("https://foodbankapi.herokuapp.com/foodbank/36/?format=json")
	det9 = json.loads(fathers.content)

	linwood = requests.get("https://foodbankapi.herokuapp.com/foodbank/37/?format=json")
	det10 = json.loads(linwood.content)

	return render(request, "detroit.html", {'det1': det1, 'det2': det2, 'det3': det3, 'det4': det4, 'det5': det5, 'det6': det6, 'det7': det7, 'det8': det8, 'det9': det9, 'det10': det10})

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

	standys = requests.get("https://foodbankapi.herokuapp.com/foodbank/26/?format=json")
	liv2 = json.loads(standys.content)

	return render(request, "livonia.html", {'liv': liv, 'liv2': liv2})


#Southfield
def southfield(request):
	import requests
	import json

	southfield = requests.get("https://foodbankapi.herokuapp.com/foodbank/6/?format=json")
	south = json.loads(southfield.content)

	franciscan = requests.get("https://foodbankapi.herokuapp.com/foodbank/27/?format=json")
	south2 = json.loads(franciscan.content)

	wordoffaith = requests.get("https://foodbankapi.herokuapp.com/foodbank/28/?format=json")
	south3 = json.loads(wordoffaith.content)

	return render(request, "southfield.html", {'south': south, 'south2': south2, 'south3': south3})


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


#NORTH CAROLINA
def ncaro(request):
	return render(request, "northcarolina.html", {})

#Raleigh
def raleigh(request):
	import requests
	import json

	raleigh1 = requests.get("http://foodbankapi.courdevelops.com/foodbank/38/?format=json")
	nc1 = json.loads(raleigh1.content)

	raleigh2 = requests.get("http://foodbankapi.courdevelops.com/foodbank/39/?format=json")
	nc2 = json.loads(raleigh2.content)

	raleigh3 = requests.get("http://foodbankapi.courdevelops.com/foodbank/40/?format=json")
	nc3 = json.loads(raleigh3.content)

	raleigh4 = requests.get("http://foodbankapi.courdevelops.com/foodbank/41/?format=json")
	nc4 = json.loads(raleigh4.content)

	raleigh5 = requests.get("http://foodbankapi.courdevelops.com/foodbank/42/?format=json")
	nc5 = json.loads(raleigh5.content)

	raleigh6 = requests.get("http://foodbankapi.courdevelops.com/foodbank/43/?format=json")
	nc6 = json.loads(raleigh6.content)

	raleigh7 = requests.get("http://foodbankapi.courdevelops.com/foodbank/44/?format=json")
	nc7 = json.loads(raleigh7.content)

	raleigh8 = requests.get("http://foodbankapi.courdevelops.com/foodbank/45/?format=json")
	nc8 = json.loads(raleigh8.content)

	raleigh9 = requests.get("http://foodbankapi.courdevelops.com/foodbank/46/?format=json")
	nc9 = json.loads(raleigh9.content)

	raleigh10 = requests.get("http://foodbankapi.courdevelops.com/foodbank/47/?format=json")
	nc10 = json.loads(raleigh10.content)


	return render(request, "raleigh.html", {'nc1': nc1, 'nc2': nc2, 'nc3': nc3, 'nc4': nc4, 'nc5': nc5, 'nc6': nc6, 'nc7': nc7, 'nc8': nc8, 'nc9': nc9, 'nc10': nc10})



#Wilmington
def willmington(request):
	import requests
	import json

	willming1 = requests.get("http://foodbankapi.courdevelops.com/foodbank/48/?format=json")
	will1 = json.loads(willming1.content)

	willming2 = requests.get("http://foodbankapi.courdevelops.com/foodbank/49/?format=json")
	will2 = json.loads(willming2.content)

	willming3 = requests.get("http://foodbankapi.courdevelops.com/foodbank/50/?format=json")
	will3 = json.loads(willming3.content)

	willming4 = requests.get("http://foodbankapi.courdevelops.com/foodbank/51/?format=json")
	will4 = json.loads(willming4.content)

	willming5 = requests.get("http://foodbankapi.courdevelops.com/foodbank/52/?format=json")
	will5 = json.loads(willming5.content)

	return render(request, "willmington.html", {'will1': will1, 'will2': will2, 'will3': will3, 'will4': will4, 'will5': will5})


#Hampstead
def hampstead(request):
	import requests
	import json

	hampstead1 = requests.get("http://foodbankapi.courdevelops.com/foodbank/53/?format=json")
	hamp1 = json.loads(hampstead1.content)

	hampstead2 = requests.get("http://foodbankapi.courdevelops.com/foodbank/54/?format=json")
	hamp2 = json.loads(hampstead2.content)

	hampstead3 = requests.get("http://foodbankapi.courdevelops.com/foodbank/55/?format=json")
	hamp3 = json.loads(hampstead3.content)

	return render(request, "hampstead.html", {'hamp1':hamp1, 'hamp2':hamp2, 'hamp3':hamp3})


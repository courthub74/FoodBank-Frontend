from django.shortcuts import render

#HOME
def home(request):
	return render(request, "home.html", {})


#MICHIGAN
def mich(request):
	return render(request, "mich.html", {})


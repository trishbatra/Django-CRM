from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request, "welcome.html", {"name": "Trish"})
def d(request):
    return render(request, "welcome.html", {"name": "D"})
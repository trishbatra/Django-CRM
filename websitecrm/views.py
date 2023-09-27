from django.shortcuts import render

# Create your views here.
def a(request):
    return render(request, "welcome.html", {"name": "Trish"})
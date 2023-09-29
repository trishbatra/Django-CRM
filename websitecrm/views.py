from django.shortcuts import render,redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import signUpForm
from .models import record

# Create your views here.
@login_required(login_url="/signup/")
def add(request):
    if request.method == "POST":
        zipp =  request.POST["zip"]
        phnum =  request.POST["phnum"]
        city =  request.POST["city"]
        print(f"name is {request.user.first_name}")
        createdRecord = record.objects.create(first_name =request.user.first_name, email= request.user.email ,last_name= request.user.last_name, zipCode = zipp, city = city, phone = phnum )
        createdRecord.save()
        return redirect("/")
    else:
        return render(request,"addrecord.html")
def welcome(request):
    current_url = request.build_absolute_uri()
    records = record.objects.all()
    return render(request, "welcome.html", { "url": current_url, "recrds": records })

def login_user(request):
    if request.method == "POST":
        name = request.POST["username"]
        passwrd = request.POST["pass"]
        user = authenticate(request, username=name, password=passwrd)
        if user is not None:
            login(request, user)
            messages.info(request, "LOGGED IN SUCCESSFULLY")
            return redirect("/")
        else:
            messages.error(request, "There was an error logging in. Please try again.")
            return redirect("/")
    else:
        return  redirect("/")
def signup_user(request):
    if request.method == "POST":
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data["username"], password = form.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "signed up successfully✅")
            return redirect("/")
    else:
        form = signUpForm()
        return  render(request, "register.html", {"form": form})
    return  render(request, "register.html", {"form": form})
   
@login_required(login_url="/signup/")
def doc(request):
    idd = request.GET.get("id")
    theR = record.objects.get(id=idd)
    return render(request,"particular.html", {"r": theR})
@login_required(login_url="/signup/")
def lgout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect("/")
@login_required(login_url="/signup/")
def delete(request, id):
    recordToDelete = record.objects.get(id=id)
    recordToDelete.delete()
    messages.success(request, "record deleted")
    return redirect("/")
@login_required(login_url="/signup/")
def update(request,id):
    recordToUpdate= record.objects.get(id=id)
    if request.method == "POST":
        zipp   = request.POST["zip"]
        phnum  = request.POST["phnum"]
        city  = request.POST["city"]
        recordToUpdate.zipCode = zipp
        recordToUpdate.phone = phnum
        recordToUpdate.city = city
        messages.info(request, "record updated")
        recordToUpdate.save()
        return redirect("/")
    else:
        return render(request,"update.html", {"r": recordToUpdate})
from . import views
from django.urls import path

app_name = "websitecrm"
urlpatterns = [
    path("", views.welcome,name="welcome" ),
    path("d/", views.d, name="d" )
]

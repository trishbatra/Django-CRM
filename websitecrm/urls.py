from . import views
from django.urls import path

app_name = "websitecrm"
urlpatterns = [
    path("", views.welcome,name="welcome" ),
    path("login/", views.login_user, name="login" ),
    path("signup/", views.signup_user, name="signup" ),
    path("lgout/", views.lgout, name="lgout" ),
    path("add/", views.add, name="add" ),
    path("doc/", views.doc, name="doc" ),
    path("delete/<int:id>", views.delete, name="delete" ),
    path("update/<int:id>/", views.update, name="update" ),
]

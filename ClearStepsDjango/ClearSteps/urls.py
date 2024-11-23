from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("personalityEntry",views.PersonalityEntry),
    path("getPersonality",views.getPersonality)
]

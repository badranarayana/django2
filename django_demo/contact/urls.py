# we are going keep all contact app specific url here and map appropriate view function
from django.urls import path
from .views import index, get_contact, create_contact

urlpatterns = [
    path('index', index),
    path('get-contacts', get_contact),
    path('create', create_contact),
]
# we are going keep all contact app specific url here and map appropriate view function
from django.urls import path
from .views import index, get_contact, create_contact, list_contacts

urlpatterns = [
    path('index', index, name='index'),
    path('get-contacts', get_contact, name='get-contacts'),
    path('create', create_contact, name='create-contact'),
]
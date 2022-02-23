from django.db import models

# Create your models here.
class Contact(models.Model): # class name is the table name in db
    # lets define column for db table
    name = models.CharField(max_length=60, null=True)
    mobile_number = models.CharField(max_length=10)
    date_of_birth = models.DateField()
    email = models.EmailField()
    location = models.CharField(max_length=15, null=True)

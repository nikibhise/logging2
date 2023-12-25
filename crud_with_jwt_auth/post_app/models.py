from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

room_type = [('AC', 'AC'), ('Non-AC', 'Non-AC')]

class Hotel(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    Room_type = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    contact_no = PhoneNumberField(region="IN")
    adharcard_no = models.CharField(max_length=20)
    email = models.EmailField()
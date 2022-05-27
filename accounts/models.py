from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class User(AbstractUser):
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    birthdate = models.DateField(null=True)
    email = models.EmailField()
    station_employees = (
        ('driver', 'driver'),
        ('shunt', 'shunt'),
        ('station_employe', 'station_employe'),
    )
    employees = models.CharField(max_length=20, choices=station_employees)
    photo = models.ImageField(upload_to='user/')
    phone_number=PhoneNumberField("NATIONAL", region='EG')

    def __str__(self):
         return self.full_name
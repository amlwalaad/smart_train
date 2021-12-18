from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # user_id=models.PositiveIntegerField()
    full_name=models.CharField(max_length=100)
    address=models.TextField()
    birthdate=models.DateField(null=True)
    email=models.EmailField()
    station_employees=(
        ('driver','driver'),
        ('shunt','shunt'),
        ('station_employe','station_employe'),
    )
    employees=models.CharField(max_length=20 , choices=station_employees)
    def __str__(self):
        return self.full_name

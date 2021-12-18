from django.db import models
from accounts.models import User


# Create your models here.

class Driver(models.Model):
    driver_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    photo = models.ImageField(upload_to='driver/')

    def __str__(self):
        return str(self.driver_id)

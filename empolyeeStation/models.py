from django.db import models
from accounts.models import User
from driver.models import Train
from shunt_factor.models import Shunt


# Create your models here.

class Station(models.Model):
    station_name = models.CharField(max_length=50, primary_key=True)
    location = models.IntegerField()


class Trip(models.Model):
    trip_id = models.IntegerField(primary_key=True)
    trip_name = models.CharField(max_length=200)
    train_number = models.ForeignKey(Train, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.trip_name)


class Path(models.Model):
    trip_id = models.ForeignKey(Trip, on_delete=models.CASCADE)
    station_name = models.ForeignKey(Station, on_delete=models.CASCADE)
    shunt_name = models.ForeignKey(Shunt, on_delete=models.CASCADE)
    time=models.TimeField()

class Employee(models.Model):
    employee_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    station_name=models.ForeignKey(Station,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.employee_id)

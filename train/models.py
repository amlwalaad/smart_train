from django.db import models


# Create your models here.

class Train(models.Model):
    train_number = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Trip(models.Model):
    trip_id = models.IntegerField(primary_key=True, unique=True)
    start_station = models.CharField(max_length=50)
    end_station = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    train_id = models.ForeignKey(Train, on_delete=models.CASCADE)

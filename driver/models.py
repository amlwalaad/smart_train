from django.db import models
from accounts.models import User


# Create your models here.
class Train(models.Model):
    train_number= models.IntegerField(primary_key=True)
    train_type=models.CharField(max_length=50)
    def __str__(self):
        return str(self.train_number)
class Driver(models.Model):
    driver_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    train_number=models.ForeignKey(Train,on_delete=models.CASCADE)

    # def __str__(self):
    #     return str(self.driver_id)




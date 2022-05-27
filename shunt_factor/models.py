from django.db import models
from accounts.models import User
# Create your models here.

class Shunt(models.Model):
    shunt_name=models.CharField(max_length=50,primary_key=True)
    location=models.IntegerField()
    def __str__(self):
        return str(self.shunt_name)
class ShuntFactor(models.Model):
    shunt_factor_id = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    shunt_name = models.ForeignKey(Shunt, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.shunt_factor_id)
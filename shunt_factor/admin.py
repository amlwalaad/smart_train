from django.contrib import admin
from shunt_factor.models import Shunt , ShuntFactor

# Register your models here.
admin.site.register(ShuntFactor)
admin.site.register(Shunt)
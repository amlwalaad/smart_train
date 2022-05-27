from django.contrib import admin
from .models import Station , Trip , Path
# Register your models here.
admin.site.register(Station)
admin.site.register(Trip)
admin.site.register(Path)
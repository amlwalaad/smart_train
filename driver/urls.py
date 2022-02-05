from django.urls import path ,include
from . import views
urlpatterns = [
    path('selecttrip/' ,views.selecttripView , name='selecttrip' ),
    path('driverLogin/',views.login_driver,name='driverLogin'),
]

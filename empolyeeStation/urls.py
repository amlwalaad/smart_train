from django.urls import path
from empolyeeStation import views
urlpatterns=[

    path('welcomeEmployee/',views.welcomeEmployee , name="welcomeEmployee"),
    path('employeeStationlogin/',views.empolyeeStationLogin , name="employee_Station_Login"),
]
from django.shortcuts import render
from driver.models import Driver
from shunt_factor.models import ShuntFactor
from empolyeeStation.models import Employee
from accounts.models import User


def welcomeView(request):
    return render(request, 'welcomePage.html')


def profileview(request):
    if request.user.groups.all()[0].name == 'drivers':
        job = 'سائق'
        details = Driver.objects.filter(pk=request.user).train_number
    elif request.user.groups.all()[0].name == 'shunt-factor':
        job = 'عامل تحويلة'
        shuntfactor = ShuntFactor.objects.filter(pk=request.user)[0]
        details = shuntfactor.shunt_name
    else:
        job = 'موظف هيئة'
        employee = Employee.objects.filter(pk=request.user)
        details = employee.station_name
    context = {'name': request.user.full_name, 'id': request.user.username, 'job': job, 'details': details,
               'phonenumber': request.user.phone_number, 'birthdate': request.user.birthdate,
               'email': request.user.email}
    return render(request, 'profile.html', context)

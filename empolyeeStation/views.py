from django.shortcuts import render ,redirect
from empolyeeStation.decorators import unauthenticatedEmployeeStation , allowed_only_empolyeeStation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
@unauthenticatedEmployeeStation
def empolyeeStationLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcomeEmployee')
        else:
            messages.info(request,
                          'الرقم السرى او الرقم القومى غير صحيح بالرجاء التاكد من صحة الرقم السرى او الرقم القومى')
    return render(request, 'empolyeeStation/empolyeeStationLogin.html')


@login_required(login_url='employee_Station_Login')
@allowed_only_empolyeeStation(allowed_list=['station_employee'])
def welcomeEmployee(request):

    return render(request,'empolyeeStation/welcomeEmpolyeeStation.html')




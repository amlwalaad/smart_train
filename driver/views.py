from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from .decorators import unauthenticated_driver, allowed_only_drivers
from django.contrib.auth.decorators import login_required


# Create your views here.
@unauthenticated_driver
def login_driver(request):
    username = password = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('selecttrip')
        else:
            messages.info(request,
                          'الرقم السرى او الرقم القومى غير صحيح بالرجاء التاكد من صحة الرقم السرى او الرقم القومى')
    return render(request, 'driver/driverLogin.html')


@login_required(login_url='driverLogin')
@allowed_only_drivers(allowed_list=["drivers"])
def selecttripView(request):
    context = {}
    return render(request, 'driver/selectTrip.html', context)

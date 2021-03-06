from django.shortcuts import render, redirect
from .decorators import unauthenticated_shunt_factor , allowed_only_shunt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@unauthenticated_shunt_factor
def shuntLogin(request):
    username = password = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('welcomeshunt')
        else:
            messages.info(request,
                          'الرقم السرى او الرقم القومى غير صحيح بالرجاء التاكد من صحة الرقم السرى او الرقم القومى')
    return render(request, 'shunt_factor/shuntLogin.html')


@login_required(login_url='shuntLogin')
@allowed_only_shunt(allowed_list=["shunt-factor"])
def welcomeshunt(request):
    return render(request, 'shunt_factor/welcomeshunt.html')


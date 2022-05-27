from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import logout

def unauthenticatedEmployeeStation(viewFunction):
    def wrapper_func(request ,*args , **kwargs):
        if request.user.is_authenticated:
            return redirect('welcomeEmployee')
        else:
            return viewFunction(request,*args,**kwargs)
    return wrapper_func


def allowed_only_empolyeeStation(allowed_list=[]):
    def decorator(view_func):
        def wrapper_function(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_list:
                return view_func(request, *args, **kwargs)
            else:
                logout(request)
                messages.info(request,
                              'انت لست موظف هيئة  لا يمكنك الدخول ')
                return redirect('employee_Station_Login')

        return wrapper_function

    return decorator

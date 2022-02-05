from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages


def unauthenticated_driver(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('selecttrip')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


def allowed_only_drivers(allowed_list=[]):
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
                              'انت لست سائق  لا يمكنك الدخول ')
                return redirect('driverLogin')

        return wrapper_function

    return decorator

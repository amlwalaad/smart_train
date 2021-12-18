from django.http import HttpResponse
from django.shortcuts import redirect


def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('selecttrip')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_user(allowed_list=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            print(allowed_list)
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                if group in allowed_list:
                    return view_func(request, *args, **kwargs)
            return view_func(request, *args, **kwargs)

        return wrapper_func

    return decorator

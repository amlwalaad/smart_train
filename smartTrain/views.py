from django.shortcuts import render

def welcomeView(request):
    return render(request,'welcomePage.html')
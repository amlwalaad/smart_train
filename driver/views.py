from django.shortcuts import render, redirect
import datetime  # for get date
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render
from accounts.decorators import unauthenticated_user, allowed_user
from django.contrib.auth.decorators import login_required


# Create your views here.
@unauthenticated_user
@allowed_user(allowed_list=['driver'])
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


def driver_logout(request):
    logout(request)
    return redirect('driverLogin')


# function to get date in arabic
def arabicday(arday):
    if arday == 'sun':
        return 'الاحد'
    elif arday == 'Mon':
        return 'الاثنين'
    elif arday == 'Tues':
        return 'الثلاثاء'
    elif arday == 'Wednes':
        return 'الاربعاء'
    elif arday == 'Thurs':
        return 'الخميس'
    elif arday == 'Fri':
        return 'الجمعة'
    elif arday == 'Satur':
        return 'السبت'


def arabicmonth(englishmonth):
    if englishmonth == 'September':
        return 'سيتمير'
    elif englishmonth == 'October':
        return "اكتوبر"
    elif englishmonth == 'November':
        return "نوفمبر"
    elif englishmonth == 'December':
        return "ديسمبر"
    elif englishmonth == 'January':
        return "يناير"
    elif englishmonth == 'February':
        return "فبراير"
    elif englishmonth == 'March':
        return "مارس"
    elif englishmonth == 'April':
        return "ابريل"
    elif englishmonth == 'May':
        return "مايو"
    elif englishmonth == 'June':
        return "يونيو"
    elif englishmonth == 'July':
        return "يوليو"
    elif englishmonth == 'August':
        return "اغسطس"

@login_required(login_url='driverLogin')
@allowed_user(allowed_list=['driver'])
def selecttripView(request):
    currentDate = datetime.datetime.now()
    day = currentDate.strftime('%a')
    numday = currentDate.strftime('%d')
    month = currentDate.strftime('%B')
    year = currentDate.strftime('%Y')
    arbday = arabicday(day)
    arbmonth = arabicmonth(month)
    context = {'day': arbday, 'numday': numday, 'month': arbmonth, 'year': year}
    return render(request, 'driver/selectTrip.html', context)

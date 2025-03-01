import json
from django.shortcuts import render
from django.contrib.auth.models import User
from .prayer_shedule import PrayerSchedule
from .models import UserAccounts
from django.template import loader
from django.http import HttpResponse
# from .models import Task


def home(request):
    # tasks = Task.objects.all()
    schedule = PrayerSchedule("Tokyo", "Japan") 
    schedule.set_up_schedule()
    timeTable = [
         { "prayer": "Fajr", "starttime" : schedule.time_chart_start["Fajr"], "endtime" : schedule.time_chart_end["Fajr"] },
         { "prayer": "Dhuhr", "starttime" : schedule.time_chart_start["Dhuhr"], "endtime" : schedule.time_chart_end["Dhuhr"] },
         { "prayer": "Asr", "starttime" : schedule.time_chart_start["Asr"], "endtime" : schedule.time_chart_end["Asr"] },
         { "prayer": "Maghrib", "starttime" : schedule.time_chart_start["Maghrib"], "endtime" : schedule.time_chart_end["Maghrib"] },
         { "prayer": "Isha", "starttime" : schedule.time_chart_start["Isha"], "endtime" : schedule.time_chart_end["Isha"] },
    ]
    
    return render(request, 'home.html', {
        'timeTable': timeTable,
        'date' : schedule.date,
        'day' : schedule.day,
    })


def product_list(request):
    users = User.objects.all()
    persons = [  { "name" : user.username } for user in users ]

    products = [
        {"name": "Banana", "price": 2168},
        {"name": "Crossiant", "price": 998},
        {"name": "Grape", "price": 1598},
        {"name": "Paprika (Capsicum)", "price": 1298},
        {"name": "Muffin", "price": 1598}
    ]

    context = {
        "persons": persons,
        "products": products
    }

    return render(request, "products_list.html", 
        {
            "persons": json.dumps(persons),
            "products": json.dumps(products)
        }
    )


def dashboard(request):
    user_data = UserAccounts.objects.all()
    current_user = request.user
    username = current_user.username
    # print(user_accounts)
    desired_user = None
    for user_info in user_data:
        if(user_info.name.lower() == username):
            desired_user = { "name" : user_info.name, "balance" : user_info.balance, "due" : user_info.due }
            print(desired_user)
    if desired_user == None:
        print("DEBUG: No matching user found")
    return render(request, "dashboard.html", {
        "useracc" : desired_user 
    })



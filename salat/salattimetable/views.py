import json
from django.shortcuts import render
from django.contrib.auth.models import User
from .prayer_shedule import PrayerSchedule
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
from django.contrib import admin
from .models import Task,UserAccounts

admin.site.register(Task)




class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['name', 'balance', 'due']

admin.site.register(UserAccounts, UserAccountAdmin)
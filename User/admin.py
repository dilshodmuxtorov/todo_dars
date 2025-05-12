from django.contrib import admin
from .models import UserModel

class UserModelAdmin(admin.ModelAdmin):
    list_display = ['name','surname','age','email','id']


admin.site.register(UserModel,UserModelAdmin)
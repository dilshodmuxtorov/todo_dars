from django.contrib import admin
from .models import TodoModel

class TodoMOdelAdmin(admin.ModelAdmin):
    list_display= ['work','deadline','user_id','id', "is_finished"]

admin.site.register(TodoModel,TodoMOdelAdmin)
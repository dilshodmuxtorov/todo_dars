from django.urls import path
from .views import TodoListView
urlpatterns = [
    path('list/',TodoListView.as_view())
]
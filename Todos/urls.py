from django.urls import path
from .views import TodoListView, RetrieveTodoView
urlpatterns = [
    path('list/',TodoListView.as_view()),
    path('list/<int:pk>/',RetrieveTodoView.as_view()),
]
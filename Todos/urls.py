from django.urls import path
from .views import *
urlpatterns = [
    path('list/',TodoListView.as_view()),
    path('list/<int:pk>/',RetrieveTodoView.as_view()),
    path('create/', CreateTodoView.as_view()),
    path('delete/<int:pk>/', DeleteTodoView.as_view()), 
    path('setactive/<int:pk>/', SetFinishedTrueView.as_view()), 

]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('words/', views.word_list, name='word_list'),
    path('words/add/', views.word_add, name='word_add'),
    path('lessons/', views.lesson_list, name='lesson_list'),
    path('lessons/add/', views.lesson_add, name='lesson_add'),
]

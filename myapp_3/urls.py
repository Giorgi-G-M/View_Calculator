from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('odd_or_even/<int:number>', views.even_odden),
]

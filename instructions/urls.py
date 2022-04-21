""" Instructions URLs """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.instructions, name='instructions'),
    path('add/', views.add_recipe, name='add_recipe'),
]

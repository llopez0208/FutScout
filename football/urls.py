from django.urls import path
from . import views

urlpatterns = [
    path('teams/', views.team_list, name='team_list'),
    path('players/', views.player_list, name='player_list'),
]

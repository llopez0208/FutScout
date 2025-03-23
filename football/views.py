from django.shortcuts import render
from .models import Team, Player

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'football/team_list.html', {'teams': teams})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'football/player_list.html', {'players': players})

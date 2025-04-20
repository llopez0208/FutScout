from django.shortcuts import render
from .models import Team, Player

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'football/team_list.html', {'teams': teams})

def player_list(request):
    players = Player.objects.all()
    return render(request, 'football/player_list.html', {'players': players})

def create_test_player(request):
    # Create a team
    team = Team.objects.create(name="Example FC", founded_year=1990, country="England")

    # Create a player with the attributes you provided
    player = Player.objects.create(
        name="Nicolas Jackson",
        position="ST",  # Striker position
        team=team,
        goals=9,
        assists=4,
        matches_played=25,
        shooting=13,
        passing=12,
        dribbling=14,
        tackling=6,
        vision=10,
        stamina=13,
        heading=13,
        off_the_ball=16,
        crossing=8,
        reflexes=0,
        handling=0
    )

    # Assign role to the player
    role = player.assign_role()

    # Render response with the player's role
    return render(request, 'player_role.html', {'player': player, 'role': role})
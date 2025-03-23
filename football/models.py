from django.db import models

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    country = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name

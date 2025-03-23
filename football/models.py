from django.db import models

# Define Team Model
class Team(models.Model):
    name = models.CharField(max_length=100)
    founded_year = models.IntegerField()
    country = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)

    def __str__(self):
        return self.name


# Define Player Model
class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    matches_played = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def assign_role(self):
        """
        Assigns a role based on the player's position (without any statistics-based logic yet).
        """
        if self.position == 'ST':
            return Striker().get_role()
        elif self.position == 'LW' or self.position == 'RW':
            return Winger().get_role()
        elif self.position == 'CAM':
            return AttackingMidfielder().get_role()
        elif self.position == 'CM':
            return CentralMidfielder().get_role()
        elif self.position == 'CDM':
            return DefensiveMidfielder().get_role()
        elif self.position == 'RB' or self.position == 'LB':
            return Fullback().get_role()
        elif self.position == 'CB':
            return CenterBack().get_role()
        elif self.position == 'GK':
            return Goalkeeper().get_role()
        else:
            return "General Role"


# Role Classes for Striker (ST)
class Striker:
    def get_role(self):
        return "Striker Role (To be assigned later)"

# Role Classes for Winger (LW / RW)
class Winger:
    def get_role(self):
        return "Winger Role (To be assigned later)"

# Role Classes for Attacking Midfielder (CAM)
class AttackingMidfielder:
    def get_role(self):
        return "Attacking Midfielder Role (To be assigned later)"

# Role Classes for Central Midfielder (CM)
class CentralMidfielder:
    def get_role(self):
        return "Central Midfielder Role (To be assigned later)"

# Role Classes for Defensive Midfielder (CDM)
class DefensiveMidfielder:
    def get_role(self):
        return "Defensive Midfielder Role (To be assigned later)"

# Role Classes for Fullback (RB / LB)
class Fullback:
    def get_role(self):
        return "Fullback Role (To be assigned later)"

# Role Classes for Center Back (CB)
class CenterBack:
    def get_role(self):
        return "Center Back Role (To be assigned later)"

# Role Classes for Goalkeeper (GK)
class Goalkeeper:
    def get_role(self):
        return "Goalkeeper Role (To be assigned later)"

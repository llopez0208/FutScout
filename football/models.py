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

    # Player statistics
    shooting = models.IntegerField(default=0)
    passing = models.IntegerField(default=0)
    dribbling = models.IntegerField(default=0)
    tackling = models.IntegerField(default=0)
    vision = models.IntegerField(default=0)
    stamina = models.IntegerField(default=0)
    heading = models.IntegerField(default=0)
    off_the_ball = models.IntegerField(default=0)
    crossing = models.IntegerField(default=0)
    reflexes = models.IntegerField(default=0)
    handling = models.IntegerField(default=0)

# Role Classes for Striker (ST)
class Striker:
    def __init__(self, player):
        self.player = player

    def get_role(self):
        if self.player.shooting > 15:
            return "Advanced Forward"
        elif self.player.off_the_ball > 15:
            return "Pressing Forward"
        elif self.player.heading > 12:
            return "Target Man"
        else:
            return "Deep Lying Forward"


# Role Classes for Winger (LW / RW)
class Winger:
    def __init__(self, player):
        self.player = player

    def get_role(self):
        if self.player.dribbling > 15:
            return "Inside Forward"
        elif self.player.passing > 14:
            return "Winger"
        else:
            return "Inverted Winger"


# Role Classes for Attacking Midfielder (CAM)
class AttackingMidfielder:
    def __init__(self, player):
        self.player = player

    def get_role(self):
        if self.player.passing > 15 and self.player.vision > 15:
            return "Advanced Playmaker"
        elif self.player.shooting > 12:
            return "Shadow Striker"
        else:
            return "Attacking Midfielder "


# Role Classes for Central Midfielder (CM)
class CentralMidfielder:
    def __init__(self, player):
        self.player = player

    def get_role(self):
        if self.player.tackling > 12 and self.player.stamina > 14:
            return "Ball Winning Midfielder"
        elif self.player.passing > 14:
            return "Deep Lying Playmaker"
        elif self.player.stamina > 15:
            return "Box to Box"
        else:
            return "Mezzala"


# Role Classes for Defensive Midfielder (CDM)
class DefensiveMidfielder:
    def __init__(self, player):
        self.player = player

    def get_role(self):
        if self.player.tackling > 15:
            return "Defensive Midfielder"
        elif self.player.passing > 13:
            return "Regista"
        else:
            return "Anchor"


# Role Classes for Fullback (RB / LB)
class Fullback:
    def __init__(self, player):
        self.player = player

    def get_role(self):
        if self.player.crossing > 14:
            return "Wing Back"
        elif self.player.tackling > 12:
            return "Fullback"
        else:
            return "Inverted Fullback"


# Role Classes for Center Back (CB)
class CenterBack:
    def __init__(self, player):
        self.player = player

    def get_role(self):
        if self.player.tackling > 15 and self.player.strength > 15:
            return "Ball Playing Defender"
        elif self.player.positioning > 14:
            return "Stopper"
        else:
            return "Central Defender"


# Role Classes for Goalkeeper (GK)
class Goalkeeper:
    def __init__(self, player):
        self.player = player

    def get_role(self):
        if self.player.reflexes > 15:
            return "Sweeper Keeper"
        elif self.player.handling > 15:
            return "Goalkeeper"
        else:
            return "Goalkeeper"




    def __str__(self):
        return self.name
    
    def assign_role(self):
        """
        Assigns a role based on the player's position and statistics(1-20 scale).
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

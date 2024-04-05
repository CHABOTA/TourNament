from django.forms import ValidationError
from django.utils import timezone
from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.name
    
class Tournament(models.Model):
    sport = models.CharField(max_length=16)
    saison = models.CharField(max_length=16)

    def __str__(self) -> str:
        return self.sport + " : " + self.saison

class Match(models.Model):
    date_time = models.DateTimeField(default=timezone.now())
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team, related_name="team1", on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team, related_name="team2", on_delete=models.CASCADE)
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)
    winner = models.CharField(default="", max_length=16)

    def __str__(self) -> str:
        return self.team1.name + " vs " + self.team2.name
    
    def setWinner(self):
        if self.score_team1 > self.score_team2:
            self.winner = self.team1.name
        else:
            self.winner = self.team2.name

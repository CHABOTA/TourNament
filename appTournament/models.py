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
    teams = models.ManyToManyField(Team, default=None, related_name="teams")
    score_team1 = models.IntegerField(default=0)
    score_team2 = models.IntegerField(default=0)
    winner = models.CharField(default=None, max_length=16)

    def __str__(self) -> str:
        return self.teams[0] + " vs " + self.teams[1]
    
    def clean(self):
        teams = self.cleaned_data.get('teams')
        if teams and teams.count() > 2:
            raise ValidationError('Maximum two teams are allowed.')
        return self.cleaned_data
    
    def setWinner(self):
        if self.score_team1 > self.score_team2:
            self.winner = self.teams[0].name
        else:
            self.winner = self.teams[1].name

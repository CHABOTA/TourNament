from django import forms
from appTournament.models import Match, Team, Tournament


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['date_time', 'tournament', 'team1', 'team2']

class UpdateMatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ['score_team1', 'score_team2']

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['sport', 'saison']

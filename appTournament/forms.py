from django import forms
from appTournament.models import Team, Tournament


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name']

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['sport', 'saison']

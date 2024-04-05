from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404

from appTournament.forms import MatchForm, TeamForm, TournamentForm, UpdateMatchForm
from appTournament.models import Match, Team, Tournament

# Create your views here.

def index(request):
    return render(request, 'index.html')

def inscription(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = TeamForm()

    context = {
        'title': 'Inscription',
        'form': form,
        'teams': Team.objects.all(),
    }

    return render(request, 'inscription.html', context)

def gestionMatchs(request):
    if request.method == "POST":
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = MatchForm()

    context = {
        'title': 'Gestion des matchs',
        'form': MatchForm(),
        'teams': Team.objects.all(),
        'tournaments': Tournament.objects.all(),
        'matchs': Match.objects.all().order_by('date_time'),
    }

    return render(request, 'gestion-matchs.html', context)

def addTournament(request):
    if request.method == "POST":
        form = TournamentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
    else:
        form = TournamentForm()

    context = {
        'title': 'Ajouter un tournois',
        'form': TournamentForm(),
        'tournaments': Tournament.objects.all()
    }

    return render(request, 'tournament.html', context)

def getMatch(request, numero):
    if request.method == "POST":
        form = UpdateMatchForm(request.POST)
        if form.is_valid():
            match_instance = Match.objects.latest('id')
            match_instance.score_team1 = form.cleaned_data['score_team1']
            match_instance.score_team2 = form.cleaned_data['score_team2']
            match_instance.setWinner()
            match_instance.save()
            return redirect('../')
    else:
        try:
            match = get_object_or_404(Match, pk=numero)
            
            if match.date_time < timezone.now():
                timeBefore = True
            else:
                timeBefore = False

            
                
            context = {
                'title': match.__str__(),
                'match': match,
                'timeBefore': timeBefore
            }
            return render(request, 'match.html', context)
        except:
            context = {
                'title': 'Erreur 404',
                'numero': numero,
            }
            return render(request, 'page404.html', context)

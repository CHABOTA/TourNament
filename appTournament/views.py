from django.shortcuts import render

from appTournament.forms import TeamForm, TournamentForm
from appTournament.models import Team, Tournament

# Create your views here.

def index(request):
    return render(request, 'index.html')

def inscription(request):
    if request.method == "POST":
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TeamForm()

    context = {
        'title': 'Inscription',
        'form': form,
        'teams': Team.objects.all()
    }
    form = None

    return render(request, 'inscription.html', context)

def gestionMatchs(request):
    context = {
        'title': 'Gestion des matchs',
        #'form': TeamForm()
    }
    return render(request, 'gestion-matchs.html', context)

def addTournament(request):
    context = {
        'title': 'Ajouter un tournois',
        'form': TournamentForm(),
        'tournaments': Tournament.objects.all()
    }
    return render(request, 'tournament.html', context)

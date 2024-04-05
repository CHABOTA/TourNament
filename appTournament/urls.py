from django.urls import path

from appTournament.views import addTournament, gestionMatchs, getMatch, index, inscription

urlpatterns = [
    path('', index),
    path('inscriptions/', inscription),
    path('matchs/', gestionMatchs),
    path('tournois/', addTournament),
    path('matchs/<int:numero>/', getMatch)
]
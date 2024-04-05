from django.contrib import admin

from appTournament.models import Match, Team, Tournament

# Register your models here.
admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Match)
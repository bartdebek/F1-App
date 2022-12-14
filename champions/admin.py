from django.contrib import admin
from django.db.models import F
from .models import Country, Team, Driver, SeasonResults


@admin.action(description='Add race to selected drivers / teams')
def add_race(modeladmin, request, queryset):
    queryset.update(total_races=F('total_races') + 1)

@admin.action(description='Add win to selected drivers / teams')
def add_win(modeladmin, request, queryset):
    queryset.update(number_of_wins=F('number_of_wins') + 1)

@admin.action(description='Add podium to selected drivers / teams')
def add_podium(modeladmin, request, queryset):
    queryset.update(total_podiums=F('total_podiums') + 1)


class DriverModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'nationality', 'active')
    ordering = ['-active', 'last_name']
    actions = [add_race, add_win, add_podium]


class TeamModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'country', 'active')
    ordering = ['-active', 'name']
    actions = [add_race, add_win, add_podium]


class SeasonResultsModelAdmin(admin.ModelAdmin):
    list_display = ('driver', 'team', 'date_updated', 'points')
    list_editable = ('points',)
    list_display_links = ('driver', 'team')
    ordering = ['-points',]



admin.site.register(Country)
admin.site.register(Team, TeamModelAdmin)
admin.site.register(Driver, DriverModelAdmin)
admin.site.register(SeasonResults, SeasonResultsModelAdmin)
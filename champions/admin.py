from django.contrib import admin
from .models import Country,Team,Driver

# Register your models here.
admin.site.register(Country)
admin.site.register(Team)

@admin.register(Driver)
class DriverModelAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'team', 'nationality', 'active')

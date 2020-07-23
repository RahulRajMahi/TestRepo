from django.contrib import admin
from IPLteam.models import team

# Register your models here.
class teamAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner', 'home_city', ]

admin.site.register(team, teamAdmin)

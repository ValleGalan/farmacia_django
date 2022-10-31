from django.contrib import admin

from farmacia_app.models import Farmacia
# Register your models here.

@admin.register(Farmacia)
class FarmaciaAdmin(admin.ModelAdmin):
    pass

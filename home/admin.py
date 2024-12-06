from django.contrib import admin

from django.contrib import admin
from .models import Sala

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nome', 'area', 'url')
    list_filter = ('area',)
    search_fields = ('nome', 'numero')


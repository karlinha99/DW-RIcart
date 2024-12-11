from django.contrib import admin
from .models import Doador, Doacao

@admin.register(Doador)
class DoadorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone')

@admin.register(Doacao)
class DoacaoAdmin(admin.ModelAdmin):
    list_display = ('doador', 'valor', 'data')

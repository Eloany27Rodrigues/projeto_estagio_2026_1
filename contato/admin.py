from django.contrib import admin
from .models import Mensagem

@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    # Isso faz com que as mensagens apareçam em colunas organizadas
    list_display = ('nome', 'email', 'data_envio')
    # Adiciona um campo de busca por nome ou email
    search_fields = ('nome', 'email')
    # Adiciona um filtro lateral por data
    list_filter = ('data_envio',)

from django.apps import AppConfig


class ApiConfig(AppConfig): # Configuração da aplicação padrão do Django
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'

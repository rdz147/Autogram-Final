from django.apps import AppConfig

class AutoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auto'

class BlogConfig(AppConfig):
    name = 'auto'

    def ready(self):
        import auto.signals
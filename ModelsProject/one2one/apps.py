from django.apps import AppConfig


class One2OneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'one2one'
    def ready(self):
        import one2one.signals

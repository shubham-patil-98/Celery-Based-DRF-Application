from django.apps import AppConfig
from django.core.signals import request_finished

class OrdersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'

    def ready(self):
        # import orders.signals  
        from .import signals
        # Explicitly connect a signal handler.
        # request_finished.connect(signals.log_request)
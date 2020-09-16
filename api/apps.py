from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'
    def ready(self):
        from videocollector import scheduler
        scheduler.start()
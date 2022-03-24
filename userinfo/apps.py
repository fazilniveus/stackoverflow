from django.apps import AppConfig


class UserinfoConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'userinfo'

    def ready(self) -> None:
        import userinfo.signals

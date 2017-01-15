from django.apps import AppConfig


class AuthConfig(AppConfig):
    name = '{{cookiecutter.project_slug}}.auth'
    verbose_name = "Auth"

    def ready(self):
        pass

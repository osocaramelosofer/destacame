from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class PersonsConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'destacame.persons'
    verbose_name = _("Persons")

    def ready(self):
        try:
            pass
        except ImportError:
            pass

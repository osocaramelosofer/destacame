from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class JourneysConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'destacame.journeys'
    verbose_name = _("Journeys")

    def ready(self):
        try:
            pass
        except ImportError:
            pass

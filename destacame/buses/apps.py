from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class BusesConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = "destacame.buses"
    verbose_name = _("Buses")

    def ready(self):
        try:
            pass
        except ImportError:
            pass

"""Django App module."""
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class POAppConfig(AppConfig):
    """Photosoverride Django app."""

    name = "photosoverride"
    verbose_name = _("Photos Override")
    default_auto_field = "django.db.models.BigAutoField"

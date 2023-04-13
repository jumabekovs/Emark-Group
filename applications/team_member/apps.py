from django.apps import AppConfig


class TeamMemberConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.team_member'
    verbose_name = "Команда"
from django.core.management.base import BaseCommand
from gestion.models import Project, Task, TeamMember, TechnicalDocument, Milestone,User

class Command(BaseCommand):
    def handle(self, *args, **options):
        Project.objects.all().delete()
        Task.objects.all().delete()
        TeamMember.objects.all().delete()
        TechnicalDocument.objects.all().delete()
        Milestone.objects.all().delete()
        User.objects.all().delete()
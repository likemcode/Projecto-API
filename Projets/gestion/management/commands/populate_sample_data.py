from django.core.management.base import BaseCommand
from gestion.factories import ProjectFactory, TaskFactory, TeamMemberFactory, TechnicalDocumentFactory, MilestoneFactory

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Create sample data
        for _ in range(10):  # Create 10 projects
            project = ProjectFactory()
            for _ in range(5):  # Create 5 tasks for each project
                task = TaskFactory(project=project)
                # Create related TechnicalDocuments
                for _ in range(2):  # Create 2 technical documents for each task
                    technical_document = TechnicalDocumentFactory(task=task)

            for _ in range(3):  # Create 3 team members for each project
                team_member = TeamMemberFactory(project=project)

            # Create related Milestones
            for _ in range(4):  # Create 4 milestones for each project
                milestone = MilestoneFactory(project=project)

        self.stdout.write(self.style.SUCCESS('Sample data populated successfully.'))

import factory
from factory.django import DjangoModelFactory
from .models import Project, Task, TeamMember, TechnicalDocument, Milestone
from django.contrib.auth.models import User  # Import User model if needed

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
    username = factory.Sequence(lambda n: f'user{n}')

class ProjectFactory(DjangoModelFactory):
    class Meta:
        model = Project
    owner = factory.SubFactory(UserFactory)
    name = factory.Faker('company')
    description = factory.Faker('text')
    starting_date = factory.Faker('date')
    expected_ending_date = factory.Faker('date')
    statut = factory.Faker('random_element', elements=['en_cours', 'annulee', 'terminee'])

class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task
    owner = factory.SubFactory(UserFactory)
    name = factory.Faker('word')
    description = factory.Faker('sentence')
    starting_date = factory.Faker('date')
    expected_ending_date = factory.Faker('date')
    statut = factory.Faker('random_element', elements=['intouchee', 'en_cours', 'annulee', 'terminee'])
    project = factory.SubFactory(ProjectFactory)

class TeamMemberFactory(DjangoModelFactory):
    class Meta:
        model = TeamMember

    name = factory.Faker('name')
    position = factory.Faker('job')
    email = factory.Faker('email')
    role_in_project = factory.Faker('job')
    project = factory.SubFactory(ProjectFactory)

class TechnicalDocumentFactory(DjangoModelFactory):
    class Meta:
        model = TechnicalDocument

    title = factory.Faker('sentence')
    description = factory.Faker('text')
    link_to_file = factory.Faker('url')
    project = factory.SubFactory(ProjectFactory)
    task = factory.SubFactory(TaskFactory)

class MilestoneFactory(DjangoModelFactory):
    class Meta:
        model = Milestone

    name = factory.Faker('sentence')
    expected_date = factory.Faker('date')
    project = factory.SubFactory(ProjectFactory)
    achieved = factory.Faker('boolean')



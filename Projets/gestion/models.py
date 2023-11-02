from django.contrib.auth.models import User
from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    starting_date = models.DateField()
    expected_ending_date = models.DateField()
    STATUT_CHOICES = [
        ('en_cours', 'En Cours'),
        ('annulee', 'Annulée'),
        ('terminee', 'Terminée'),
    ]
    statut = models.CharField(max_length=15, choices=STATUT_CHOICES)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=None)  # Le propriétaire du projet
      # Le propriétaire du projet

class TeamMember(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,default=None,null=True,blank=True)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=100, default=None)
    email = models.EmailField()
    role_in_project = models.CharField(max_length=100,blank=True)  # Choices for team member roles
    project = models.ForeignKey(Project, on_delete=models.CASCADE,default=None)

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    starting_date = models.DateField()
    expected_ending_date = models.DateField()
    STATUT_CHOICES = [
        ('intouchee', 'Intouchée'),
        ('en_cours', 'En Cours'),
        ('annulee', 'Annulée'),
        ('terminee', 'Terminée'),
    ]
    statut = models.CharField(max_length=15, choices=STATUT_CHOICES)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    team_members = models.ManyToManyField(TeamMember, related_name='tasks')
    owner = models.ForeignKey(User, on_delete=models.CASCADE,default=None)

class TechnicalDocument(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link_to_file = models.URLField(max_length=200)  # Specify maximum length
    project = models.ForeignKey(Project, on_delete=models.CASCADE,default=None)
    task = models.ForeignKey(Task, on_delete=models.CASCADE,default=None)

class Milestone(models.Model):
    name = models.CharField(max_length=200)
    expected_date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    achieved = models.BooleanField(default=False)












    
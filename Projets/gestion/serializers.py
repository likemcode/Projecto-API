from rest_framework.serializers import ModelSerializer
from .models import Project,Task,TeamMember,TechnicalDocument,Milestone

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class ProjectSerializer(ModelSerializer):
    taches = TaskSerializer(many=True, read_only=True)
    class Meta:
        model=Project
        fields='__all__'
class TeamMemberSerializer(ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['name', 'position', 'email', 'role_in_project', 'project']

class TechnicalDocumentSerializer(ModelSerializer):
    class Meta:
        model = TechnicalDocument
        fields = '__all__'
    
class MilestoneSerializer(ModelSerializer):
    class Meta:
        model=Milestone
        fields='__all__'
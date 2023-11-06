from rest_framework import generics, viewsets,status
from .models import Project, Task, TeamMember, TechnicalDocument, Milestone
from .serializers import ProjectSerializer, TaskSerializer, TeamMemberSerializer, TechnicalDocumentSerializer, MilestoneSerializer
from .permissions import IsProjectManager, IsEngineer
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only project managers can create, update, and delete projects
            permission_classes = [IsAdminUser|IsProjectManager]
        else:
            # All authenticated users can view the list of projects
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

class ProjectTasksView(generics.ListAPIView):
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        project_id = self.kwargs['project_id']
        tasks = Task.objects.filter(project_id=project_id)
        return tasks

    def list(self, request, *args, **kwargs):
        project_id = self.kwargs['project_id']
        tasks = self.get_queryset()
        team_members = TeamMember.objects.filter(project_id=project_id)

        page = self.paginate_queryset(tasks)
        if page is not None:
            tasks = self.get_serializer(page, many=True).data
        else:
            tasks = self.get_serializer(tasks, many=True).data

        team_members = TeamMemberSerializer(team_members, many=True).data

        data = {
            'tasks': tasks,
            'team_members': team_members,
        }

        if page is not None:
            return self.get_paginated_response(data)

        return Response(data)


class ProjectMilestonesViewset(viewsets.ModelViewSet):
    serializer_class = MilestoneSerializer

    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Milestone.objects.filter(project_id=project_id)
    def get_permissions(self):
        
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only project managers can create, update, and delete projects
            permission_classes = [IsProjectManager|IsAdminUser]
        else:
            # All authenticated users can view the list of projects
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Milestone.objects.filter(project_id=project_id)
    
     
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return Task.objects.filter(project_id=project_id)

    def get_permissions(self):
        
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only project managers can create, update, and delete projects
            permission_classes = [IsProjectManager|IsAdminUser]

        elif self.action in ['update', 'partial_update']:
            permission_classes=[IsEngineer]
        else:
            # All authenticated users can view the list of tasks
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class TaskTechnicalDocumentListView(generics.ListCreateAPIView):
    serializer_class = TechnicalDocumentSerializer
    permission_classes=[IsEngineer|IsProjectManager|IsAdminUser]
    def get_queryset(self):
        task_id = self.kwargs['task_id']
        technical_documents = TechnicalDocument.objects.filter(task_id=task_id)
        return technical_documents


class TaskTechnicalDocumentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TechnicalDocumentSerializer
    lookup_field = 'id'
    permission_classes=[IsEngineer]
    
    def get_queryset(self):
        task_id = self.kwargs['task_id']
        technical_documents = TechnicalDocument.objects.filter(task_id=task_id)
        return technical_documents

    def destroy(self, request, *args, **kwargs):
        # Implement your custom delete logic here
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class TaskTeamMembersView(generics.ListCreateAPIView):
    serializer_class = TeamMemberSerializer
    permission_classes=[IsAuthenticated,IsProjectManager]

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        task = Task.objects.get(id=task_id)
        return task.team_members.all()

class TaskTeamMemberDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TeamMemberSerializer
    lookup_field = 'id'
    permission_classes=[IsEngineer|IsProjectManager|IsAdminUser]

    def get_queryset(self):
        task_id = self.kwargs['task_id']
        task = Task.objects.get(id=task_id)
        return task.team_members.all()

    def destroy(self, request, *args, **kwargs):
        # Implement your custom delete logic here
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TeamMemberViewSet(viewsets.ModelViewSet):
    serializer_class = TeamMemberSerializer
    def get_permissions(self):
        
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # Only project managers can create, update, and delete projects
            permission_classes = [IsProjectManager|IsEngineer]
        else:
            # All authenticated users can view the list of projects
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        project_id = self.kwargs.get('project_pk')
        return TeamMember.objects.filter(project_id=project_id)




from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

projects_router = DefaultRouter()
projects_router.register(r'tasks', TaskViewSet, basename='project-tasks')
projects_router.register(r'milestones',ProjectMilestonesViewset, basename='project-milestones')
projects_router.register(r'team-members', TeamMemberViewSet, basename='project-team-members')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/projects/<int:project_pk>/', include(projects_router.urls)),
    path('api/projects/<int:project_id>/tasks/<int:task_id>/team-members/', TaskTeamMembersView.as_view(), name='task_team_members_list'),
    path('api/projects/<int:project_id>/tasks/<int:task_id>/team-members/<int:id>/', TaskTeamMemberDetailView.as_view(), name='task_team_member_detail'),
    path('api/projects/<int:project_id>/tasks/<int:task_id>/technical-document/', TaskTechnicalDocumentListView.as_view(), name='task_technical_document_list'),
    path('api/projects/<int:project_id>/tasks/<int:task_id>/technical-document/<int:id>/', TaskTechnicalDocumentDetailView.as_view(), name='task_technical_document_detail'),
]   

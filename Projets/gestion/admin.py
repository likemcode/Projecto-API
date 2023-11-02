from django.contrib import admin
from .models import Project, TeamMember, Task, TechnicalDocument, Milestone

# Enregistrer chaque modèle dans l'interface d'administration
admin.site.register(Project)
admin.site.register(TeamMember)
admin.site.register(Task)
admin.site.register(TechnicalDocument)
admin.site.register(Milestone)






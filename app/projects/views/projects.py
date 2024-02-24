from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.shortcuts import get_object_or_404

from projects.models import Project


class ProjectsView(View):
    template_name = "projects.html"

    def get(self, request, *args, **kwargs):

        projects = Project.objects.all()
        return render(
            request, 
            self.template_name, 
            {"projects": projects}
        )


class ProjectView(View):
    template_name = "project.html"

    def get(self, request, *args, **kwargs):

        project_id = kwargs.get('id')
        project = get_object_or_404(Project, pk=project_id)

        return render(
            request, 
            self.template_name, 
            {"project": project}
        )
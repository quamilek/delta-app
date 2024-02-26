from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from projects.models import Project, ProjectElement



class ProjectsView(LoginRequiredMixin, View):
    template_name = "projects.html"

    def get(self, request, *args, **kwargs):

        projects = Project.objects.all()
        return render(
            request, 
            self.template_name, 
            {"projects": projects}
        )


class ProjectView(LoginRequiredMixin, View):
    template_name = "project.html"

    def get(self, request, *args, **kwargs):

        project_id = kwargs.get('id')
        project = get_object_or_404(Project, pk=project_id)
        project_elements = ProjectElement.objects.filter(project=project)

        paginator = Paginator(project_elements, 10) # 10 elements per page

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


        return render(
            request, 
            self.template_name, 
            {
                "project": project,
                "page_obj": page_obj,
            }
        )
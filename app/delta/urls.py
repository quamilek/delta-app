from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from projects.views.views import import_project
from projects.views.projects import ProjectView, ProjectsView

urlpatterns = [
    # path("/", ProjectsView.as_view(), name='projects'),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  

    path("projects/new", import_project, name="import_project"),
    path("projects/", ProjectsView.as_view(), name='projects'),
    path("projects/<int:id>", ProjectView.as_view(), name='project'),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from projects.views.views import import_project
from projects.views.projects import ProjectView, ProjectsView
from django.views.generic.base import RedirectView
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("/accounts/login")
    # Redirect to a s


urlpatterns = [
    # path("/", ProjectsView.as_view(), name='projects'),
    path(
        "",
        RedirectView.as_view(url="projects"),
        name="home-page",
    ),
    path("logout", logout_view),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),  

    path("projects/new", import_project, name="import_project"),
    path("projects/", ProjectsView.as_view(), name='projects'),
    path("projects/<int:id>", ProjectView.as_view(), name='project'),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



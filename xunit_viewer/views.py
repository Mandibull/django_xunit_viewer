from django.shortcuts import get_object_or_404, render

from .models import Project


def index(request):
    context = {
        'projects': Project.objects.all(),
    }
    return render(request, 'xunit_viewer/index.html', context)


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    context = {}
    return render(request, 'xunit_viewer/project.html', context)

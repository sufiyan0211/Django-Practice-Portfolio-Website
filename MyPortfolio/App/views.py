from django.shortcuts import render, get_object_or_404
from App.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context ={
        'projects':projects
    }
    return render(request, 'index.html', context)


def projectDetails(request, pk):
    project = get_object_or_404(Project, id=pk)
    projects = Project.objects.all()
    context = {
        'project' : project,
        'projects' : projects
    }
    return render(request, 'projectDetails.html', context)
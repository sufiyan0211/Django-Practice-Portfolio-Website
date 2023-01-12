from django.shortcuts import render
from App.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context ={
        'projects':projects
    }
    return render(request, 'index.html', context)
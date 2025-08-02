from django.shortcuts import render
from .models import SiteStatus, Project

def home(request):
    status = SiteStatus.objects.first()

    # If you want to show projects on home too, fetch from DB here
    # But if not, you can just pass empty list or omit
    return render(request, 'portfolio_app/home.html', {
        'open_to_work': status.open_to_work if status else True,
    })

def projects(request):
    projects = Project.objects.all()

    # Gather unique tech tags for filtering
    all_techs = set()
    for project in projects:
        all_techs.update(project.tech_tags())

    all_techs = sorted(all_techs)

    return render(request, 'portfolio_app/projects.html', {
        'projects': projects,
        'all_techs': all_techs,
    })

def cv(request):
    return render(request, 'cv.html')

def view_cv(request):
    return render(request, 'cv.html')

def home(request):
    status = SiteStatus.objects.first()
    projects = Project.objects.all()
    return render(request, 'portfolio_app/home.html', {
        'open_to_work': status.open_to_work if status else True,
        'projects': projects,
    })
from django.shortcuts import render
from django.conf import settings
from django.http.response import HttpResponse,Http404
import os
from .models import *

def media_path(request, path):
    full_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.isfile(full_path):
        with open(full_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='application/octet-stream')
    else:
        raise Http404("File not found")

def static_path(request, path):
    full_path = os.path.join(settings.STATICFILES_DIRS[0], path)
    if os.path.isfile(full_path):
        with open(full_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='application/octet-stream')
    else:
        raise Http404("File not found")


def IndexPage(request):
    DATA = {
        'developer':Developer.objects.last(),
        'work':AboutWork.objects.last(),
        'bio':Bio.objects.last(), 
        'platforms':Platform.objects.all()
    }
    return render(request,'index.html',DATA)

def WorksPage(request):
    DATA = {
        'developer':Developer.objects.last(),
        'works':Work.objects.all().order_by('-id'),
    }
    return render(request,'works.html',DATA)

def ProjectsPage(request):
    DATA = {
        'developer':Developer.objects.last(),
        'projects':Project.objects.all().order_by('-id'),
    }
    return render(request,'projects.html',DATA)

def UsesPage(request):
    DATA = {
        'developer':Developer.objects.last(),
        'uses':Use.objects.all().order_by('-id'),
    }
    return render(request,'uses.html',DATA)

def WallpapersPage(request):
    DATA = {
        'developer':Developer.objects.last(),
        'wallpapers':Wallpaper.objects.all().order_by('-id'),
    }
    return render(request,'wallpapers.html',DATA)

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Workapp
# Create your views here
def workapp(request):
    info = Workapp.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        'info': info ,
    }
    return HttpResponse(template.render(request, context))

def details(request, id):
    info = Workapp.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'info' : info,
    }
    return HttpResponse(template.randeer(context, request))
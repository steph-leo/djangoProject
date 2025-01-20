from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Workapp
# Create your views here
def workapp(request):
    app = Workapp.objects.all().values()
    template = loader.get_template("index.html")
    context = {
        'app': app,
    }
    return HttpResponse(template.render(request, context))

def details(request, id):
    det = Workapp.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        'det' : det,
    }
    return HttpResponse(template.randeer(context, request))

def info(request, id):
    data = Workapp.objects.get(id=id)
    template = loader.get_template("ifo.html")
    context = {
        "data" : data,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template =loader.get_template('main.html')
    return HttpResponse(template.render(request))

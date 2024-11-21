
from django.template import loader
from django.http import HttpResponse
def reg(request):
    template = loader.get_template('reg.html')
    return HttpResponse(template.render())
# Create your views here.
def log(request):
    template = loader.get_template('log.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def cont(request):
    template = loader.get_template('cont.html')
    return HttpResponse(template.render())

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
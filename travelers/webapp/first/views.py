from django.shortcuts import render
from .models import Mission
from django.views.generic import TemplateView
from django.http import HttpResponse


class TestView(TemplateView):
    test_template = 'text.html'


def home(request):
    return render(request, 'home.html',{'message':'I passed you in'})


def mission(request):
    return render(request, 'mission.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    missions = Mission.objects.all()
    return render(request, 'index.html', {'missions': missions})


def add(request):
    return render(request, 'result.html', {'result': int(request.POST['num1']) + int(request.POST['num2'])})


# Create your views here.

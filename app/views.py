from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView,ListView

# Create your views here.

class home(TemplateView):
    model=School
    template_name='app/home.html'
    context_object_name='schools'

class SchoolList(ListView):
    model=School
    context_object_name='schools'

from django.shortcuts import render
from app.models import *
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class home(TemplateView):
    model=School
    template_name='app/home.html'
    context_object_name='schools'

class SchoolList(ListView):
    model=School
    context_object_name='schools'


class SchoolDetail(DetailView):
    model=School
    context_object_name='school'


class SchoolCreate(CreateView):
    model=School
    fields='__all__'

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name='schoolobject'
    success_url=reverse_lazy('SchoolList')

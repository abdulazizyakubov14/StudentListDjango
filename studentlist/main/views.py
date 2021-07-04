
from django.db.models import fields
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from .models import *
from django.views.generic import (
    View,
    ListView,
    DeleteView,
)
from django.views.generic.edit import(
    CreateView,
    UpdateView,
    DeleteView,

)
# Create your views here.

# class CreateViewPage(CreateView):
#     models = Groups
#     template_name = 'groups.html'
#     success_url = '/'

class HomeView(View):
    def get(self,request):
        model = Groups.objects.all()
        students = Student.objects.all()
        all_student = len(students)
        group_id = len(model)
        context = {
            'model':model,
            'group_id':group_id,
            'all_student':all_student
        }
        return render(request,'index.html',context)

def group_page(request,group_slug):
    group = Groups.objects.get(slug=group_slug)
    classs = group.groups.all
    context = {
        'group':classs,
    }
    return render(request,'detail.html',context)


class CreatGroup(CreateView):
    model = Groups
    fields = '__all__'
    template_name = 'create.html'
    success_url = '/'

class CreatStudent(CreateView):
    model = Student
    fields = '__all__'
    template_name = 'create.html'
    success_url = '/'

class UpadateGroup(UpdateView):
    model = Groups
    fields = '__all__'
    success_url = '/'
    template_name = 'create.html'

class UpadateStudent(UpdateView):
    model = Student
    fields = '__all__'
    success_url = '/'
    template_name = 'create.html'
    
class DeletGroup(DeleteView):
    model = Groups
    success_url = '/'
    template_name = 'delete.html'

class DeletStudent(DeleteView):
    model = Student
    success_url = '/'
    template_name = 'delete.html'

def search(request):
    q = request.GET.get('search',None)
    model = Student.objects.filter(name__icontains=q)
    res = len(model)
    context = {
        'res':res,
        'model':model,
        
    }

    return render(request,'search.html',context)



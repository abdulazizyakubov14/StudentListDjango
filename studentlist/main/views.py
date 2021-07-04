from .forms import *
from django.shortcuts import render
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
        group_id = len(model)
        context = {
            'model':model,
            'group_id':group_id,
        }
        return render(request,'index.html',context)

def group_page(request,group_slug):
    group = Groups.objects.get(slug=group_slug)
    classs = group.groups.all
    context = {
        'group':classs,
        'model':model
    }
    return render(request,'detail.html',context)


class CreateGoup(View):
    def get(self,request):
        form = CreateForm(request.GET)

        context = {
            'form':form
        }
    def post(self,request):
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = CreateForm()


# class CreatGroup(CreateView):
#     model = Groups
#     fields = ['group_name','weekday','course_times','slug',]
#     template_name = 'create.html'
#     success_url = '/'

# class CreatStudent(CreateView):
#     model = Student
#     fields = '__all__'
#     template_name = 'create.html'
#     success_url = '/'


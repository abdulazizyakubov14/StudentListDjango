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
        student = Student.objects.all()
        res = len(student)
        context = {
            'model':model,
            'res':res,
        }

        return render(request,'index.html',context)

def group_page(request,group_slug):
    group = Groups.objects.get(slug=group_slug)
    classs = group.groups.all
    context = {
        'group':classs
    }
    return render(request,'detail.html',context)



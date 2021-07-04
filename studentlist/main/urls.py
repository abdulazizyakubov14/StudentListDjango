from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('<str:group_slug>',group_page,name='group_detail'),
    # path('group/', CreatGroup.as_view(), name='create_group'),
    # path('student/', CreatStudent.as_view(), name='student_create')
]

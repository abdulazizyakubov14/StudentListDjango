from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('search/',search, name="search"),
    path('',HomeView.as_view(),name='home'),
    path('<str:group_slug>',group_page,name='group_detail'),
    path('group/', CreatGroup.as_view(), name='create_group'),
    path('student/', CreatStudent.as_view(), name='student_create'),
    path('delete_group/<pk>/', DeletGroup.as_view(), name='delete_group'), 
    path('update_group/<pk>/', UpadateGroup.as_view(), name='upadet_group'),
    path('delete_student/<pk>/', DeletStudent.as_view(), name='delete_student'),
    path('update_student/<pk>/', UpadateStudent.as_view(), name='upadet_student'),
     

]

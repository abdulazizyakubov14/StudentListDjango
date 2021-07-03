from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Mentors)
admin.site.register(Weekday)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['name', 'id']
	list_display_links = ['name']
	prepopulated_fields = {'slug':('name',)}
@admin.register(Groups)
class GroupAdmin(admin.ModelAdmin):
	list_display = ['group_name', 'id']
	list_display_links = ['group_name']
	prepopulated_fields = {'slug':('group_name',)}
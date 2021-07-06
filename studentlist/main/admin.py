from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Student)
	
@admin.register(Groups)
class GroupAdmin(admin.ModelAdmin):
	list_display = ['group_name', 'id']
	list_display_links = ['group_name']
	prepopulated_fields = {'slug':('group_name',)}
admin.site.register(Mentors)
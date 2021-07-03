from django.db import models
from django.urls import reverse


# Create your models here.

class Mentors(models.Model):
    class_mentor = models.CharField('Guruh Mentori', max_length=50)

    def __str__(self):
        return self.class_mentor

class Weekday(models.Model):
    days = models.CharField('Hafta Kuni',max_length=50)
    def __str__(self):
        return self.days

class Groups(models.Model):
    group_name = models.CharField('Guruh nomi' ,max_length=100)
    group_year = models.DateField('Yaratilgan sanai', auto_now_add=True)
    slug = models.SlugField('*',max_length=100)
    def get_absolute_url(self):
        return reverse("main:group_detail", kwargs={"group_slug": self.slug})
    
    def __str__(self):
        return self.group_name

    def __str__(self):
        return self.group_name

class Student(models.Model):
    name = models.CharField('Ismi',max_length=100)
    surname = models.CharField('Familiysai',max_length=100)
    phone = models.CharField('Telfon raqami',max_length=20 ,blank=True)
    address = models.CharField('Yashash manzili',max_length=200,blank=True)
    pay = models.BooleanField('To\'lovi',default=False)
    slug = models.SlugField('*',max_length=100)
    groups = models.ForeignKey(Groups, related_name='groups',on_delete=models.PROTECT)
    Weekdays = models.ManyToManyField(Weekday,)
    class_mentors = models.ForeignKey(Mentors, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


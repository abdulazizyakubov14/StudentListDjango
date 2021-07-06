from django.db import models
from django.urls import reverse


# Create your models here.

class Mentors(models.Model):
    class_mentor = models.CharField('Guruh Mentori', max_length=50)

    def __str__(self):
        return self.class_mentor

class Groups(models.Model):
    COURSE_DAY = (
                    ('Dush-Chor-Juma','Dush-Chor-Juma'),
                    ('Sesh-Pay-Shan','Sesh-Pay-Shan'))
    COURSE_TIME = (
                ('09:00 dan 11:00 gacha','09:00 dan 11:00 gacha'),
                ('13:00 dan 15:00 gacha','13:00 dan 15:00 gacha'),
                ('15:00 dan 17:00 gacha','15:00 dan 17:00 gacha'),
                ('17:00 dan 18:00 gacha','17:00 dan 18:00 gacha'))
    group_name = models.CharField('Guruh nomi' ,max_length=100)
    group_year = models.DateField('Yaratilgan sanai', auto_now_add=True)
    weekday = models.CharField('Hafta kunlari',max_length=200,choices=COURSE_DAY)
    course_times = models.CharField('Dars vaqtlari',max_length=200,choices=COURSE_TIME)
    mentors = models.ForeignKey(Mentors,on_delete=models.CASCADE)
    slug = models.SlugField('*',max_length=100)
    def get_absolute_url(self):
        return reverse("main:group_detail", kwargs={"group_slug": self.slug})
    
    def __str__(self):
        return self.group_name

class Student(models.Model):
    name = models.CharField('Ismi',max_length=100)
    surname = models.CharField('Familiysai',max_length=100)
    phone = models.CharField('Telfon raqami',max_length=20 ,blank=True)
    address = models.CharField('Yashash manzili',max_length=200,blank=True)
    pay = models.BooleanField('To\'lovi',default=False)
    groups = models.ForeignKey(Groups, related_name='groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.name


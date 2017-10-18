from django.db import models
import datetime
# Create your models here.
class staff(models.Model):
    name=models.CharField(max_length=10,primary_key=True)
    researchInterest=models.TextField(null=True)
    bio=models.TextField(null=True)
    publications=models.TextField(null=True)
    courses=models.TextField(null=True)
    img=models.ImageField(upload_to='Simg',default='Simg/no-img.jpg')

    def __str__(self):
        return self.name

class Gstudent(models.Model):
    name=models.CharField(max_length=10,primary_key=True)
    researchInterest = models.TextField(null=True)
    bio = models.TextField(null=True)
    img = models.ImageField(upload_to='Simg',default='Simg/no-img.jpg')

    def __str__(self):
        return self.name


class Ustudent(models.Model):
    name=models.CharField(max_length=10,primary_key=True)
    researchInterest = models.TextField(null=True)
    bio = models.TextField(null=True)
    img = models.ImageField(upload_to='Simg',default='Simg/no-img.jpg')

    def __str__(self):
        return self.name


class indexContent(models.Model):
    name=models.CharField(max_length=100,primary_key=True,default='indexContent')
    text1=models.TextField(null=True)
    text2 = models.TextField(null=True)
    text3 = models.TextField(null=True)
    pics1=models.ImageField(upload_to='Aimg',default='Aimg/no-img.jpg')
    pics2 = models.ImageField(upload_to='Aimg',default='Aimg/no-img.jpg')
    pics3 = models.ImageField(upload_to='Aimg',default='Aimg/no-img.jpg')

    def __str__(self):
        return self.name


class blog(models.Model):
    title=models.CharField(max_length=100)
    category = models.CharField(max_length=50, blank=True)
    date_time = models.DateTimeField(auto_now_add=True,null=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class papers(models.Model):
    title=models.CharField(max_length=200,primary_key=True)
    category = models.CharField(max_length=50, blank=True)
    year=models.IntegerField(default=datetime.date.today().year)
    file=models.FileField(upload_to='file')
    date_time = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=['-date_time']


from django.db import models
import datetime
from django.utils import timezone


# Create your models here.
class staff(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    researchInterest = models.TextField(null=True)
    bio = models.TextField(null=True)
    publications = models.TextField(null=True)
    courses = models.TextField(null=True)
    img = models.ImageField(upload_to='Simg', default='Simg/no-img.jpg')

    def __str__(self):
        return self.name


class Gstudent(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    researchInterest = models.TextField(null=True)
    bio = models.TextField(null=True)
    img = models.ImageField(upload_to='Simg', default='Simg/no-img.jpg')

    def __str__(self):
        return self.name


class Ustudent(models.Model):
    name = models.CharField(max_length=10, primary_key=True)
    researchInterest = models.TextField(null=True)
    bio = models.TextField(null=True)
    img = models.ImageField(upload_to='Simg', default='Simg/no-img.jpg')

    def __str__(self):
        return self.name


class indexContent(models.Model):
    name = models.CharField(max_length=100, primary_key=True, default='indexContent')
    title1 = models.CharField(max_length=100, default='About')
    text1 = models.TextField(null=True)
    text2 = models.TextField(null=True)
    text3 = models.TextField(null=True)
    pics1 = models.ImageField(upload_to='Aimg', default='Aimg/no-img.jpg')
    pics2 = models.ImageField(upload_to='Aimg', default='Aimg/no-img.jpg')
    pics3 = models.ImageField(upload_to='Aimg', default='Aimg/no-img.jpg')

    def __str__(self):
        return self.name


class blog(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, null=False)
    date_time = models.DateTimeField(default=timezone.now, null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class papers(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, null=False)
    year = models.IntegerField(default=datetime.date.today().year)
    file = models.FileField(upload_to='PFile')
    date_time = models.DateTimeField(default=timezone.now, null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class patent(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, null=False)
    date_time = models.DateTimeField(default=timezone.now, null=False)
    content = models.TextField(null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class resource(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50, null=False)
    date_time = models.DateTimeField(default=timezone.now, null=False)
    file = models.FileField(upload_to='RFile')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class ask(models.Model):
    title = models.CharField(max_length=100)
    date_time = models.DateTimeField(default=timezone.now, null=False)
    content = models.TextField(null=False)
    Email = models.EmailField(null=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']


class event(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class about(models.Model):
    content = models.TextField(null=False)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['id']

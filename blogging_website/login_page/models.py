from django.db import models

# Create your models here.
class Destination(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
class Post1(models.Model):
    name1=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    description=models.TextField()
    count=models.IntegerField(default=0)
    spam=models.IntegerField(default=0)
class comment1(models.Model):
    name1=models.CharField(max_length=100)
    comment=models.TextField()
    num=models.IntegerField(default=0)
class ContactForm(models.Model):
    email=models.CharField(max_length=100,default=None)
    subject=models.CharField(max_length=100,default=None)
    body=models.TextField(default=None)






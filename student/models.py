from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    rollnumber=models.CharField(max_length=10)
    email=models.EmailField(max_length=50)
    year=models.IntegerField()


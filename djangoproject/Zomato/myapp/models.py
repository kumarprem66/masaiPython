from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=10)
    city = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


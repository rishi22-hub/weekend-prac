
from django.db import models
class college(models.Model):
    name=models.CharField(max_length=100,default="none",unique=True)
    def __str__(self):
        return self.name

class branch(models.Model):
    college=models.ForeignKey(college,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,default="None",unique=True)
    def __str__(self):
        return self.name

class Student(models.Model):
    name=models.CharField(max_length=100)
    jeerank=models.IntegerField()
    college=models.ForeignKey(college,on_delete=models.SET_NULL,null=True)
    branch=models.ForeignKey(branch,on_delete=models.SET_NULL,null=True)
    location = models.CharField(max_length=100,default="rewa")
    def __str__(self):
        return self.name
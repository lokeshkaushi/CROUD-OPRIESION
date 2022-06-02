from django.db import models
class Reg(models.Model):
    uname= models.CharField(max_length=100)
    password= models.CharField(max_length=100)
    emailid= models.CharField(max_length=100)
    mobileno= models.CharField(max_length=100)

class Registration(models.Model):
    email =models.CharField(max_length=100)
    password =models.CharField(max_length=100)
    mobileno =models.CharField(max_length=100)
    technology =models.CharField(max_length=100)
    candidatetype =models.CharField(max_length=100)
    higherquli =models.CharField(max_length=100)    
    
class Job(models.Model):
    jobtitle = models.CharField(max_length=100)
    jobdescription = models.CharField(max_length=500)

# Create your models here.

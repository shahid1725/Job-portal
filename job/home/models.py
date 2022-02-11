from django.utils import timezone

from django.db import models
from user.models import HireJob

# Create your models here.

class Job(models.Model):
    image = models.ImageField(upload_to="logoimages", null=True)
    title=models.CharField(max_length=120)
    company=models.CharField(max_length=120)
    location=models.CharField(max_length=120)
    experience=models.CharField(max_length=120)
    eligibility=models.CharField(max_length=120)
    notice_period=models.CharField(max_length=120)
    description=models.CharField(max_length=500)
    posted_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title



class Application(models.Model):
    job_name=models.ForeignKey(Job,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    phone=models.PositiveIntegerField(max_length=12)
    location=models.CharField(max_length=120)
    experience=models.PositiveIntegerField(max_length=5)
    qualification=models.CharField(max_length=120)
    skills=models.CharField(max_length=300)
    income=models.PositiveIntegerField(max_length=120)

class HireApplication(models.Model):
    job_name=models.ForeignKey(HireJob,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=120)
    last_name=models.CharField(max_length=120)
    email=models.EmailField(max_length=120)
    phone=models.PositiveIntegerField(max_length=12)
    location=models.CharField(max_length=120)
    experience=models.PositiveIntegerField(max_length=5)
    qualification=models.CharField(max_length=120)
    skills=models.CharField(max_length=300)
    income=models.PositiveIntegerField(max_length=120)


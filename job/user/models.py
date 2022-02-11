from django.db import models
from django.utils import timezone
# Create your models here.

class HireJob(models.Model):
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
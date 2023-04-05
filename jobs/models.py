from django.db import models
from users.models import User
# Create your models here.

class Job(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField(max_length=200)
    skills = models.TextField(max_length=50)
    price = models.IntegerField()
    posted = models.ForeignKey(User, on_delete=models.CASCADE)
    applied = models.ManyToManyField(User, related_name='jobs_applied', blank=True)
    
    def __str__(self):
        return self.posted.username

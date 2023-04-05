from django.db import models
# Create your models here.



class User(models.Model):
    pfp = models.ImageField()
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=254, default="abc@gmail.com", null="")
    about = models.TextField(max_length=500)
    skills = models.TextField(max_length=50)

    def __str__(self):
        return self.username

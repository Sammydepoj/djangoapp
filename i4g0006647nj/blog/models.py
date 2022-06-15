
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Post(models.Model):
    Title=models.CharField(max_length=200)
    text=models.TextField(max_length=1000)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    created_date=models.DateTimeField(default=datetime.now, blank=True)
    published_date=models.DateTimeField(default=datetime.now, blank=True)

    

    
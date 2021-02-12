from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CalcField(models.Model):
    age = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    created_by = models.ForeignKey(User, related_name='calc', on_delete=models.CASCADE)
    created_dt = models.DateField(auto_now_add=True)

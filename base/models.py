from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Question(models.Model):
    uid = models.UUIDField(primary_key=True,default = uuid.uuid4)
    puzzle = models.TextField(null=True)
    ans = models.TextField()
   

   

class Stat(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    eye = models.IntegerField(default=0)
    accuracy = models.FloatField(default=33.3)


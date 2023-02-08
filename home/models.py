from django.db import models

# Create your models here.
from django.db import models


class students(models.Model):
    stu_id=models.IntegerField()
    name=models.TextField()
    phone_no=models.IntegerField()
    age=models.IntegerField()
    summary=models.TextField(default="is a good student !!!")


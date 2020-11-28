from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=64)
    content = models.CharField(max_length=256)
    ischecked = models.BooleanField()

    def __str__(self):
        return self.title
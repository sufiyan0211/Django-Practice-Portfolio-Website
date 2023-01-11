from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

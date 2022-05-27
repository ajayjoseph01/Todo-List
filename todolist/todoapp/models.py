from django.db import models

# Create your models here.
class todolists(models.Model):
    Task=models.CharField(max_length=200)
    Description=models.CharField(max_length=200)
    status=models.CharField(max_length=200)

    def _str_(self):
        return self.Task
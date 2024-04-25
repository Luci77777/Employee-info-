from django.db import models

class peoples(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField(null=True,blank=True)

    def __str__(self) -> str:
        return self.name

# Create your models here.
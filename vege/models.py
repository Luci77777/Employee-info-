from django.db import models

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_id= models.IntegerField(primary_key=True,unique=True)
    hours_worked=models.IntegerField(null=True)
    overtime_hours=models.IntegerField(null=True)

# Create your models here.
    
    def __str__(self):
        return f"{self.employee_name}"

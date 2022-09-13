from django.db import models

# Create your models here.
class Teachers(models.Model):
    name = models.CharField(
        max_length=15
    )
    age = models.IntegerField(

    )
    
    """"""
    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(
        max_length=20,
    )
    roll_no = models.IntegerField(

    )
    
    def __str__(self):
        return self.name


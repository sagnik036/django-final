from django.db import models

# Create your models here.
class Student (models.Model):
    """ student class table """
    student_name = models.CharField(
        max_length=20
    )
    student_id = models.IntegerField(

    )

    """ function overriding """
    def __str__(self):
        return self.student_name
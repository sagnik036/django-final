from django.db import models

# Create your models here.
class School(models.Model):
    """ this is table attribute """
    school_name = models.CharField(
        max_length=20
    )
    school_id = models.IntegerField(

    )

    """ function overding (polymorphism) """
    def __str__(self):
        return self.school_name
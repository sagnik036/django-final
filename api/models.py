from api.schools.models import *
from api.student.models import *

class Car(models.Model):
    car_name = models.CharField(
        max_length=15
    )
    mobile = models.IntegerField(

    )

    def __str__(self):
        return self.car_name

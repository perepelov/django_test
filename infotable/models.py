from django.db import models

# Create your models here.
class Model(models.Model):
    name = models.CharField(max_length=20)
    max_tonnage = models.FloatField()
    
    def __str__(self):
        return self.name

class Truck(models.Model):
    onboard_number = models.CharField(max_length=10)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    curr_load = models.FloatField()
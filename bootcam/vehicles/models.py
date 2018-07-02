from django.db import models

# Create your models here.

class Vehicle(models.Model):
    register_plate = models.CharField(max_length=264, unique= True, primary_key = True)
    owner = models.CharField(max_length=264)

    def __str__(self):
        return self.register_plate
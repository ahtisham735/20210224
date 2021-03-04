from django.db import models

# Create your models here.

class Airports(models.Model):
    code=models.CharField(max_length=3)
    city=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.code}:{self.city}"
class Flight(models.Model):
    origin=models.ForeignKey(Airports,on_delete=models.CASCADE,related_name="departures")
    destination=models.ForeignKey(Airports,on_delete=models.CASCADE,related_name="arrivals")
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.id}:from {self.origin} to {self.destination} in {self.duration} minutes "

class Passengers(models.Model):
    name=models.CharField(max_length=30)
    flights=models.ManyToManyField(Flight,blank=True,related_name="passengers")
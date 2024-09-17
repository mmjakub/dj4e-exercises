from django.core.validators import MinValueValidator
from django.db import models

class Make(models.Model):
    name = models.CharField(max_length=80, unique=True)

class Auto(models.Model):
    nickname = models.CharField(max_length=80)
    make = models.ForeignKey(Make, on_delete=models.CASCADE)
    mileage = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    comments = models.CharField(max_length=300)

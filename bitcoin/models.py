from django.db import models
from django.db.models.expressions import F

class Hour(models.Model):
    Prices=models.DecimalField(max_digits=20,decimal_places=2)
    time=models.DateTimeField(auto_now=False)
    class Meta:
        ordering=["-time"]

class Day(models.Model):
    Prices=models.DecimalField(max_digits=20,decimal_places=2)
    time=models.DateTimeField(auto_now=False)
    class Meta:
        ordering=["-time"]

class Week(models.Model):
    Prices=models.DecimalField(max_digits=20,decimal_places=2)
    time=models.DateTimeField(auto_now=False)
    class Meta:
        ordering=["-time"]

class Month(models.Model):
    Prices=models.DecimalField(max_digits=20,decimal_places=2)
    time=models.DateTimeField(auto_now=False)
    class Meta:
        ordering=["-time"]


class Year(models.Model):
    Prices=models.DecimalField(max_digits=20,decimal_places=2)
    time=models.DateTimeField(auto_now=False)
    class Meta:
        ordering=["-time"]

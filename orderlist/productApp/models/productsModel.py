from django.db import models
from django.db.models import CASCADE


class Attributes(models.Model):
    name = models.CharField(max_length=55, blank=True, null=True, default='DEFAULT VALUE')

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=55, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=15, null=True, blank=True, default='DEFAULT VALUE')

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=55)
    alternateName = models.CharField(max_length=55)
    categories = models.ManyToManyField(Categories)
    attributes = models.ManyToManyField(Attributes)
    price = models.IntegerField(default=0)
    unit = models.ForeignKey(Unit, on_delete=CASCADE)

    def __str__(self):
        return self.name

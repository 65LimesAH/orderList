from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=25)
    user = models.ManyToManyField(User)
    orderList = models.ForeignKey('orderListApp.OrderList', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

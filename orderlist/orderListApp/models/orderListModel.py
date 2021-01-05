from django.db import models


class OrderList(models.Model):
    name = models.CharField(max_length=55)
    owner = models.ForeignKey('organizationsApp.Organization', on_delete=models.CASCADE)
    products = models.ForeignKey('productApp.Products', on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

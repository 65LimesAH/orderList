from django.contrib import admin

from .models.productsModel import (Products, Categories, Unit, Attributes)

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Unit)
admin.site.register(Attributes)

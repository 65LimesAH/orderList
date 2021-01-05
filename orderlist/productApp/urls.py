from django.urls import path, include
from django.conf.urls.static import static
from django.contrib import admin

from orderlist.productApp.views import ProductCreateView

urlpatterns = [
    path('create/', ProductCreateView.as_view(), name='create')
]

from django import forms

from orderlist.productApp.models.productsModel import Products


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import productsModel
from .forms import productForm


class ProductListView(ListView):
    model = productsModel


class ProductDetailView(DetailView):
    model = productsModel


class ProductCreateView(CreateView):
    form_class = productForm
    model = productsModel
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'view_type': 'create'})
        return context


class ProductUpdateView(UpdateView):
    form_class = productForm
    model = productsModel
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'update'
        })
        return context


class ProductDeleteView(DetailView):
    model = productsModel
    success_url = '/'

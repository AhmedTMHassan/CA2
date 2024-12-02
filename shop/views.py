from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product, Make


class ProductListView(ListView):
    model = Product
    context_object_name = 'prod_list'
    template_name = 'shop/prod_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['make_list'] = Make.objects.all()  
        return context

    def get_queryset(self):
        queryset = Product.objects.all() 
        make_name = self.kwargs.get('make_name')  
        
        if not make_name:
            make_name = self.request.GET.get('make') 
        
        if make_name and make_name != "All Makes":
            make = get_object_or_404(Make, name=make_name)
            queryset = queryset.filter(make=make) 

        return queryset

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/prod_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['make_list'] = Make.objects.all() 
        return context

    def get_queryset(self):
        queryset = Product.objects.all() 
        make_name = self.kwargs.get('make_name')  
        
        if not make_name:
            make_name = self.request.GET.get('make')
        
        if make_name and make_name != "All Makes":
            make = get_object_or_404(Make, name=make_name)
            queryset = queryset.filter(make=make) 

        return queryset


class MakeListView(ListView):
    model = Make
    context_object_name = 'make_list'
    template_name = 'shop/make_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['make_list'] = Make.objects.all() 
        return context

    def get_queryset(self):
        queryset = Product.objects.all() 
        make_name = self.kwargs.get('make_name')  
        
        if not make_name:
            make_name = self.request.GET.get('make')  
        
        if make_name and make_name != "All Makes":
            make = get_object_or_404(Make, name=make_name)
            queryset = queryset.filter(make=make) 

        return queryset


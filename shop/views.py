from django.views.generic import ListView, DetailView
from .models import Product, Make

# Product views
class ProductListView(ListView):
    model = Product
    context_object_name = 'prod_list'
    template_name = 'shop/prod_list.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'shop/prod_detail.html'

# Make views
class MakeListView(ListView):
    model = Make
    context_object_name = 'make_list'
    template_name = 'shop/make_list.html'


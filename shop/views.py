from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, Make, CarListing
from .forms import CarListingForm
from django.contrib.auth.decorators import login_required

@login_required 
def create_car_listing(request):
    if request.method == "POST":
        form = CarListingForm(request.POST, request.FILES)
        if form.is_valid():
            car_listing = form.save(commit=False)
            car_listing.user = request.user 
            car_listing.save()

            return redirect('shop:customer_list') 
    else:
        form = CarListingForm()

    return render(request, 'shop/create_car_listing.html', {'form': form})


class CarListView(ListView):
    model = CarListing 
    context_object_name = 'car_list' 
    template_name = 'shop/customer_car_listing.html'

    def get_queryset(self):
        queryset = CarListing.objects.filter(user=self.request.user).distinct()
        return queryset


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


class ContactUsView(TemplateView):
    template_name = 'contactus.html'

class AboutUsView(TemplateView):
    template_name = 'about.html'






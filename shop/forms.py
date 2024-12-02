from django import forms
from .models import CarListing

class CarListingForm(forms.ModelForm):
    class Meta:
        model = CarListing
        fields = ['make', 'name','mileage', 'price', 'stock', 'colour', 'year_made', 'description', 'image']




from django import forms
from .models import CarListing, Make

class CarFilterForm(forms.Form):
    make = forms.ModelChoiceField(queryset=Make.objects.all(), required=False)
    name = forms.CharField(max_length=255, required=False)
    mileage = forms.CharField(max_length=255, required=False)
    price_min = forms.IntegerField(required=False)
    price_max = forms.IntegerField(required=False)
    stock = forms.IntegerField(required=False)
    year_made = forms.IntegerField(required=False)
    colour = forms.CharField(max_length=255, required=False)

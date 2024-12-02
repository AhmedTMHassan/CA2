import uuid
from django.db import models
from django.urls import reverse
from django.conf import settings





class Make(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='make', blank=True)



    def __str__(self):
        return self.name

class CarListing(models.Model):
    make = models.ManyToManyField(Make)
    name = models.CharField(max_length=255)
    mileage = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    year_made = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='car_images', blank=True)
    colour = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="car_listings") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.make)

class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True)
    make = models.ManyToManyField(Make)
    name = models.CharField(max_length=255)
    mileage = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    stock = models.IntegerField()
    year_made = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='product_images', blank=True)
    colour = models.CharField(max_length=255)



    def get_absolute_url(self):
        return reverse('shop:prod_detail', args=[self.id])

    def __str__(self):
        return str(self.make)









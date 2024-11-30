import uuid
from django.db import models
from django.urls import reverse

class Make(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=250, unique=True)
    image = models.ImageField(upload_to='make', blank=True)

    def __str__(self):
        return self.name




class Product(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True)
    make = models.ManyToManyField(Make)
    name = models.CharField(max_length=255)
    mileage = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    stock = models.IntegerField(null=True, blank=True)
    year_made = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images', blank=True)

    def get_absolute_url(self):
        return reverse('shop:prod_detail', args=[self.id])

    def __str__(self):
        return str(self.make)

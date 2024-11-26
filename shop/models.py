
from django.db import models
import uuid
from django.urls import reverse

class Make(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=True)
    name = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank = True)
    image = models.ImageField(upload_to = 'makes', blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'makes'
        verbose_name_plural = 'make'

    def get_absolute_url(self):
        return reverse('shop:products_by_make', args=[self.id])

    def __str__(self):
        return self.name


class Product(models.Model):
    make = models.TextField(null=True, blank=True)
    mileage = models.CharField(max_length=255)
    price = models.CharField(max_length=20)
    year_made = models.IntegerField(null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images', blank=True)


    def __str__(self):
        return self.make if self.make else ""

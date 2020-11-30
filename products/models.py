from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_absolute_url(self):
        return reverse('products_by_category', kwargs={'category_slug': self.slug})

class Colour(models.Model):
    colour = models.CharField(max_length=254)
    hex_value = models.CharField(max_length=7)

    def __str__(self):
        return self.colour

    def get_hex_value(self):
        return self.hex_value

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand_name = models.CharField(max_length=254)
    product_name = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    description = models.TextField()
    colours = models.ManyToManyField(Colour)

    def __str__(self):
        return self.product_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.product_name)
        super(Product, self).save(*args, **kwargs)



    
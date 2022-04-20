""" Models for Products, Categories, and Reviews """
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    """ Class for product category """
    class Meta:
        """ Class for product category plural name of table """
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        """ Return name as string """
        return f'{self.friendly_name}'

    def get_friendly_name(self):
        """ Return friendly name """
        return f'{self.friendly_name}'


class Product(models.Model):
    """ Class for products """
    category = models.ForeignKey('Category',
                                 null=True,
                                 blank=True,
                                 on_delete=models.SET_NULL
                                 )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6,
                                 decimal_places=2,
                                 null=True,
                                 blank=True
                                 )
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        """ Return name as string """
        return f'{self.name}'

    def __unicode__(self):
        return f'{self.name}'


class Review(models.Model):
    """ Class for reviews """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)

    def __str__(self):
        return self.review

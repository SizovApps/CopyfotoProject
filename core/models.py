from django.db import models
from django.shortcuts import reverse
from PIL import Image


class Prod(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    price = models.PositiveIntegerField()
    slug = models.SlugField(max_length=150, db_index=True)
    author = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('product_update_url', kwargs={'slug': self.slug})


class Service(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    fill10 = models.CharField(max_length=150, db_index=True, default='', blank=True)
    fill50 = models.CharField(max_length=150, db_index=True, default='', blank=True)
    fill100 = models.CharField(max_length=150, db_index=True, default='', blank=True)
    quantity = models.CharField(max_length=150, db_index=True, default='')
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='products_pics')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('service_detail_url', kwargs={'slug': self.slug})

    def get_update_url(self):
        return reverse('service_update_url', kwargs={'slug': self.slug})


class Work(models.Model):
    name = models.CharField(max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, db_index=True)
    price = models.PositiveIntegerField()
    timeOfWork = models.CharField(max_length=150)
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('portfolio_detail_url', kwargs={'slug': self.slug})


class Price(models.Model):
    fill10 = models.CharField(max_length=150, db_index=True, default='')
    fill50 = models.CharField(max_length=150, db_index=True, default='')
    fill100 = models.CharField(max_length=150, db_index=True, default='')


class CartItem(models.Model):
    product = models.ForeignKey(Prod, on_delete=models.CASCADE)
    qual = models.PositiveIntegerField(default=1)
    item_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return "Cart item for product {0}".format(self.product.name)


class Cart(models.Model):
    items = models.ManyToManyField(CartItem, blank=True)
    cart_total = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)

    def __str__(self):
        return str(self.id)








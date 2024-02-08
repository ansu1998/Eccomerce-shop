from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, unique=True, default=1)
    slug = models.SlugField(max_length=250, unique=True, default=1)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'categoryin'
        verbose_name_plural = 'hiii'


    def __str__(self):
        return '{}'.format(self.name)
    
class Product(models.Model):
    name = models.CharField(max_length=250, unique=True, default=1)
    slug = models.SlugField(max_length=250, unique=True, default=1)
    descriptions = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=1)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='products', blank=True)
    stock = models.IntegerField()
    avaliable = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return '{}'.format(self.name)
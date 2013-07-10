import moneyed
import datetime
from django.db import models
from djmoney.models.fields import MoneyField

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    parent = models.ForeignKey('self',blank=True, null=True) 
    def __unicode__(self):
        return self.name
        
class Product(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True, help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    size = models.CharField(max_length=3, null=True)
    #quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length=200, help_text='Comma-delimited set of SEO keywords for meta tag')
    category = models.ManyToManyField(Category)
   
    
    
    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return ('product_product', (), { 'product_slug': self.slug })
        
class Discount(models.Model):
    

    product = models.ForeignKey(Product)
    quantity_start = models.IntegerField(help_text='enter the start of the range')
    quantity_end = models.IntegerField(help_text='enter the end of the range')
    discount = models.DecimalField(max_digits=14, decimal_places=2, help_text='discount amount in dollars')
    #date_added = models.DateTimeField(default=datetime.now)   
        
        

    #description = models.TextField()
    #is_active = models.BooleanField(default=True)
    #meta_keywords = models.CharField("Meta Keywords",max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    #meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
            
        
        


from django.db import models
from datetime import datetime
from apps.account.models import User
from apps.common.models import Base
from apps.payment.models import Payment
#coding: utf-8


class Customer(models.Model):
    user = models.OneToOneField(User ,blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)
 
class Country(models.Model):
    name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    iso_2 = models.CharField(max_length=2, blank=True) # not unique as there are duplicates (IT)
    iso_3 = models.CharField(max_length=3, blank=True)

    class Meta:
        verbose_name_plural = 'Countries'
        ordering = ('name',)

    def __unicode__(self):
        return self.name
  
class Address(models.Model):
    street_line1 = models.CharField(max_length=100, blank=True, null=True)
    street_line2 = models.CharField(max_length=100, blank=True, null=True)
    zipcode = models.CharField( max_length=12, blank=True, null=True)
    city = models.CharField( max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.ForeignKey(Country, blank=False, null=False)
    landmark = models.CharField( max_length=80, blank=True, null=True)
    guiding_directions = models.CharField(max_length=200, blank=True, null=True)
    computed_address = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    latitude = models.DecimalField(max_digits=8, decimal_places=5, blank=True, null=True)
    geocode_error = models.BooleanField(default=False, blank=False, null=False)
    customer = models.ForeignKey(Customer)
    def __unicode__(self):
        return ', '.join(filter(None, [self.city, self.state, self.zipcode, unicode(self.country)]))

    def full(self, delimiter=','):
        return delimiter.join(filter(None, [self.street_line1, self.street_line2, self.city, self.state, self.zipcode, unicode(self.country)]))

    @property
    def full_br(self):
        return self.full('<br>')

    class Meta:
        verbose_name_plural = 'Addresses'
        ordering = ('pk',)
        
class Category(Base):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True, help_text='Unique value for product page URL, created from name.')
    #description = models.TextField()
    #is_active = models.BooleanField(default=True)
    #meta_keywords = models.CharField("Meta Keywords",max_length=255, help_text='Comma-delimited set of SEO keywords for meta tag')
    #meta_description = models.CharField("Meta Description", max_length=255, help_text='Content for description meta tag')
    
    
class Product(models.Model):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=80, unique=True, help_text='Unique value for product page URL, created from name.')
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    size = models.CharField(max_length=3, null=True)
    #quantity = models.IntegerField()
    description = models.TextField()
    meta_keywords = models.CharField(max_length=200, help_text='Comma-delimited set of SEO keywords for meta tag')
    categories = models.ManyToManyField(Category)
    customers = models.ForeignKey(Customer)
    
    
    def __unicode__(self):
        return self.name
    @models.permalink
    def get_absolute_url(self):
        return ('product_product', (), { 'product_slug': self.slug })
    
  # def sale_price(self):
   #     if self.old_price > self.price:
    #        return self.price
    #    else:
     #       return None
 
class Order(models.Model):
    delivered = models.BooleanField(False)
    payment = models.OneToOneField(Payment, primary_key=True)
    customer = models.ForeignKey(Customer)
        

from django.db import models
from apps.product.models import Product

class SEO(models.Model):
    heading = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    slug = models.SlugField(max_length = 200)
    
class Collection(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length = 50, unique=True, blank=False)
    description = models.CharField(max_length=200)
    seo = models.ForeignKey(SEO)
    


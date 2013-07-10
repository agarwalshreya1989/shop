from django.db import models
from apps.customer.models import Customer
from apps.shipping.models import Shipping
from djmoney.models.fields import MoneyField
from apps.product.models import Product

class Order(models.Model):
    shipping = models.ForeignKey(Shipping)
    customer = models.ForeignKey(Customer)
    product = models.ForeignKey(Product)
    shipping_cost = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    quantity = models.IntegerField()
    price = MoneyField(max_digits=10, decimal_places=2, default_currency='USD')
    

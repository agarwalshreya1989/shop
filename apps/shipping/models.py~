import datetime
from django.db import models
from apps.common.models import Address

STATUS_CHOICES = (
    (1, ('Delivered')),
    (2, ('Not Delivered')),
    (4, ('Delivered Damaged')),
    (8, ('Delivered Delayed')),
    (128, ('Under Processing')),
)
 
class Shipping(Address):
    status = models.IntegerField(max_length=1,choices=STATUS_CHOICES)
    tracking_url =  models.URLField(max_length=200)
    delivery_date = models.DateTimeField(blank=True, null=True, auto_now_add=True, editable=True)
    expected_date_arrival = models.DateTimeField(editable=True)
    
    

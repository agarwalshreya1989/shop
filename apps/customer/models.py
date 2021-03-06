from django.db import models
from apps.account.models import User
#from django.contrib.localflavor.in_.models import INPhoneNumberField
#from django.contrib.localflavor.us.models import PhoneNumberField

from apps.common.models import Address


class Customer(Address):
    user = models.OneToOneField(User ,blank=True, null=True)
    phone_number = models.CharField(blank=True, max_length=30)
    name = models.CharField(max_length=100, null=False, blank=False)

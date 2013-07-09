from django.db import models

class Payment(models.Model):
    payment_is_credit_card = models.BooleanField(default=False)
    payment_is_debit_card = models.BooleanField(default=False)
    payment_is_net_banking = models.BooleanField(default=False)
    payment_is_paypal = models.BooleanField(default=False)

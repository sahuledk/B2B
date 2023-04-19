from django.db import models
from orders.models import Currencies


# Create your models here.
class Balance_amount(models.Model):
    balance_amount = models.IntegerField()
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)

    def __init__(self):
        return self.balance_amount

class Account(models.Model):
    account = models.CharField(max_length=1000)
    balance_amount = models.ForeignKey(Balance_amount, on_delete=models.CASCADE)
    custom_sms_message = models.TextField
    pdf_type = models.CharField(max_length=1000)
    order_validity_month = models.IntegerField()

    def __str__(self):
        return self.account

from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.utils import timezone


class PaymentHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_payment_paytm', on_delete=models.CASCADE, null=True, default=None)
    MID = models.CharField(max_length=20)
    TXNID = models.CharField('TXN ID', max_length=64)
    ORDERID = models.CharField('ORDER ID', max_length=30)
    BANKTXNID = models.CharField('BANK TXN ID', max_length=64, null=True, blank=True)
    TXNAMOUNT = models.FloatField('TXN AMOUNT')
    CURRENCY = models.CharField('CURRENCY', max_length=4, null=True, blank=True)
    STATUS = models.CharField('STATUS', max_length=12)
    RESPCODE = models.IntegerField('RESP CODE')
    RESPMSG = models.TextField('RESP MSG', max_length=250)
    TXNDATE = models.DateTimeField('TXN DATE', default=timezone.now)
    GATEWAYNAME = models.CharField("GATEWAY NAME", max_length=20, null=True, blank=True)
    BANKNAME = models.CharField('BANK NAME', max_length=75, null=True, blank=True)
    PAYMENTMODE = models.CharField('PAYMENT MODE', max_length=10, null=True, blank=True)

    def __str__(self):
        return 'Paytm TXN'
    
    class Meta:
        app_label = 'paytm_gateway'
        unique_together = (("ORDERID", "TXNID"),)

    def __unicode__(self):
        return self.STATUS

class OrderHistory(models.Model):
    user = models.ForeignKey(User, related_name='rel_order_paytm', on_delete=models.CASCADE, null=True, default=None)
    ORDERID = models.CharField('ORDER ID', max_length=30)
    TXNAMOUNT = models.FloatField('TXN AMOUNT')
    ORDERDATE = models.DateTimeField('ORDER DATE', default=timezone.now)

    def __str__(self):
        return self.user.email


    
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    res_add = models.CharField(max_length=75, null=True, blank=True)
    res_city = models.CharField(max_length=30, null=True, blank=True)
    res_state = models.CharField(max_length=30, null=True, blank=True)
    phone_no = models.CharField(max_length=12, unique=True, null=True, blank=True)

    def __str__(self):
        return '{} Profile'.format(self.user.email)

class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)

    def __str__(self):
        return '{0}\'s Wallet'.format(self.user.username)

class TransferHistory(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_transfer_from', on_delete=models.CASCADE, null=True, default=None)
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='rel_transfer_to', on_delete=models.CASCADE, null=True, default=None)
    amount = models.FloatField(default=0)
    time = models.DateTimeField(default=timezone.now)

    # def __str__(self):
    #     return ''
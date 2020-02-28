from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone

from .models import Profile
from .models import Wallet
from paytm_gateway.models import PaymentHistory

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # Create a client profile for every user
    if created:
        Profile.objects.create(user=instance)
        Wallet.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
    instance.wallet.save()


@receiver(post_save, sender=PaymentHistory)
def create_money_add_request(sender, instance, created, **kwargs):
    if created:
        if instance.STATUS=='TXN_SUCCESS':
            wallet = Wallet.objects.get(user=instance.user)
            wallet.balance = wallet.balance + instance.TXNAMOUNT
            wallet.save()
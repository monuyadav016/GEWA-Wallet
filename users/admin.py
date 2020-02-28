from django.contrib import admin
from .models import Profile, Wallet, TransferHistory

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'dob', 'phone_no']

class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'balance']

class TransferHistoryAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'amount', 'time']

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(TransferHistory, TransferHistoryAdmin)

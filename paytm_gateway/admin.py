from django.contrib import admin
from .models import PaymentHistory, OrderHistory
# Register your models here.
class PaymentHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'TXNAMOUNT', 'STATUS', 'TXNDATE')

class OrderHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'ORDERID', 'TXNAMOUNT', 'ORDERDATE')


admin.site.register(PaymentHistory, PaymentHistoryAdmin)
admin.site.register(OrderHistory, OrderHistoryAdmin)
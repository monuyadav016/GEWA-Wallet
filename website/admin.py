from django.contrib import admin
from .models import ContactPage

class ContactPageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']

admin.site.register(ContactPage, ContactPageAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'id', 'first_name', 'last_name']
    fields = ('first_name', 'last_name', 'username', 'email', 'password',
        'is_active', 'is_staff', 'is_superuser', 'user_permissions',
        'last_login', 'date_joined')

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)

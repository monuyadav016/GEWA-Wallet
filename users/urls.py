from django.urls import path
from . import views as users_views

urlpatterns = [
    path('edit_profile/', users_views.edit_profile, name='edit-user-profile'),
    path('profile/', users_views.profile, name='user-profile'),
    path('add_money/', users_views.add_money, name='add-money'),
    path('send_money/', users_views.transfer_money, name='transfer-money'),
    path('transfers/', users_views.transfer_history, name='user-transfers'),
    path('payments/', users_views.add_to_wallet_history, name='user-payments'),
]
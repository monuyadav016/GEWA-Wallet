from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('payment/<str:amount>/', views.payment, name='payment'),
    # REPLACE USERNAME WITH PRIMARY KEY OF YOUR USER MODEL
    path('paytm/response/<str:user_username>/', views.response, name='response'),
]
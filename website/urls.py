from django.urls import path
from django.conf.urls import handler404, handler500
from . import views

urlpatterns = [
    path('', views.home, name='website-home'),
    path('about/', views.about, name='website-about'),
    path('contact/', views.contact, name='website-contact')
]


handler404 = 'website.views.handler404'
handler500 = 'website.views.handler500'
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as auth_system_views

urlpatterns = [
    path('signup/', auth_system_views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='auth_system/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='auth_system/logout.html'), name="logout"),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='auth_system/password_reset.html'), name="password_reset"),
    path('password-reset-done', auth_views.PasswordResetDoneView.as_view(
        template_name='auth_system/password_reset_done.html'), name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth_system/password_reset_confirm.html'), name="password_reset_confirm"),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth_system/password_reset_complete.html'), name="password_reset_complete"),
]
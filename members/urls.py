from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

from .views import LoginAjaxView, RegisterAjaxView

urlpatterns = [
    path('login_user/', views.login_user, name='login_user'),
    path('logout_user/', views.logout_user, name='logout'),
    path('register_user/', views.register_user, name='register_user'),
    path('reset_password', views.PasswordResetView2.as_view(template_name="members/password_reset.html"), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="members/password_reset_send.html"), name='password_reset_done'),
    path('reset/<uid64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="members/password_reset_form.html"), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('login_ajax/', LoginAjaxView.as_view(), name='login_ajax'),
    path('register_ajax', RegisterAjaxView.as_view(), name='register_ajax')
    ]

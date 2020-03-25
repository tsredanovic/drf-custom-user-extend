from allauth.account.views import email_verification_sent
from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from users.api.views import *

router = routers.DefaultRouter()
urlpatterns = [
    # Login, Logout
    url(r'^login/$', CustomLoginView.as_view(), name='rest_login'),
    url(r'^logout/$', CustomLogoutView.as_view(), name='rest_logout'),

    # Password
    url(r'^password/change/$', CustomPasswordChangeView.as_view(), name='rest_password_change'),
    url(r'^password/reset/$', CustomPasswordResetView.as_view(), name='rest_password_reset'),
    url(r'^password/reset/confirm/$', CustomPasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),

    # Registration
    url(r'^registration/$', CustomRegisterView.as_view(), name='rest_register'),
    url(r'^registration/verify-email/$', CustomVerifyEmailView.as_view(), name='rest_verify_email'),

    # User
    url(r'^user/$', CustomUserDetailsView.as_view(), name='rest_user_details'),

    # Email
    path("confirm-email/", email_verification_sent, name="account_email_verification_sent"),  # Needed for registration email
]

from allauth.account.views import confirm_email
from django.conf.urls import url
from django.urls import include
from rest_auth.views import PasswordResetConfirmView, PasswordResetView
from rest_framework import routers

from users.api.views import CustomLoginView, CustomLogoutView, CustomPasswordChangeView, CustomRegisterView, \
    CustomVerifyEmailView, CustomUserDetailsView

router = routers.DefaultRouter()
urlpatterns = [
    # Rest auth urls
    url(r'^password/reset/$', PasswordResetView.as_view(), name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    url(r'^login/$', CustomLoginView.as_view(), name='rest_login'),
    url(r'^logout/$', CustomLogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', CustomUserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', CustomPasswordChangeView.as_view(), name='rest_password_change'),

    url(r'^registration/$', CustomRegisterView.as_view(), name='rest_register'),
    url(r'^registration/verify-email/$', CustomVerifyEmailView.as_view(), name='rest_verify_email'),

    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
        name='account_confirm_email'),
]

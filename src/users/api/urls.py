from allauth.account.views import confirm_email
from django.conf.urls import url
from django.urls import include
from rest_auth.views import PasswordResetView, PasswordResetConfirmView, UserDetailsView, PasswordChangeView
from rest_framework import routers

from users.views import CustomLoginView, CustomLogoutView

router = routers.DefaultRouter()
urlpatterns = [
    # Rest auth urls
    url(r'^password/reset/$', PasswordResetView.as_view(),
        name='rest_password_reset'),
    url(r'^password/reset/confirm/$', PasswordResetConfirmView.as_view(),
        name='rest_password_reset_confirm'),
    url(r'^login/$', CustomLoginView.as_view(), name='rest_login'),
    url(r'^logout/$', CustomLogoutView.as_view(), name='rest_logout'),
    url(r'^user/$', UserDetailsView.as_view(), name='rest_user_details'),
    url(r'^password/change/$', PasswordChangeView.as_view(), name='rest_password_change'),

    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^accounts-rest/registration/account-confirm-email/(?P<key>.+)/$', confirm_email,
        name='account_confirm_email'),
]

from allauth.account.adapter import DefaultAccountAdapter
from allauth.utils import build_absolute_uri
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse


class CustomAccountAdapter(DefaultAccountAdapter):
    def send_confirmation_mail(self, request, emailconfirmation, signup):
        current_site = get_current_site(request)
        verify_email_endpoint = build_absolute_uri(request, reverse('rest_verify_email'))
        ctx = {
            "verify_email_endpoint": verify_email_endpoint,
            "current_site": current_site,
            "key": emailconfirmation.key,
        }
        if signup:
            email_template = 'account/email/email_confirmation_signup'
        else:
            email_template = 'account/email/email_confirmation'
        self.send_mail(email_template, emailconfirmation.email_address.email, ctx)
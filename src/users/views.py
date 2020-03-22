from django.contrib.auth import logout as django_logout
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import ugettext_lazy as _
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_auth.serializers import TokenSerializer
from rest_auth.views import LoginView, PasswordChangeView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class CustomLoginView(LoginView):
    @swagger_auto_schema(
        operation_id='login',
        operation_description=
        """
        Check the credentials and return the REST Token
        if the credentials are valid and authenticated.

        Calls Django Auth login method to register User ID
        in Django session framework.

        Accept the following POST parameters: email, password
        Return the REST Framework Token Object's key.
        """,
        operation_summary=
        """
        Check the credentials and return the REST Token
        if the credentials are valid and authenticated.
        """,
        responses={
            200:
                openapi.Response('REST Framework Token Object\'s key.', TokenSerializer)
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class CustomLogoutView(APIView):
    """
    Calls Django logout method and deletes the Token object
    assigned to the current User object.

    Accepts/Returns nothing.
    """
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        operation_id='logout',
        operation_description=
        """
        Calls Django logout method and deletes the Token object
        assigned to the current User object.

        Accepts/Returns nothing.
        """,
        operation_summary=
        """
        Calls Django logout method and deletes the Token object
        assigned to the current User object.
        """,
        responses={
            200:
                openapi.Response('Nothing.')
        }
    )
    def post(self, request, *args, **kwargs):
        return self.logout(request)

    def logout(self, request):
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        if getattr(settings, 'REST_SESSION_LOGIN', True):
            django_logout(request)

        response = Response({"detail": _("Successfully logged out.")}, status=status.HTTP_200_OK)

        return response


class CustomPasswordChangeView(PasswordChangeView):
    @swagger_auto_schema(
        operation_id='password_change',
        operation_description=
        """
        Calls Django Auth SetPasswordForm save method.

        Accepts the following POST parameters: old_password, new_password1, new_password2
        Returns nothing.
        """,
        operation_summary=
        """
        Calls Django Auth SetPasswordForm save method.
        """,
        responses={
            200:
                openapi.Response('Nothing.')
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

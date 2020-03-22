from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_auth.serializers import TokenSerializer
from rest_auth.views import LoginView


class CustomLoginView(LoginView):
    """
    Check the credentials and return the REST Token
    if the credentials are valid and authenticated.
    Calls Django Auth login method to register User ID
    in Django session framework.

    Accept the following POST parameters: username, password
    Return the REST Framework Token Object's key.
    """

    @swagger_auto_schema(
        responses={
            200:
                openapi.Response('REST Framework Token Object\'s key.', TokenSerializer)
        }
    )
    def post(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

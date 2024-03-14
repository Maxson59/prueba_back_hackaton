from rest_framework import (
    generics,
    permissions,
)
from user.serializers import UserSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['User'])
class CreateUserView(generics.CreateAPIView):
    """ View to create a new user in the system. """

    serializer_class = UserSerializer


@extend_schema(tags=['Me'])
class UserMeView(generics.RetrieveUpdateAPIView):
    """ View for authenticated user. """

    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """ Retrive and return the authenticated user. """
        return self.request.user

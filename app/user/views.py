from rest_framework import generics
from user.serializers import CreateUserSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(tags=['User'])
class CreateUserView(generics.CreateAPIView):
    """ View to create a new user in the system. """

    serializer_class = CreateUserSerializer

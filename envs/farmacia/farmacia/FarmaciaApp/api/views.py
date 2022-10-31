from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.hashers import make_password

from FarmaciaApp.models import User
from FarmaciaApp.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    permission_class = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all() 
    #Encriptar la contraseña que se guarda en la BD
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)
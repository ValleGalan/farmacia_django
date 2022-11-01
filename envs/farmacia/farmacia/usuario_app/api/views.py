from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.hashers import make_password

from usuario_app.models import User
from usuario_app.api.serializers import UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

#ADMIN PARA EL ADMINISTRADOR
class UserApiViewSet(ModelViewSet):
    permission_class = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all() 
    #Encriptar la contraseña que se guarda en la BD
    def create(self, request, *args, **kwargs):
        request.data['password'] = make_password(request.data['password'])
        return super().create(request, *args, **kwargs)

    #Actualizar el encriptado de contraseña
    def partial_update(self, request, *args, **kwargs):
        password = request.data['password']
        if password:
            request.data['password'] = make_password(password)
        else:
            request.data['password'] = request.user.password
        return super().update(request, *args, **kwargs)

#Devuelve los datos del usuario que esta logueado, EMPLEADOS
class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser


from FarmaciaApp.models import User
from FarmaciaApp.api.serializers import UserSerializer


class UserApiViewSet(ModelViewSet):
    permission_class = [IsAdminUser]
    serializer_class = UserSerializer
    queryset = User.objects.all() 
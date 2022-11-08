from rest_framework.viewsets import ModelViewSet
#si estas logueado podes hacer todo sino leer
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from django_filters.rest_framework import DjangoFilterBackend

from farmacia_app.models import Farmacia
from farmacia_app.api.serializers import FarmaciaSerializer

class FarmaciaApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = FarmaciaSerializer

    queryset = Farmacia.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre'] #filtrar despues por turno o ubicacion!!!
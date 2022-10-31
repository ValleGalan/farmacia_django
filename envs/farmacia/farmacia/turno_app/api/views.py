from rest_framework.viewsets import ModelViewSet
#si estas logueado podes hacer todo sino leer
from rest_framework.permissions import IsAuthenticatedOrReadOnly 
from django_filters.rest_framework import DjangoFilterBackend

from turno_app.models import Turno
from turno_app.api.serializers import TurnoSerializer

class TurnoApiViewSet(ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = TurnoSerializer

    queryset = Turno.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['localizacion'] #filtrar campos
from rest_framework.serializers import ModelSerializer
from farmacia_app.models import Farmacia


class FarmaciaSerializer(ModelSerializer):
    class Meta:
        model = Farmacia
        fields = ['id', 'nombre', 'imagen',
                'ubicacion','localidad','turno_date',
                'turno_time']
from rest_framework.serializers import ModelSerializer
from turno_app.models import Turno
from farmacia_app.api.serializers import FarmaciaSerializer


class TurnoSerializer(ModelSerializer):
    #Para conectar con otra tabla
    farmacia_data = FarmaciaSerializer(source='farmacia', read_only=True)


    class Meta:
        model = Turno
        fields = ['id', 'localizacion', 'turno_date',
                'turno_time','farmacia','farmacia_data']
from rest_framework.routers import DefaultRouter

from turno_app.api.views import TurnoApiViewSet


router_turno = DefaultRouter()

router_turno.register(
    prefix='turno_app', basename='turno_app', viewset= TurnoApiViewSet
)
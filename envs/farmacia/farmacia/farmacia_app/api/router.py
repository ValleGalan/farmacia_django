from rest_framework.routers import DefaultRouter

from farmacia_app.api.views import FarmaciaApiViewSet

router_farmacia = DefaultRouter()

router_farmacia.register(
    prefix='farmacia_app', basename='farmacia_app', viewset=FarmaciaApiViewSet
)
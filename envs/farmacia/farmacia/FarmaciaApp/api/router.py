from django.urls import path
from rest_framework.routers import DefaultRouter
#from rest_framework_simplejwt.views import TokenObtainPairView
from FarmaciaApp.api.views import UserApiViewSet, UserView

router_user = DefaultRouter()

router_user.register(
    prefix='FarmaciaApp', basename='FarmaciaApp', viewset=UserApiViewSet
)

urlpatterns = [
    path('auth/me/', UserView.as_view())
]
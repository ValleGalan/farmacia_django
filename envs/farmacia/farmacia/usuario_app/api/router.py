from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from usuario_app.api.views import UserApiViewSet, UserView

router_user = DefaultRouter()

router_user.register(
    prefix='usuario_app', basename='usuario_app', viewset=UserApiViewSet
)

urlpatterns = [
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/me/', UserView.as_view())
]
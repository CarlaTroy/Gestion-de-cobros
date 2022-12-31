from rest_framework.routers import DefaultRouter
from apps.authentication.api.view import UserViewSet

router = DefaultRouter()

router.register(r'authentication', UserViewSet, basename='authentication')

urlpatterns = router.urls
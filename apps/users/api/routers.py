from rest_framework.routers import DefaultRouter
from apps.users.api.view import UserViewSet

router = DefaultRouter()

router.register(r'authentication', UserViewSet, basename='authentication')

urlpatterns = router.urls
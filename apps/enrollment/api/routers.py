from rest_framework.routers import DefaultRouter
from apps.enrollment.api.views.enrollment_viewsets import EnrollmentViewSet
from apps.enrollment.api.views.payment_viewsets import PaymentViewSet

router = DefaultRouter()

router.register(r'enrollment', EnrollmentViewSet, basename='enrollment')
router.register(r'payment', PaymentViewSet, basename='payment')

urlpatterns = router.urls
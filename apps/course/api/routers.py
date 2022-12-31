from rest_framework.routers import DefaultRouter
from apps.course.api.views.course_viewsets import CourseViewSet
from apps.course.api.views.cohort_viewsets import CohortViewSet

router = DefaultRouter()

router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'cohort', CohortViewSet, basename='cohort')

urlpatterns = router.urls
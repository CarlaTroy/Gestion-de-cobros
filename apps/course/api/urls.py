from django.urls import path
from apps.course.api.views.course_viewsets import CourseViewSet
from apps.course.api.views.cohort_viewsets import CohortViewSet
urlpatterns = [
    #path('course/', CourseViewSet, name='course_create_list'),
    #path('course/retrieve-update-destroy/<int:pk>', CourseViewSet, name='course_retrieve_update_destroy'),

    #path('cohort/', CohortListCreateAPIView.as_view(), name='cohort_create_list'),
    #path('cohort/retrieve-update-destroy/<int:pk>', CohortRetrieveUpdateDestroyAPIView.as_view(), name='cohort_retrieve_update_destroy'),


]
from django.urls import path
from apps.student.views import StudentView
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', StudentView.as_view(), name='students')
]
urlpatterns = format_suffix_patterns(urlpatterns)
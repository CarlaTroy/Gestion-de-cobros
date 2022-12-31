from apps.enrollment.models import Enrollment

from rest_framework import serializers


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        exclude = ('state', 'created_date', 'modified_date','deleted_date')
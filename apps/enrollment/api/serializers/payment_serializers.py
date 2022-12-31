from rest_framework import serializers
from apps.enrollment.models import Payment
from apps.course.api.serializers.course_serializers import CourseSerializer


class PaymentSerializer(serializers.ModelSerializer):
    # course = CourseSerializer()
    # course = serializers.StringRelatedField()

    class Meta:
        model = Payment
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

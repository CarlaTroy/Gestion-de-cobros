from rest_framework import serializers
from apps.course.models import Cohort
from apps.course.api.serializers.course_serializers import CourseSerializer


class CohortSerializer(serializers.ModelSerializer):
    # course = CourseSerializer()
    #course = serializers.StringRelatedField()

    class Meta:
        model = Cohort
        # fields = ['course', 'name', 'initial_date', 'end_date' , 'effective_cost', 'credit_cost']
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')

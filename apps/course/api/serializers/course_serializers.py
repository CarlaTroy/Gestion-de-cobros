from rest_framework import serializers
from apps.course.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        # fields = '__all__'

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "name": instance.name,
            "description": instance.description,
            #"image": instance.image if instance.image != '' else '',
        }

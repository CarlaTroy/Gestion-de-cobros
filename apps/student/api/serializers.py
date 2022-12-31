from rest_framework import serializers
from apps.student.models import Student


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student

    def to_representation(self, instance):
        return {
            'last_names': instance['last_names'],
            'first_names': instance['first_names'],
            'identification': instance['identification'],
            'cellphone': instance['cellphone'],
            'address': instance['address'],
            'email': instance['email']
        }

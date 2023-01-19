from rest_framework import serializers
from apps.users.models import User


class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'name', 'last_name')
    
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user

"""class TestUserSerializer(serializers.Serializer):

    email = serializers.EmailField()

    def validate_email(self, value):
        if value == '': 
            raise serializers.ValidationError('Tiene que indicar un correo')
        return value

    def validate(self,data):
        return data

    def create(self,validated_data):
        return self.model.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance
    
    def save(self):
        print(self)
"""

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }

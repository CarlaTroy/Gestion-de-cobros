from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.authentication.models import User
from apps.authentication.api.serializers import UserSerializer


@api_view(['GET', 'POST'])
def user_api_view(request):
    # List
    if request.method == 'GET':
        # queryset
        users = User.objects.all().values('id', 'username', 'email', 'password', 'name')
        users_serializers = UserSerializer(users, many=True)
        return Response(users_serializers.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        user_serializer = UserSerializer(data=request.data)

        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_view(request, pk):
    if request.method == 'GET':
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user)
        return Response(user_serializer.data)

    elif request.method == 'PUT':
        user = User.objects.filter(id=pk).first()
        user_serializer = UserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data)
        return Response(user_serializer.errors)
    elif request.method == 'DELETE':
        user = User.objects.filter(id=pk).first()
        user.delete()
        return Response('Eliminado')

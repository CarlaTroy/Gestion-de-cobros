from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from apps.student.models import Student
from apps.student.api.serializers import StudentSerializer, StudentListSerializer


@api_view(['GET', 'POST'])
def student_api_view(request):
    #List
    if request.method == 'GET':

        #queryset
        students = Student.objects.all().values('last_names','first_names', 'identification','cellphone', 'address', 'email')
        students_serializer = StudentSerializer(students, many=True)
        return Response(students_serializer.data, status=status.HTTP_200_OK)

    #Create
    elif request.method == 'POST':
        student_serializer = StudentSerializer(data=request.data)

        #validacion
        if student_serializer.is_valid():
            student_serializer.save()
            return Response(student_serializer.data, status=status.HTTP_201_CREATED)
        return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_api_view(request, pk=None):
    #consulta queryset
    student = Student.objects.filter(id=pk).first()

    #validacion
    if student:
        #retrieve
        if request.method == 'GET':
            student_serializer = StudentSerializer(student)
            return Response(student_serializer.data, status=status.HTTP_200_OK)

        #update
        elif request.method == 'PUT':
            student_serializer = StudentSerializer(student, data=request.data)
            if student_serializer.is_valid():
                student_serializer.save()
                return Response(student_serializer.data, status=status.HTTP_200_OK)
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        #delete
        elif request.method == 'DELETE':
            student.delete()
            return Response({'message': '¡Estudiante eliminado correctamente!'}, status=status.HTTP_200_OK)

    return Response({'message': 'No se ha encontrado usuario con los datos solicitados'}, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import viewsets
from rest_framework import generics, status
from rest_framework.response import Response
from apps.users.authentication_mixins import Authentication
from apps.course.api.serializers.course_serializers import CourseSerializer


class CourseViewSet(Authentication, viewsets.ModelViewSet):
    serializer_class = CourseSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        #print(self.user)
        course_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(course_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Curso creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            course_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if course_serializer.is_valid():
                course_serializer.save()
                return Response(course_serializer.data, status=status.HTTP_200_OK)
            return Response(course_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        course = self.get_queryset().filter(id=pk).first()
        if course:
            course.state = False
            course.save()
            return Response({'message': 'Curso eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un curso con estos datos'}, status=status.HTTP_400_BAD_REQUEST)


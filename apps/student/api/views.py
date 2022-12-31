from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from apps.student.api.serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        student_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(student_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Estudiante creado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            student_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if student_serializer.is_valid():
                student_serializer.save()
                return Response(student_serializer.data, status=status.HTTP_200_OK)
            return Response(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        student = self.get_queryset().filter(id=pk).first()
        if student:
            student.state = False
            student.save()
            return Response({'message': 'Estudiante eliminado correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un estudiante con estos datos'}, status=status.HTTP_400_BAD_REQUEST)
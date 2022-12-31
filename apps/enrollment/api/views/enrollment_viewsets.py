from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from apps.enrollment.api.serializers.enrollment_serializers import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    serializer_class = EnrollmentSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        enrollment_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(enrollment_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Matricula creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            enrollment_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if enrollment_serializer.is_valid():
                enrollment_serializer.save()
                return Response(enrollment_serializer.data, status=status.HTTP_200_OK)
            return Response(enrollment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        enrollment = self.get_queryset().filter(id=pk).first()
        if enrollment:
            enrollment.state = False
            enrollment.save()
            return Response({'message': 'Matricula eliminada correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una matricula con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

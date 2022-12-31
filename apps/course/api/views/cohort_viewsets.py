from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from apps.course.api.serializers.cohort_serializers import CohortSerializer


class CohortViewSet(viewsets.ModelViewSet):
    serializer_class = CohortSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        cohort_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(cohort_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Cohorte creada correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            cohort_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if cohort_serializer.is_valid():
                cohort_serializer.save()
                return Response(cohort_serializer.data, status=status.HTTP_200_OK)
            return Response(cohort_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        cohort = self.get_queryset().filter(id=pk).first()
        if cohort:
            cohort.state = False
            cohort.save()
            return Response({'message': 'Cohorte eliminada correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe una cohorte con estos datos'}, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from apps.enrollment.api.serializers.payment_serializers import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, state=True).first()

    def list(self, request):
        payment_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(payment_serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Pago registrado correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            payment_serializer = self.serializer_class(self.get_queryset(pk), data=request.data)
            if payment_serializer.is_valid():
                payment_serializer.save()
                return Response(payment_serializer.data, status=status.HTTP_200_OK)
            return Response(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        payment = self.get_queryset().filter(id=pk).first()
        if payment:
            payment.state = False
            payment.save()
            return Response({'message': 'Payment correctamente'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un pago con estos datos'}, status=status.HTTP_400_BAD_REQUEST)


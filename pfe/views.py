from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Client, Facture, DateChange
from .serializers import (
    UserSerializer, ClientSerializer,
    FactureSerializer, DateChangeSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

    
# idk if this is needed yet
    # @action(detail=False, methods=['get'])
    # def all_sorted_by_client(self, request):
    #     # factures sorted by ID
    #     factures = Facture.objects.order_by('client__id')

    #     if not factures.exists():
    #         return Response({"message": "No factures available"}, status=200)

    #     serializer = self.get_serializer(factures, many=True)
    #     return Response(serializer.data)


class DateChangeViewSet(viewsets.ModelViewSet):
    queryset = DateChange.objects.all()
    serializer_class = DateChangeSerializer
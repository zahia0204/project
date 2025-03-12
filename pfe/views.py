
from rest_framework import viewsets
from .models import User, Client, Region, Facture, Case, Etat, DateChange
from .serializers import UserSerializer, ClientSerializer, RegionSerializer, FactureSerializer, CaseSerializer, EtatSerializer, DateChangeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = Case.objects.all()
    serializer_class = CaseSerializer

class EtatViewSet(viewsets.ModelViewSet):
    queryset = Etat.objects.all()
    serializer_class = EtatSerializer

class DateChangeViewSet(viewsets.ModelViewSet):
    queryset = DateChange.objects.all()
    serializer_class = DateChangeSerializer


from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User, Client, Region, Facture, DateChange
from .serializers import (
    UserSerializer, ClientSerializer, RegionSerializer,
    FactureSerializer, DateChangeSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.SearchFilter]  
    search_fields = ['client_id'] 
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.role.startswith("ResponsableDe"):
    #         region_name = user.role.replace("ResponsableDe", "")
    #         return Client.objects.filter(region__name__startswith=region_name)
    #     return Client.objects.all()

@action(detail=False, methods=['get'])
def get_by_etat(self, request):
    etat_name = request.query_params.get("etat_name")
    if not etat_name:
        return Response({"error": "etat_name parameter is required"}, status=400)

    clients = Client.objects.filter(etat__iexact=etat_name).distinct()
    serializer = self.get_serializer(clients, many=True)
    return Response(serializer.data)



class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class FactureViewSet(viewsets.ModelViewSet):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

    @action(detail=False, methods=['get'])
    def all_sorted_by_client(self, request):
        # factures sorted by ID
        factures = Facture.objects.order_by('client__id')

        if not factures.exists():
            return Response({"message": "No factures available"}, status=200)

        serializer = self.get_serializer(factures, many=True)
        return Response(serializer.data)

    # def get_queryset(self):
    #     #Filter cases based on responsable 
    #     user = self.request.user
    #     if user.role.startswith("ResponsableDe"):
    #         region_name = user.role.replace("ResponsableDe", "")
    #         return Case.objects.filter(employee__region__name__startswith=region_name)
    #     return Case.objects.all()


    # def get_queryset(self):
        # #Filter etats based on responsable
        # user = self.request.user
        # if user.role.startswith("ResponsableDe"):
        #     region_name = user.role.replace("ResponsableDe", "")
        #     return Etat.objects.filter(case__employee__region__name__startswith=region_name)
        # return Etat.objects.all()

class DateChangeViewSet(viewsets.ModelViewSet):
    queryset = DateChange.objects.all()
    serializer_class = DateChangeSerializer

    def get_queryset(self):
        user = self.request.user
        # if user.role.startswith("ResponsableDe"):
        #     region_name = user.role.replace("ResponsableDe", "")
        #     return DateChange.objects.filter(case__employee__region__name__startswith=region_name)
        # return DateChange.objects.all()

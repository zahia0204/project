from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from pfe.views import (
    UserViewSet, ClientViewSet, RegionViewSet, FactureViewSet, 
    CaseViewSet, EtatViewSet, DateChangeViewSet
)


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'regions', RegionViewSet)
router.register(r'factures', FactureViewSet)
router.register(r'cases', CaseViewSet)
router.register(r'etats', EtatViewSet)
router.register(r'datechanges', DateChangeViewSet)


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('api/', include(router.urls)),  
]



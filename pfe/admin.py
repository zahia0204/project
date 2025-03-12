from django.contrib import admin
from .models import User, Client, Region, Facture, Case, Etat, DateChange

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Region)
admin.site.register(Facture)
admin.site.register(Case)
admin.site.register(Etat)
admin.site.register(DateChange)


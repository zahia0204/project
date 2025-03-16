from django.db import models
from django.contrib.auth.models import AbstractUser , Group, Permission

class User(AbstractUser):
    ROLE_CHOICES = [
        ("admin", "Admin"),
        ("employee", "Employee"),
    ]

    phone_number = models.CharField(max_length=15)  
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(Group, related_name="user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="user_permissions", blank=True)

    def __str__(self):
        return f"{self.get_role_display()}: {self.username}"

class Region(models.Model):
    REGION_CHOICES = [
        ("Boufarik", "Boufarik"),
        ("Mozaia", "Mozaia"),
        ("Larbaa", "Larbaa"),
        ("OuladYaich", "Oulad Yaich"),
        ("ElWouroud", "El Wouroud"),
        ("Bougara", "Bougara"),
        ("Aafroun", "Aafroun"),
    ]
    name = models.CharField(max_length=50, choices=REGION_CHOICES, unique=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    CLIENT_TYPE_CHOICES = [
        ("Corporate", "Corporate"),
        ("Residential", "Residential"),
    ]
    client_id = models.CharField(max_length=50, unique=True)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    client_type = models.CharField(max_length=20, choices=CLIENT_TYPE_CHOICES)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)  

    def __str__(self):
        return self.full_name


class Facture(models.Model):
    invoice_id = models.CharField(max_length=50, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    client = models.ForeignKey(Client, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Facture {self.invoice_id} - {self.amount} USD"


class Total(models.Model):
    total_amount = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"Total: {self.total_amount} USD"


class Case(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'employee'})  
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"Case handled by {self.employee.username} for {self.client.full_name}"


class Etat(models.Model):
    STATUS_CHOICES = [
        ("Non Traité", "Non Traité"),
        ("Décédé", "Décédé"),
        ("Avocat", "Avocat"),
        ("Huissier", "Huissier"),
        ("Juridique", "Juridique"),
        ("En Cours", "En Cours"),
        ("Payment Réglé", "Payment Réglé"),
    ]
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Status: {self.status}"


class DateChange(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Change Date: {self.changed_at}"

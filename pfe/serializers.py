from rest_framework import serializers
from .models import User, Client, Region, Facture, Case, Etat, DateChange

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'role']
        extra_kwargs = {
            'password': {'write_only': True}  # Prevent exposing passwords
        }

    def create(self, validated_data):
        """Ensure password is hashed when creating a user"""
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
class ClientSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='region.name', read_only=True)

    class Meta:
        model = Client
        fields = '__all__'


class CaseSerializer(serializers.ModelSerializer):
    employee_name = serializers.SerializerMethodField()
    client_name = serializers.SerializerMethodField()

    class Meta:
        model = Case
        fields = '__all__'  
        read_only_fields = ['employee_name', 'client_name']  

    def get_employee_name(self, obj):
        return obj.employee.username  

    def get_client_name(self, obj):
        return f"{obj.client.name} {obj.client.surname}"  


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Case
        fields = '__all__'

class EtatSerializer(serializers.ModelSerializer):
    case_id = serializers.IntegerField(source='case.id', read_only=True)

    class Meta:
        model = Etat
        fields = '__all__'


class DateChangeSerializer(serializers.ModelSerializer):
    case_id = serializers.IntegerField(source='case.id', read_only=True)

    class Meta:
        model = DateChange
        fields = '__all__'



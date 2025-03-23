from rest_framework import serializers
from .models import User, Client, Facture,  DateChange
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'role']
        extra_kwargs = {
            'password': {'write_only': True} 
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password']) 
        return super().create(validated_data)

class FactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'

class DateChangeSerializer(serializers.ModelSerializer):
    case_id = serializers.IntegerField(source='case.id',  allow_null=True ,read_only=True)

    class Meta:
        model = DateChange
        fields = '__all__'



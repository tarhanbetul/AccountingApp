# serializers.py
from rest_framework import serializers
from .models import Company, Transaction
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class CustomVerifyJSONWebTokenSerializer(VerifyJSONWebTokenSerializer):
    def validate(self, attrs):
        data = super(CustomVerifyJSONWebTokenSerializer, self).validate(attrs)
        user = self.user
        data['username'] = user.username
        data['roles'] = user.groups.values_list('name', flat=True)
        return data
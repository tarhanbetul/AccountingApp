
from rest_framework import viewsets
from .models import Company
from .models import Transaction
from .serializers import CompanySerializer
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import DjangoObjectPermissions



class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, DjangoObjectPermissions] # Authentication and group/Permissions control



class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, DjangoObjectPermissions]  # Authentication and group/Permissions control


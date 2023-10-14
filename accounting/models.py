from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    company_name = models.CharField(max_length=100)
    tax_number = models.CharField(max_length=20)
    company_code = models.IntegerField()
    address = models.CharField(max_length=300)
    added_date = models.DateField()
    report = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_name

    class Meta:
        db_table = 'Company'

class Transaction(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)  # ForeignKey with Company models connection
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    report = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.company} - {self.transaction_type}"

    class Meta:
        db_table = 'Transaction'

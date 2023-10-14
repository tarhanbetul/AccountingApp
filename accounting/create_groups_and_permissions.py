
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounting.models import Company, Transaction 

# permission and groups 
content_type_company = ContentType.objects.get_for_model(Company)
can_add_company = Permission.objects.get(codename='add_company', content_type=content_type_company)
can_change_company = Permission.objects.get(codename='change_company', content_type=content_type_company)
can_delete_company = Permission.objects.get(codename='delete_company', content_type=content_type_company)
can_view_report = Permission.objects.get(codename='view_report', content_type=content_type_company)

content_type_transaction = ContentType.objects.get_for_model(Transaction)
can_add_transaction = Permission.objects.get(codename='add_transaction', content_type=content_type_transaction)

admin_group, created = Group.objects.get_or_create(name='Admin')
accountant_group, created = Group.objects.get_or_create(name='Muhasebeci')
processor_group, created = Group.objects.get_or_create(name='İşlemci')

# Admin group permisssion 
admin_group.permissions.add(can_add_company, can_change_company, can_delete_company, can_view_report)

# Accounting group permisssion 
accountant_group.permissions.add(can_view_report)

# processor group permisssion 
processor_group.permissions.add(can_add_transaction)

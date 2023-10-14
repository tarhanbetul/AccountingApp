from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'Create initial user groups'

    def handle(self, *args, **options):
        admin_group, created = Group.objects.get_or_create(name='Admin')
        accountant_group, created = Group.objects.get_or_create(name='Muhasebeci')
        processor_group, created = Group.objects.get_or_create(name='İşlemci')


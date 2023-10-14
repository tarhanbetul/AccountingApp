from django.test import TestCase
from django.test import Client
from django.contrib.auth.models import User
from .models import Company, Transaction
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import Group

USERNAME = 'TestUserForEndpointsTest'
PASSWORD = 'qwe123qwe'
TESTGROUP = 'Admin'

class CompanyAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.company = Company.objects.create(
            company_name="Test Company",
            tax_number="1234567890",
            company_code=123,
            address="Test Address",
            added_date="2023-10-14",
        )

    def generate_jwt_token(self, username, password):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        user = User.objects.get(username=username, password=password)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return f'Bearer {token}'

    def create_test_user(self):
        username = f'{USERNAME}1'
        password = PASSWORD
        user1 = User.objects.create_user(username=username, password=password)
        group, created = Group.objects.get_or_create(name=TESTGROUP)
        user1.groups.add(group)
        return user1

    def test_create_company(self):
        user1 = self.create_test_user()
        token = self.generate_jwt_token(user1.username, user1.password)

        response = self.client.post(
            '/accounting/api/firmalar/',
            {
                "company_name": "New Company",
                "tax_number": "0987654321",
                "company_code": 11,
                "address": "New Address",
                "added_date": "2023-10-15",
            },
            format='json',
            HTTP_AUTHORIZATION=token
        )
        # Test assertions...

    def test_update_company(self):
        user2 = self.create_test_user()
        token = self.generate_jwt_token(user2.username, user2.password)

        response = self.client.post(
            '/accounting/api/firmalar/',
            {
                "company_name": "New Company UPDATE",
                "tax_number": "0987654321",
                "company_code": 11,
                "address": "New Address",
                "added_date": "2023-10-15",
            },
            format='json',
            HTTP_AUTHORIZATION=token
        )

        self.assertEqual(response.status_code, 201)  # Success ANSWER
        company_id = response.data['id']

        updated_data = {
            "company_name": "Updated Company Name",
            "tax_number": "1234567890",
            "company_code": 11,
            "address": "Updated Address",
            "added_date": "2023-10-20",
        }
        update_response = self.client.put(
            f'/accounting/api/firmalar/{company_id}/',
            updated_data,
            format='json',
            content_type='application/json',
            HTTP_AUTHORIZATION=token
        )

        self.assertEqual(update_response.status_code, 200)  # Success UPDATE

    def test_read_companies(self):
        user3 = self.create_test_user()
        token = self.generate_jwt_token(user3.username, user3.password)

        response = self.client.get('/accounting/api/firmalar/', HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)  # Success ANSWER

    def test_delete_company(self):
        user4 = self.create_test_user()
        token = self.generate_jwt_token(user4.username, user4.password)

        response = self.client.post(
            '/accounting/api/firmalar/',
            {
                "company_name": "New Company DELETE",
                "tax_number": "0987654321",
                "company_code": 22,
                "address": "New Address",
                "added_date": "2023-10-15",
            },
            format='json',
            content_type='application/json',
            HTTP_AUTHORIZATION=token
        )

        self.assertEqual(response.status_code, 201)  # Success ANSWER
        company_id = response.data['id']
        delete_response = self.client.delete(
            f'/accounting/api/firmalar/{company_id}/',
            HTTP_AUTHORIZATION=token
        )

        self.assertEqual(delete_response.status_code, 204)  # Success DELETE

class TransactionAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        self.company = Company.objects.create(
            company_name="Test Company",
            tax_number="1234567890",
            company_code=123,
            address="Test Address",
            added_date="2023-10-14",
        )
    def generate_jwt_token(self, username, password):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        user = User.objects.get(username=username, password=password)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return f'Bearer {token}'

    def create_test_user(self):
        username = f'{USERNAME}2'
        password = PASSWORD
        user5 = User.objects.create_user(username=username, password=password)
        group, created = Group.objects.get_or_create(name=TESTGROUP)
        user5.groups.add(group)
        return user5

    def test_create_transaction(self):
        user5 = self.create_test_user()
        token = self.generate_jwt_token(user5.username, user5.password)

        response = self.client.post(
            '/accounting/api/islemler/',
            {
                "company": self.company.id,
                "user": user5.id,
                "transaction_type": "Purchase",
                "amount": "100.00",
                "date": "2023-10-15",
                "report": "Test transaction report",
            },
            format='json',
            content_type='application/json',
            HTTP_AUTHORIZATION=token
        )

        self.assertEqual(response.status_code, 201)  # Success ANSWER

    def test_read_transactions(self):
        user6 = self.create_test_user()
        token = self.generate_jwt_token(user6.username, user6.password)

        response = self.client.get('/accounting/api/islemler/', HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 200)  #

    def test_update_transaction(self):
        user7 = self.create_test_user()
        token = self.generate_jwt_token(user7.username, user7.password)

        response = self.client.post(
            '/accounting/api/islemler/',
            {
                "company": self.company.id,
                "user": user7.id,
                "transaction_type": "Purchase",
                "amount": "100.00",
                "date": "2023-10-15",
                "report": "Test transaction report",
            },
            format='json',
            content_type='application/json',
            HTTP_AUTHORIZATION=token
        )
        self.assertEqual(response.status_code, 201)  #  Success CREATE
        transaction_id = response.data['id']
        updated_data = {
            "company": self.company.id,
            "user": user7.id,
            "transaction_type": "Purchase UPDATE",
            "amount": "120.00",
            "date": "2023-09-12",
            "report": "Test transaction report UPDATE",
        }
        update_response = self.client.put(
            f'/accounting/api/islemler/{transaction_id}/',  # UPDATE
            updated_data,
            format='json',
            content_type='application/json',
            HTTP_AUTHORIZATION=token
        )

        self.assertEqual(update_response.status_code, 200)   # Success UPDATE

    def test_delete_transaction(self):
        user8 = self.create_test_user()
        token = self.generate_jwt_token(user8.username, user8.password)

        transaction = Transaction.objects.create(
            company=self.company,
            user=user8,
            transaction_type="Sale",
            amount=50.0,
            date="2023-10-15",
            report="Transaction to delete",
        )

        response = self.client.delete(f'/accounting/api/islemler/{transaction.id}/', HTTP_AUTHORIZATION=token)
        self.assertEqual(response.status_code, 204)  # Success DELETE

    def tearDown(self):
        self.client.logout()
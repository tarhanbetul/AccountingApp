from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet, TransactionViewSet
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()
router.register(r'firmalar', CompanyViewSet)
router.register(r'islemler', TransactionViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_jwt_token)

]

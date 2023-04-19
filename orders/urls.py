from django.urls import path
from .views import (CurrencyList, BrandList, OrderList, CurrencyViewSet,
                    CategoryViewSet, OrderViewSet, BrandViewSet,LocationCityViewSet)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'city',LocationCityViewSet)
urlpatterns = [
    path('currency/', CurrencyList.as_view()),
    path('brands/', BrandList.as_view()),
    path('order/', OrderList.as_view()),
    
]
urlpatterns += router.urls
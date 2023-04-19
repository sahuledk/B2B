from django.shortcuts import render
from .models import (Currencies, Brands, Order, BrandLocationCity,
                     Location, Categories, Countries, BrandLocationCity)
from .serializers import (Currencyserializer, Brandserializer, OrderSerializer,
                          LocationCitySerializer, CategorySerializer)
from rest_framework.generics import ListAPIView, ListCreateAPIView
from rest_framework import viewsets
from .management.commands.brandlocation import Command


class CurrencyList(ListAPIView):
    queryset = Currencies.objects.all()
    serializer_class = Currencyserializer


class BrandList(ListAPIView):
    queryset = Brands.objects.all()
    serializer_class = Brandserializer


class OrderList(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currencies.objects.all()
    serializer_class = Currencyserializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brands.objects.all()
    serializer_class = Brandserializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class LocationCityViewSet(viewsets.ModelViewSet):
    queryset = BrandLocationCity.objects.all()
    serializer_class = LocationCitySerializer
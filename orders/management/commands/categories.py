from django.core.management.base import BaseCommand
import datetime
import requests
from httpsig.requests_auth import HTTPSignatureAuth
import json
from orders.models import Categories
from orders.serializers import CategorySerializer, Categoryserializer


class Command(BaseCommand):
    help = 'To get category details'

    def categories(self):
        API_KEY = 'NGJHIVCEHBZCODYQC0EF'
        API_SECRET = 'MK6Go9VxfyVykdHTaW6UyHpJCW7c1mP9R1qCwqCH'

        uri = "https://private-anon-91b0e7114e-ygagcorporaterewards.apiary-mock.com/corporate/api/v2-4/ar/categories/"


        # signature_headers = ['accept', 'date']
        # headers = {
        #     'Accept': 'application/json',
        #     'X-Api-Key': API_KEY,
        #     'date': str(datetime.datetime.utcnow()),
        # }

        # auth = HTTPSignatureAuth(key_id=API_KEY, secret=API_SECRET, headers=signature_headers)
        category_details = requests.get(uri)
        category_details = category_details.json()['categories']
        return category_details

    def handle(self, *args, **kwargs):
        categories = self.categories()
        serializer = CategorySerializer(data=categories, many=True)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return categories







from django.core.management.base import BaseCommand
import datetime
import requests
from httpsig.requests_auth import HTTPSignatureAuth
import json
from orders.models import Currencies
from orders.serializers import Currencyserializer


class Command(BaseCommand):
    help = 'To get currency details'

    def currencies(self):
        API_KEY = 'NGJHIVCEHBZCODYQC0EF'
        API_SECRET = 'MK6Go9VxfyVykdHTaW6UyHpJCW7c1mP9R1qCwqCH'

        uri = "https://private-anon-91b0e7114e-ygagcorporaterewards.apiary-mock.com/corporate/api/v2-4/currencies/"


        # signature_headers = ['accept', 'date']
        # headers = {
        #     'Accept': 'application/json',
        #     'X-Api-Key': API_KEY,
        #     'date': str(datetime.datetime.utcnow()),
        # }

        # auth = HTTPSignatureAuth(key_id=API_KEY, secret=API_SECRET, headers=signature_headers)
        currency_details = requests.get(uri)
        currency_details = currency_details.json()
        return currency_details

    def handle(self, *args, **kwargs):
        currency = self.currencies()
        serializer = Currencyserializer(data=currency['currencies'], many=True)
        if serializer.is_valid():
            serializer.save()
        else:
            print(serializer.errors)
        return currency







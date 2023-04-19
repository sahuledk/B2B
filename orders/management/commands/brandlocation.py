from django.core.management.base import BaseCommand
import datetime
import requests
from httpsig.requests_auth import HTTPSignatureAuth
import json
from orders.models import BrandLocationCity, Location
from orders.serializers import LocationCitySerializer


class Command(BaseCommand):
    help = 'To get brand location in a city '

    def location(self):
        API_KEY = 'NGJHIVCEHBZCODYQC0EF'
        API_SECRET = 'MK6Go9VxfyVykdHTaW6UyHpJCW7c1mP9R1qCwqCH'

        uri = "https://private-anon-239d136929-ygagcorporaterewards.apiary-mock.com/corporate/api/v2-4/ar/brands/brand_code/locations/city_id/"


        # signature_headers = ['accept', 'date']
        # headers = {
        #     'Accept': 'application/json',
        #     'X-Api-Key': API_KEY,
        #     'date': str(datetime.datetime.utcnow()),
        # }

        # auth = HTTPSignatureAuth(key_id=API_KEY, secret=API_SECRET, headers=signature_headers)
        response = requests.get(uri)
        details = response.json()
        print(details)
        return details



    def handle(self, *args, **kwargs):
        details = self.location()
        print(details)
        locations = details.pop('locations')
        print(locations)
        for location in locations:
            Location.objects.create(**location)
        # BrandLocationCity.objects.create(**details)




        # serializer = LocationCitySerializer(data=details)
        # if serializer.is_valid():
        #     serializer.save(commit=False)
        # else:
        #     print(serializer.errors)


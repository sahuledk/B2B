from django.core.management.base import BaseCommand
import datetime
import requests
from httpsig.requests_auth import HTTPSignatureAuth
import json
from orders.serializers import Brandserializer
from orders.models import Countries, Categories, Currencies, MyImage, Brands


class Command(BaseCommand):
    help = 'To get brand details'

    def brands(self):
        API_KEY = 'NGJHIVCEHBZCODYQC0EF'
        API_SECRET = 'MK6Go9VxfyVykdHTaW6UyHpJCW7c1mP9R1qCwqCH'

        uri = "https://private-anon-91b0e7114e-ygagcorporaterewards.apiary-mock.com/corporate/api/v2-4/ar/brands/"
        # uri = uri.format(brand_code=1847)

        #

        brand_details = requests.get(uri)
        brand_details = brand_details.json()['brands']

        return brand_details

    def handle(self, *args, **kwargs):
        brands = self.brands()
        for brand in brands:
            category_list = []
            images_list = []
            country = brand.pop('country')
            currency = brand.pop('brand_accepted_currency')
            Countries.objects.get_or_create(**country)
            categories = brand.pop('categories')
            images = brand.pop('image_gallery')
            brand.pop('is_generic')
            brand.pop('denominations')
            Brands.objects.create(**brand)
            for category in categories:
                category = Categories.objects.get_or_create(**category)
                Brands.objects.update(categories=category.categories_id)
                category_list.append(category)
                print(category_list)
            for image in images:
                image = MyImage.objects.get_or_create(**image)
                images_list.append(image)
                print(images_list)
            print(country)
            print(brand)







        # serializer = Brandserializer(data=brands, many=True)
        # if serializer.is_valid():
        #     serializer.save()
        # else:
        #     print(serializer.errors)









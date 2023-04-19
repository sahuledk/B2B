from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import (Currencies, City, MyImage,
                     Countries, Languages, Categories,
                     Brands, MobileNumberFormat, Order, Utilized,
                     Order_amount, Brand_amount, Gift, Location,
                     BrandLocationCity, BrandLocation)


class Currencyserializer(ModelSerializer):
    class Meta:
        model = Currencies
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class Categoryserializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name']


class Langaugeserializer(ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


class Mobileseserializer(ModelSerializer):
    class Meta:
        model = MobileNumberFormat
        fields = ['mobile_number_formats']


class Countryserializer(ModelSerializer):
    mobile_number_formats = Mobileseserializer(many=True)
    languages = Langaugeserializer()

    class Meta:
        model = Countries
        fields = '__all__'


class BrandCityserializer(ModelSerializer):
    class Meta:
        model = City
        fields = ['city_locations_url']


class Imageserializer(ModelSerializer):
    class Meta:
        model = MyImage
        exclude = ('id',)

class CountryOnlySerializer(ModelSerializer):
    class Meta:
        model = Countries
        fields = ['name', 'code']


class Brandserializer(ModelSerializer):

    # country = CountryOnlySerializer(many=True)
    image_gallery = Imageserializer(many=True)
    categories = Categoryserializer(many=True)
    # locations_url = BrandCityserializer()

    class Meta:
        model = Brands
        fields = ['id', 'is_active', 'brand_code', 'pin_redeemable', 'name', 'logo', 'product_image', 'validity_in_months', 'variable_amount', 'tagline', 'description',
                  'brand_accepted_currency', 'redemption_type', 'redemption_instructions', 'detail_url', 'locations_url', 'categories', 'image_gallery']

    def create(self, validated_data):
        print(validated_data)
        category_data = validated_data.pop('categories')
        # country_data= validated_data.pop('country')
        image_data = validated_data.pop('image_gallery')
        brand = Brands.objects.create(**validated_data)
        # for country_data in country_data:
        #     Countries.objects.create(country=brand, **country_data)
        for category in category_data:
            Categories.objects.create(categories=brand, **category)
        for images in image_data:
            MyImage.objects.create(image_gallery=brand, **images)
        return brand

class Utilize(ModelSerializer):
    class Meta:
        model = Utilized
        exclude = ('id',)


class Ordered_serializer(ModelSerializer):
    class Meta:
        model = Order_amount
        fields = '__all__'


class BrandedSerializer(ModelSerializer):
    class Meta:
        model = Brand_amount
        fields = '__all__'


class BrandCodeSerializer(ModelSerializer):
    class Meta:
        model = Brands
        fields = ["logo", "product_image", "brand_code", "name"]


class GiftSerializer(ModelSerializer):
    class Meta:
        model = Gift
        fields = ['label', 'value']


class OrderSerializer(ModelSerializer):
    utilized_details = Utilize()
    ordered_amount = Ordered_serializer()
    brand_accepted_amount = BrandedSerializer()
    brand_accepted_currency = Currencyserializer()
    brand_details = BrandCodeSerializer()
    gift_voucher = GiftSerializer()
    country = CountryOnlySerializer()
    delivery_language = Langaugeserializer()

    class Meta:
        model = Order
        fields = ['gift_token', 'order_id', 'state', 'utilized_details', 'ordered_amount',
                  'brand_accepted_amount', 'reference_id', 'exchange_rate', 'notify',
                  'brand_accepted_currency', 'amount', 'barcode', 'brand_details', 'gift_voucher', 'expiry_date',
                  'redemption_instructions', 'country', 'receiver_name', 'receiver_email',
                  'receiver_phone', 'delivery_language', 'date_added']


class LocationSerializer(ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'



class LocationCitySerializer(ModelSerializer):
    locations = LocationSerializer(many=True)

    class Meta:
        model = BrandLocationCity
        fields = '__all__'

    def create(self, validated_data):
        print(validated_data)
        locations_data = validated_data.pop('locations')
        print(locations_data)
        city = BrandLocationCity.objects.create(**validated_data)
        for location in locations_data:
            print(location)
            try:
                print('+++++++++++++++++++')
                location_value = Location.objects.get(locations=city)
                print(location_value)
                print('-----------------')
            except Location.DoesNotExist:
                print('==================')
                Location.objects.create(locations=city, **location)

        return city



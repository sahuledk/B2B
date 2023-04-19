from django.db import models
import pytz
TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))
# from timezone_field import TimeZoneField


# Create your models here.
class Currencies(models.Model):
    name = models.TextField()
    code = models.TextField(primary_key=True, unique=True)

    def __str__(self):
        return self.code

class ExcahngeRate(models.Model):
    base_currency = models.ForeignKey(Currencies, on_delete=models.CASCADE, related_name='base')
    target_currency = models.ForeignKey(Currencies, on_delete=models.CASCADE, related_name='target')
    conversion_rate = models.CharField(max_length=10)

    def __str__(self):
        return self.conversion_rate

class Topup(models.Model):
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    amount = models.IntegerField()
    reference_id = models.IntegerField(primary_key=True, unique=True)

    def __init__(self):
            return self.reference_id

class Categories(models.Model):
    name = models.CharField(max_length=75)
    brands_url = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.name 

class Languages(models.Model):
    name = models.TextField()
    lang_code = models.TextField(primary_key=True, unique=True)

    def __str__(self):
        return self.lang_code

class MobileNumberFormat(models.Model):
    mobile_number_formats = models.CharField(max_length=25)

class Countries(models.Model):
    name = models.CharField(max_length=75)
    code = models.CharField( max_length=75)
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE, null=True)
    timezone = models.CharField(max_length=32, choices=TIMEZONES, default='UTC')
    mobile_number_formats = models.ManyToManyField(MobileNumberFormat, null=True)
    mobile_number_regex = models.CharField(max_length=75, null=True)
    detail_url = models.URLField(max_length=200, null=True)
    languages = models.ManyToManyField(Languages, null=True)

class City(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=75)
    city_locations_url = models.URLField(max_length=250)

    def __str__(self):
        return self.city_locations_url

class Retailers(models.Model):
    name = models.CharField(max_length=75)

    def __str__(self):
        return self.name 


class MyImage(models.Model):
    image = models.CharField(max_length=500)

    def __str__(self):
        return self.image


class Brands(models.Model):
    brand_code = models.CharField(max_length=30, null=True)
    is_active = models.BooleanField(default=False)
    pin_redeemable = models.BooleanField(default=True)
    name = models.CharField(max_length=75)
    logo = models.CharField(max_length=300, null=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE, null=True)
    image_gallery = models.ForeignKey(MyImage,on_delete=models.CASCADE, null=True, blank=True)
    product_image = models.CharField(max_length=300, null=True)
    validity_in_months = models.IntegerField(null=True)
    variable_amount = models.BooleanField(default=False)
    #denominations
    tagline = models.CharField(max_length=275, null=True)
    description = models.TextField(null=True)
    brand_accepted_currency = models.OneToOneField(Currencies, on_delete=models.CASCADE, null=True)
    # classgalleryfield.fields.GalleryField(target_model=MyImage, *args, **kwargs)
    redemption_type = models.CharField(max_length=50, null=False, blank=False)
    redemption_instructions = models.TextField(max_length=1000, null=True)
    detail_url = models.CharField(max_length=200, null=True)
    locations_url = models.URLField(null=True)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)



    def __str__(self):
        return self.name 
        

class BrandLocation(models.Model):
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE)
    cities = models.ManyToManyField(City)
    Retailers = models.ManyToManyField(Retailers)


class Location(models.Model):
    name = models.CharField(max_length=275)
    phone = models.CharField(max_length=30, null=True)


class BrandLocationCity(models.Model):
    brand_name = models.CharField(max_length=30, null=True) #models.ForeignKey(Brands, on_delete=models.CASCADE, null=True)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)


class Order_amount(models.Model):
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Brand_amount(models.Model):
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    amount = models.IntegerField()

class Gift(models.Model):
    label = models.CharField(max_length=100)
    value = models.CharField(max_length=100)


class Utilized(models.Model):
    redemption_reference_id = models.CharField(max_length=100)
    redemption_id = models.CharField(max_length=100)
    utilized_date = models.DateField()
    brand_code = models.CharField(max_length=100)
    

class Order(models.Model):
    gift_token = models.CharField(max_length=100)
    order_id = models.CharField(max_length=100)
    state = models.IntegerField()
    utilized_details = models.ForeignKey(Utilized, on_delete=models.CASCADE, null=True, blank=True)
    ordered_amount = models.ForeignKey(Order_amount, on_delete=models.CASCADE, null=True, blank=True)
    brand_accepted_amount = models.ForeignKey(Brand_amount, on_delete=models.CASCADE, null=True, blank=True)
    extra_field = models.CharField(max_length=100, null=True)
    reference_id = models.IntegerField(max_length=40, primary_key=True)
    exchange_rate = models.ForeignKey(ExcahngeRate, on_delete=models.CASCADE, related_name='exchange')
    notify = models.BooleanField(default=True)
    currency = models.ForeignKey(Currencies, on_delete=models.CASCADE)
    amount = models.IntegerField()
    barcode = models.URLField(null=True, blank=True)
    brand_details = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='brand_details')
    gift_voucher = models.ManyToManyField(Gift)
    expiry_date = models.DateField()
    redemption_instructions = models.TextField()
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    receiver_name = models.CharField(max_length=100)
    receiver_email = models.EmailField()
    receiver_phone = models.CharField(max_length=75)
    delivery_language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    date_added = models.DateField()

































from django.contrib import admin
from django.apps import apps
post_models = apps.get_app_config('orders').get_models()

# from .models import MyGallery
# from galleryfield.mixins import GalleryFormMediaMixin


# class MyGalleryAdminForm(GalleryFormMediaMixin, forms.ModelForm):
#     class Meta:
#         model = MyGallery
#         exclude = ()


# class MyGalleryAdmin(admin.ModelAdmin):
#     form = MyGalleryAdminForm

# admin.site.register(MyGallery, MyGalleryAdmin)



for model in post_models:
    admin.site.register(model)

# Register your models here.
# admin.site.register(Currencies)
# admin.site.register(Topup)
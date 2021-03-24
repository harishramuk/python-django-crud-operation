from django.contrib import admin
from TestApp.models import Parcel

# Register your models here.
class ParcelAdmin(admin.ModelAdmin):
    list_display = ['billno','shippername','rate']
admin.site.register(Parcel,ParcelAdmin)

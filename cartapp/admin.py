from django.contrib import admin
from cartapp import models
# Register your models here.
from cartapp.models import cart


class cartadmin(admin.ModelAdmin):
    list_display=['username','pid','units','unitprice','tuprice','image']
    list_filter=['pid','username']
    class Meta:
        model=cart
admin.site.register(cart,cartadmin)


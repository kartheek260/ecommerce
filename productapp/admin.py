from django.contrib import admin
from .models import product, stock


class productadmin(admin.ModelAdmin):
    list_display = ['pid', 'pcat', 'pname', 'pdscnt', 'pcost', 'pmfdt', 'pexpdt','pimage']
    list_filter = ['pcat', 'pname']

    class Meta:
        model = product


admin.site.register(product, productadmin)


class stockadmin(admin.ModelAdmin):
    list_display = ['prodid', 'totqty', 'last_update', 'next_update']
    list_filter = ['prodid']

    class meta:
        model = stock


admin.site.register(stock, stockadmin)

# Register your models here.

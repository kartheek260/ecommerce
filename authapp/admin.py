from django.contrib import admin
from .models import registers


# Register your models here.
class Regadmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'Password', 'confirm_Password', 'phone']
    list_filter = ['email']

    class meta:
        model = registers


admin.site.register(registers, Regadmin)

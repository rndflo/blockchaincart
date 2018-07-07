from django.contrib import admin

# Register your models here.
from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["__str__", "created", "updated"]
    class Meta:
        model = Product

admin.site.register(Product, ProductModelAdmin)
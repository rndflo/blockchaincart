from django.contrib import admin

# Register your models here.
from .models import Product

class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "created", "updated"]
    list_filter = ["created", "updated"]
    search_fields = ["title", "description"]
    class Meta:
        model = Product

admin.site.register(Product, ProductModelAdmin)
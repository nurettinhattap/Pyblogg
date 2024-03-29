from django.contrib import admin
from .models import Product, Offer, mpost


class OfferAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')


class mpostAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')


admin.site.register(Offer, OfferAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(mpost, mpostAdmin)

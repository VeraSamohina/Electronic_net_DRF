from django.contrib import admin

from electronic.models import Seller, Product

admin.site.register(Product)


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city', 'product', 'provider')
    list_filter = ('city',)


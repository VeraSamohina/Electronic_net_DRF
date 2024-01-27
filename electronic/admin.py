from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from electronic.models import Seller, Product

admin.site.register(Product)


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt='0')


@admin.register(Seller)
class SellerAdmin(admin.ModelAdmin):
    list_display = ('title', 'country', 'city',  'view_provider_link')
    list_filter = ('city',)
    actions = [clear_debt]

    def view_provider_link(self, obj):
        """
        Создает HTML-ссылку на страницу редактирования поставщика.
            obj (Seller): Экземпляр модели Seller.

        Returns:
            str: HTML-ссылка на страницу поставщика или '-' если поставщик отсутствует.
        """
        if obj.provider:
            url = reverse("admin:electronic_seller_change", args=[obj.provider.pk])
            return format_html('<a href="{}">{}</a>', url, obj.provider.title)
        return "-"

    view_provider_link.short_description = "Поставщик"

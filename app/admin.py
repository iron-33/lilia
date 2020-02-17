from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin
from .models import *


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ("name", "parent")
    mptt_level_indent = 20


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "get_image")
    list_display_links = ("name",)
    def get_image(self, obj):
        return mark_safe(f'<img src={obj.img.url} width="50" height="50"')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("card", "date", "status")
    list_filter = ("status",)
    readonly_fields = ['get_table_products']


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "status")
    list_filter = ("user", "status")
    list_display_links = ("user",)



admin.site.register(CardItem)
admin.site.register(Comment)

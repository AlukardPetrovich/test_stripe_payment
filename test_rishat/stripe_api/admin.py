from django.contrib import admin

from .models import Item, Order, OrderedItem


class ItemAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'price')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('pk',)


class OrderedItemAdmin(admin.ModelAdmin):
    list_display = ('item', 'amount', 'order')


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedItem, OrderedItemAdmin)

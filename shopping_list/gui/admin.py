from django.contrib import admin
from .models import ShoppingItem

class ShoppingItemAdmin(admin.ModelAdmin):
    model = ShoppingItem
    ordering = ('name', 'quantity')
    search_fields = ('name',)
    list_display = ('name', 'quantity', 'bought')
    fields = ('name', 'quantity', 'bought')

admin.site.register(ShoppingItem, ShoppingItemAdmin)

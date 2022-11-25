from django.contrib import admin
from .models import ShoppingItem, ShoppingList


class ShoppingItemAdmin(admin.ModelAdmin):
    model = ShoppingItem
    ordering = ('shopping_list', 'name', 'quantity')
    search_fields = ('name', 'shopping_list')
    list_display = ('shopping_list', 'name', 'quantity', 'bought')
    fields = ('shopping_list', 'name', 'quantity', 'bought')


class ShoppingItemInlineAdmin(admin.TabularInline):
    model = ShoppingItem


class ShoppingListAdmin(admin.ModelAdmin):
    model = ShoppingList
    ordering = ('name', 'owner')
    search_fields = ('name',)
    list_display = ('name', 'owner')
    fields = ('name', 'owner')
    inlines = [ShoppingItemInlineAdmin]


admin.site.register(ShoppingItem, ShoppingItemAdmin)
admin.site.register(ShoppingList, ShoppingListAdmin)

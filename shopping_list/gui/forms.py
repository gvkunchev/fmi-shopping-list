from django import forms
from .models import ShoppingItem, ShoppingList


class AddShoppingItemForm(forms.ModelForm):

    class Meta:
        model = ShoppingItem
        fields = ('name', 'quantity', 'shopping_list')

class AddShoppingListForm(forms.ModelForm):

    class Meta:
        model = ShoppingList
        fields = ('name', 'owner')

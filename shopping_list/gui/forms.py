from django import forms
from .models import ShoppingItem


class AddShoppingItemForm(forms.ModelForm):

    class Meta:
        model = ShoppingItem
        fields = ('name', 'quantity', 'shopping_list')

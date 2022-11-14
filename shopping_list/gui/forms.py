from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ShoppingItem, ShoppingList


class AddShoppingItemForm(forms.ModelForm):

    class Meta:
        model = ShoppingItem
        fields = ('name', 'quantity', 'shopping_list')


class AddShoppingListForm(forms.ModelForm):

    class Meta:
        model = ShoppingList
        fields = ('name', 'owner')


class RegisterUserForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",
                  "password1", "password2")

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator


class ShoppingList(models.Model):
    name = models.CharField(max_length=90)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.username} - {self.name}"


class ShoppingItem(models.Model):
    name = models.CharField(max_length=90)
    quantity = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    bought = models.BooleanField(default=False)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE,
                                      related_name='items')

    def __str__(self):
        return self.name

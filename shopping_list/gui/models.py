from django.db import models
from django.contrib.auth.models import User


class ShoppingList(models.Model):
    name = models.CharField(max_length=90)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.owner.email} - {self.name}"


class ShoppingItem(models.Model):
    name = models.CharField(max_length=90)
    quantity = models.IntegerField(default=1)
    bought = models.BooleanField(default=False)
    shopping_list = models.ForeignKey(ShoppingList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

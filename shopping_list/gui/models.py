from django.db import models

class ShoppingItem(models.Model):
    name = models.CharField(max_length=90)
    quantity = models.IntegerField(default=1)
    bought = models.BooleanField(default=False)

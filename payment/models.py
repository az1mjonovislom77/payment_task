from django.db import models
from django.core.validators import MinValueValidator


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return self.name

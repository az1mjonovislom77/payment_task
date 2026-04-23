from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    currency = models.CharField(max_length=10, default='usd')

    def __str__(self):
        return self.name


class Discount(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.percent}%)"


class Tax(models.Model):
    name = models.CharField(max_length=100)
    percent = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ({self.percent}%)"


class Order(models.Model):
    items = models.ManyToManyField(Item)
    discount = models.ForeignKey(Discount, null=True, blank=True, on_delete=models.SET_NULL)
    tax = models.ForeignKey(Tax, null=True, blank=True, on_delete=models.SET_NULL)

    def get_total_amount(self):
        total = sum(item.price for item in self.items.all())

        if self.discount:
            total -= total * self.discount.percent // 100

        if self.tax:
            total += total * self.tax.percent // 100

        return total

    def __str__(self):
        return f"Order {self.id}"

from django.db import models
from customers.models import Customer
from companies.models import Product


class Basket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count_products = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)


    # def __str__(self):
    #     return f"Корзина для {self.customer.first_name} {self.customer.last_name} | Товар: {self.product.name_prod}"


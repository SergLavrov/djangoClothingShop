from django.db import models

# Create your models here.

class Company(models.Model):                        # КОМПАНИИ/ПРОДАВЦЫ
    name_company = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)


    class Meta:
        ordering = ['name_company']


class Category(models.Model):                      # КАТЕГОРИИ ТОВАРОВ (ОДЕЖДА, ОБУВЬ, АКСЕССУАРЫ)
        name_category = models.CharField(max_length=50)

class Season(models.Model):
    name_season = models.CharField(max_length=50)

class ProductComposition(models.Model):                         # СОСТАВ ТОВАРА
    product_composition = models.CharField(max_length=50)

class SizeCloth(models.Model):
    size_cloth = models.IntegerField()

class SizeShoes(models.Model):
    size_shoes = models.IntegerField()


# class Reserv(models.Model):
#     is_reserved = models.BooleanField(default=False)


class Product(models.Model):
    name_prod = models.CharField(max_length=50)
    article = models.CharField(max_length=50)
    description = models.TextField(null=True)
    color = models.CharField(max_length=50)
    price = models.FloatField()
    product_count = models.IntegerField()  # (наличие товара на складе, единиц)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # ForeignKey
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True)     # ForeignKey
    product_composition = models.ForeignKey(ProductComposition, on_delete=models.SET_NULL, null=True) # ForeignKey
    size_cloth = models.ForeignKey(SizeCloth, on_delete=models.SET_NULL, null=True) # ForeignKey
    size_shoes = models.ForeignKey(SizeShoes, on_delete=models.SET_NULL, null=True) # ForeignKey
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True)      # ForeignKey
    # photo = models.ImageField(null=True, blank=True)   # (ФОТОГРАФИИ товара)
    # reserv = models.ForeignKey(Reserv, on_delete=models.SET_NULL, null=True)  # ForeignKey

    class Meta:
        ordering = ['name_prod']
# from django.db import models
# from djrichtextfield.models import RichTextField
#
# from apps.accounts.models import User
# from apps.common.models import Media
#
#
# class Category(models.Model):
#     name = models.CharField(max_length=100)
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=None)
#     image = models.ForeignKey(Media, on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.FloatField()
#     short_description = models.TextField(max_length=500)
#     description = models.TextField()
#     quantity = models.IntegerField()
#     instructions = RichTextField()
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     in_stock = models.BooleanField(default=False)
#     brand = models.CharField(max_length=100, blank=True, null=True)
#     discount = models.IntegerField(default=0)
#
#
# class Wishlist(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.user.username
#
#
# class ProductSize(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     size = models.CharField(max_length=5)
#
#     def __str__(self):
#         return f'{self.product.name}'
#
#
# class ProductColor(models.Model):
#     color = models.CharField(max_length=10)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#
# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ForeignKey(Media, on_delete=models.CASCADE)
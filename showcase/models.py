from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=50)
    order = models.PositiveIntegerField(unique=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child')

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='category')

    def __str__(self):
        return self.name


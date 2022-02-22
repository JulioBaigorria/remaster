from django.db import models

# from apps.utils import SoftDeleteQuerySet, SoftDeleteManager, DeletedQuerySet, DeletedManager


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ToxicityLabel(Common):
    category = models.CharField('Category', max_length=3)
    color = models.CharField('Color Band', max_length=15)

    class Meta:
        db_table = 'toxicity_label'

    def __str__(self):
        return f'{self.category} - {self.color}'


class ActiveIngredient(Common):
    name = models.CharField('Active Ingredient and ', max_length=70, unique=True)

    class Meta:
        ordering = ['-name']

    def __str__(self):
        return f'{self.name}'


class Type(Common):
    name = models.CharField('Type Name', max_length=20)

    def __str__(self):
        return f'{self.name}'


class Formulation(models.Model):
    name = models.CharField('Formulation', max_length=50)
    symbol = models.CharField('Symbol', max_length=4)

    def __str__(self):
        return f'{self.name} {self.symbol}'


class Product(Common):
    name = models.CharField('Official registered name', max_length=100)
    cod_senasa = models.CharField('Product code', max_length=10, unique=True)
    types = models.ManyToManyField(Type, related_name="products")
    act_ingredients = models.ManyToManyField(ActiveIngredient, related_name="products")
    tox_labels = models.ManyToManyField(ToxicityLabel, related_name="products")

    def __str__(self):
        return f'{self.name}'

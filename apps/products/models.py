from apps.clients.models import Client
from django.db import models


# from apps.utils import SoftDeleteQuerySet, SoftDeleteManager, DeletedQuerySet, DeletedManager


class Common(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['name']


class ToxicityLabel(Common):
    category = models.CharField('Category', max_length=3)
    color = models.CharField('Color Band', max_length=15)

    class Meta:
        db_table = 'toxicity_label'
        ordering = ['category']

    def __str__(self):
        return f'{self.category} - {self.color}'


class ActiveIngredient(Common):
    name = models.CharField('Active Ingredient and ', max_length=70, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Type(Common):
    name = models.CharField('Type Name', max_length=20)

    def __str__(self):
        return f'{self.name}'


class Formulation(models.Model):
    symbol = models.CharField('Symbol', max_length=4)
    name = models.CharField('Name', max_length=50)

    class Meta:
        ordering = ['symbol']

    def __str__(self):
        return f'{self.symbol} - {self.name}'


class Product(Common, models.Model):
    name = models.CharField('Official registered name', max_length=100)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True, blank=True)
    cod_senasa = models.CharField('Product code', max_length=10, unique=True)
    types = models.ManyToManyField(Type, related_name="products")
    act_ingredients = models.ManyToManyField(ActiveIngredient, related_name="products")
    formulations = models.ManyToManyField(Formulation, related_name="products")
    tox_labels = models.ManyToManyField(ToxicityLabel, related_name="products")
    is_trazable = models.BooleanField('Is trazable?', default=False)


    def __str__(self):
        return f'{self.name}'

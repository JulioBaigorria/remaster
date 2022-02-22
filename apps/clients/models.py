from django.conf import settings
from django.db import models

from apps.products.models import Product
# from apps.utils import SoftDeleteQuerySet, SoftDeleteManager, DeletedQuerySet, DeletedManager


class Common(models.Model):
    tnumber = models.CharField('Telephone Number', max_length=40)
    address = models.CharField('Address', max_length=50)
    city = models.CharField('City', max_length=50)
    pcode = models.CharField('City Postal Code', max_length=10)
    country = models.CharField('Country', max_length=30)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    class Meta:
        abstract = True


class Client(Common):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField('Client / Company Name', max_length=200)
    cuit = models.CharField('Company CUIT', max_length=13, unique=True)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'


class Deposit(Common):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    gln = models.CharField('Deposit GLN', max_length=13, unique=True)
    senasa_id = models.CharField('SENASA Identifier', max_length=15, unique=True)
    latitude = models.FloatField('Deposit Latitude', max_length=30)
    longitude = models.FloatField('Deposit Longitude', max_length=30)

    def __str__(self):
        return f'GLN: {self.gln} from {self.client.name[:20]} {self.address}'

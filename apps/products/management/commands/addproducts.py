from itertools import islice

import pandas as pd
from django.core.management.base import BaseCommand

from apps.products.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        file = 'apps/products/management/formulados_2021.xlsx'
        newdata = pd.read_excel(file).drop_duplicates()
        print(newdata.head())
        # objs = [Product(name=i[0]) for i in newdata.values]
        # Product.objects.bulk_create(objs, 100)


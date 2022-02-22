from itertools import islice

import pandas as pd
from django.core.management.base import BaseCommand

from apps.products.models import ActiveIngredient


class Command(BaseCommand):

    def handle(self, *args, **options):
        file = 'apps/products/management/principios_activos.xlsx'
        newdata = pd.read_excel(file).drop_duplicates()
        objs = [ActiveIngredient(name=i[0]) for i in newdata.values]
        ActiveIngredient.objects.bulk_create(objs, 100)


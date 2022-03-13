from itertools import islice

import pandas as pd
from django.core.management.base import BaseCommand

from apps.products.models import Formulation


class Command(BaseCommand):

    def handle(self, *args, **options):
        file = 'apps/products/management/formulacionesfinal.xlsx'
        newdata = pd.read_excel(file).drop_duplicates()
        # objs = [ActiveIngredient(name=i[0], symbol=[1]) for i in newdata.values]
        objs = []
        for line in newdata.values:
            objs.append(Formulation(symbol=line[0], name=line[1]))
        print(objs)
        # Formulation.objects.bulk_create(objs, 100)


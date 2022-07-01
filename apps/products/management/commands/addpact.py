from itertools import islice

import pandas as pd
from django.core.management.base import BaseCommand

from apps.products.models import ActiveIngredient


class Command(BaseCommand):

    def handle(self, *args, **options):
        # file = 'apps/products/management/productos.xlsx'
        # newdata = pd.read_excel(file)
        # # print(newdata.head())
        # arrobjt = newdata["2,4-D EQUIVALENTE ACIDO"].drop_duplicates()
        # cleanobjs = []
        # for i in arrobjt:
        #     if "+" in i:
        #         print("asd")
        #         a = []
        #         a = i.split('+')
        #         a[0].strip()
        #         a[0].strip()
        #         cleanobjs.append(a[0].strip())
        #         cleanobjs.append(a[1].strip())
        #         print(a[0], a[1])
        #     else:
        #         cleanobjs.append(i.strip())
        #
        # objs = [ActiveIngredient(name=str(i)) for i in set(cleanobjs)]
        # ActiveIngredient.objects.bulk_create(objs)

        print("HAcer cualquier cosa")

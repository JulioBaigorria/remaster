from django.core.management.base import BaseCommand
import pandas as pd
from apps.products.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # file = 'apps/products/management/formulados_2021.xlsx'
        # objs = []
        # try:
        #     newdata = pd.read_excel(file)
        #     print(newdata.head())
        #     dataframe = newdata.drop_duplicates(subset='Nº REG', keep="last")
        # except FileNotFoundError:
        #     print("alskdf")
        # for i in dataframe.values:
        #     i[7] = i[7].replace(",","")
        #     objs.append(Product(name=i[7], cod_senasa=i[6]))
        # Product.objects.bulk_create(objs, 100)

        # -------

        file = 'apps/products/management/productos.xlsx'
        objs = []
        try:
            newdata = pd.read_excel(file).drop_duplicates(subset=37966, keep="last")
        except FileNotFoundError:
            print("alskdf")
        for i in newdata.values:
            name = str(i[2])
            cod = str(i[10])
            objs.append(Product(name=name, cod_senasa=cod))
        print(objs)
        Product.objects.bulk_create(objs, 100)


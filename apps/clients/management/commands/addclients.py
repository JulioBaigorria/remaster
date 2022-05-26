import pandas as pd
from django.core.management.base import BaseCommand
from apps.clients.models import Client


class Command(BaseCommand):

    def handle(self, *args, **options):
        file = 'apps/clients/management/clients.xlsx'
        newdata = pd.read_excel(file)
        values = newdata.values.tolist()
        objs = [Client(name=str(i[0]), cuit=str(i[1])) for i in values]
        Client.objects.bulk_create(objs, 100)

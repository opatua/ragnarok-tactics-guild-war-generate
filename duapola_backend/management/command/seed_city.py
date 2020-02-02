from csv import reader
from os import path

from django.apps import apps
from django.core.management.base import BaseCommand

from pajak_core.models.city import City


class Command(BaseCommand):
    help = 'Seed Cities'

    def handle(self, *args, **options):
        self.stdout.write('Seeding: Cities')

        file = path.join(
            apps.get_app_config('pajak_core').path,
            'storage/web/city.csv'
        )

        with open(file) as csv_file:
            csv_reader = reader(csv_file)
            next(csv_reader)

            cities = []

            for row in csv_reader:
                row = [value.strip() for value in row]
                cities.append(
                    City(
                        id=row[0],
                        name=row[1]
                    )
                )

            City.objects.bulk_create(cities)

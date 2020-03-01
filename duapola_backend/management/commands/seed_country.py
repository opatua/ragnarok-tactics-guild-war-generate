from django.core.management.base import BaseCommand

from duapola_backend.models import Country


class Command(BaseCommand):
    help = 'Seed Countries'
    countries = {
        'ID': 'Indonesia',
        'MY': 'Malaysia',
        'TH': 'Thailand',
        'SG': 'Singapore',
    }

    def handle(self, *args, **options):
        self.stdout.write('Seeding: Countrie')

        for country_id, country_name in self.countries.items():
            Country.objects.create(
                id=country_id,
                name=country_name
            )

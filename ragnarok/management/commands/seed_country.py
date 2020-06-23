from django.core.management.base import BaseCommand

from ragnarok.models import Country


class Command(BaseCommand):
    help = 'Seed Countries'
    countries = {
        'ID': 'Indonesia',
        'MY': 'Malaysia',
        'TH': 'Thailand',
        'VN': 'Vietnam',
        'SG': 'Singapore',
        'PH': 'Philippines',
        'MM': 'Myanmar',
        'LA': 'Laos',
        'KH': 'Cambodia',
        'BN': 'Brunei',
        'TL': 'Timor-Leste',
    }

    def handle(self, *args, **options):
        self.stdout.write('Seeding: Countries')

        for country_id, country_name in self.countries.items():
            Country.objects.create(
                id=country_id,
                name=country_name
            )

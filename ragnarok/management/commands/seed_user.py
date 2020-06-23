from django.core.management.base import BaseCommand

from ragnarok.models import Country


class Command(BaseCommand):
    help = 'Seed Users'

    def handle(self, *args, **options):
        self.stdout.write('Seeding: Users')

        for country_id, country_name in self.countries.items():
            Country.objects.create(
                id=country_id,
                name=country_name
            )

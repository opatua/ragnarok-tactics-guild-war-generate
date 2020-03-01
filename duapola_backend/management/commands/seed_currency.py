from django.core.management.base import BaseCommand

from duapola_backend.models import Currency


class Command(BaseCommand):
    help = 'Seed Currencies'
    currencies = {
        'IDR': 'Indonesian Rupiah',
        'MYR': 'Malaysian Ringgit',
        'SGD': 'Singapore Dollar',
        'THB': 'Thailand Baht',
    }

    def handle(self, *args, **options):
        self.stdout.write('Seeding: Currencies')

        for currency_id, currency_name in self.currencies.items():
            Currency.objects.create(
                id=currency_id,
                name=currency_name,
                minor_unit=2
            )

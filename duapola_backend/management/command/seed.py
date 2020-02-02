from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed default data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding')

        call_command('seed_city')

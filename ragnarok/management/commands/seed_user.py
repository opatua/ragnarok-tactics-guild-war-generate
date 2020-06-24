from django.core.management.base import BaseCommand

from ragnarok.models import User


class Command(BaseCommand):
    help = 'Seed Users'

    def handle(self, *args, **options):
        self.stdout.write('Seeding: Users')

        for index in range(0, 31):
            User.objects.create_user(
                email=f'user_{index}@example.com',
                password='!QAZxsw2',
                name=f'user_{index}',
            )

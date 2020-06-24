from django.core.management.base import BaseCommand
from random import randint

from ragnarok.models import Character, User


class Command(BaseCommand):
    help = 'Seed Characters'

    def handle(self, *args, **options):
        self.stdout.write('Seeding: Characters')

        users = User.objects.filter(
            is_staff=False
        )

        for user in users:
            character = Character.objects.create(
                user_id=user.id,
                name=f'character_{user.email}',
                point=randint(2500, 5000),
            )

from django.core.management.base import BaseCommand
from random import randint

from ragnarok.models import Character, User, Team


class Command(BaseCommand):
    help = 'Seed Characters'

    def handle(self, *args, **options):
        self.stdout.write('Seeding: Characters')

        users = User.objects.filter(
            is_staff=False
        )

        for user_index, user in enumerate(users):
            character = Character.objects.create(
                user_id=user.id,
                name=f'character_{user.email}',
            )
            team = Team.objects.create(
                character_id=character.id,
                point=randint(2500, 5000),
            )
            if (len(users)-1) == user_index:
                for count in range(0, 2):
                    team = Team.objects.create(
                        character_id=character.id,
                        point=randint(2500, 5000),
                    )

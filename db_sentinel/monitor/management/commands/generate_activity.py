from django.core.management.base import BaseCommand
from monitor.models import UserActivity
import random
import time

class Command(BaseCommand):
    help = 'Generate fake user activity'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=100)
        parser.add_argument('--delay', type=float, default=0.0)

    def handle(self, *args, **kwargs):
        count = kwargs['count']
        delay = kwargs['delay']

        actions = ["login", "view", "click", "purchase"]

        self.stdout.write(f"Generating {count} activities...")

        for i in range(count):
            UserActivity.objects.create(
                user_id=random.randint(1, 100),
                action=random.choice(actions)
            )

            self.stdout.write(f"Created activity {i+1}/{count}")

            if delay > 0:
                time.sleep(delay)

        self.stdout.write(self.style.SUCCESS("Done generating activity ✅"))
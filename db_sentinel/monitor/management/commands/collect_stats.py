from django.core.management.base import BaseCommand
# from monitor.collector import collect_query_stats
from monitor.collector import collect_query_stats

class Command(BaseCommand):
    help = 'Collect PostgreSQL query stats'

    def handle(self, *args, **kwargs):
        collect_query_stats()
        self.stdout.write(self.style.SUCCESS('Stats collected successfully'))

from django.core.management.base import BaseCommand
from django.urls import get_resolver


class Command(BaseCommand):
    help = 'List all URL patterns'

    def handle(self, *args, **options):
        url_resolver = get_resolver()
        for pattern in url_resolver.url_patterns:
            self.stdout.write(str(pattern))

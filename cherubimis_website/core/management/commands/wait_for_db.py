"""
Django command to wait for the MySQL database to be available.
"""
import time

from django.db.utils import DEFAULT_DB_ALIAS, OperationalError
from django.core.management.base import BaseCommand
from django.db import connections


class Command(BaseCommand):
    """Django command to wait for MySQL database."""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                connections[DEFAULT_DB_ALIAS].cursor()
                db_up = True
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
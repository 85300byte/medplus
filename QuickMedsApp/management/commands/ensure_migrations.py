from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Ensures all migrations are applied and creates missing tables'

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            # Check if the table exists
            cursor.execute("""
                SELECT EXISTS (
                    SELECT FROM information_schema.tables 
                    WHERE table_schema = 'public'
                    AND table_name = 'QuickMedsApp_product'
                );
            """)
            table_exists = cursor.fetchone()[0]

            if not table_exists:
                self.stdout.write(self.style.WARNING('Product table does not exist. Running migrations...'))
                from django.core.management import call_command
                call_command('migrate', 'QuickMedsApp', interactive=False)
                self.stdout.write(self.style.SUCCESS('Migrations applied successfully'))
            else:
                self.stdout.write(self.style.SUCCESS('Product table exists')) 
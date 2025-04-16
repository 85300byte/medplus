from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from QuickMedsApp.models import UserProfile

class Command(BaseCommand):
    help = 'Creates UserProfile for all users who do not have one'

    def handle(self, *args, **options):
        users_without_profile = User.objects.filter(userprofile__isnull=True)
        count = 0
        
        for user in users_without_profile:
            UserProfile.objects.create(user=user)
            count += 1
            
        self.stdout.write(self.style.SUCCESS(f'Successfully created {count} UserProfile(s)')) 
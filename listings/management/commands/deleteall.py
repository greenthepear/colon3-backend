from django.core.management.base import BaseCommand, CommandError
from listings.models import Listing

class Command(BaseCommand):
    help = "Deletes all cat listings"
        
    def handle(self, *args, **options):
        l = Listing.objects.all()
        llen = len(l)
        l.delete()
        self.stdout.write(f"Number of cats deleted: {llen}")
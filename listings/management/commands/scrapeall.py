from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from listings.models import Listing, Source

def add_data() -> int:

    from . import _scrp_schronisko_lodz_pl
    from . import _scrp_ciapkowo_pl

    _scrp_ciapkowo_pl.scrape_ciapkowo_pl()
    
    allData = []
    allData.append(_scrp_schronisko_lodz_pl.scrape_schronisko_lodz_pl())
    added = 0
    for item in allData:
        for cat_dict in item:
            if Listing.objects.filter(listing_url=cat_dict["listing_url"]).count() == 0:
                cat_dict["added_date"] = timezone.now()
                cat_dict["source"] = Source.objects.filter(url=cat_dict["source"])
                
                Listing.objects.create(**cat_dict)

                added += 1

    return added

class Command(BaseCommand):
    help = "Adds all scraped data to database"
        
    def handle(self, *args, **options):
        added = add_data()
        self.stdout.write(f"Number of cats added: {added}")
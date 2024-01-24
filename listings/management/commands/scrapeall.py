from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from listings.models import Listing, Source

def add_data() -> int:

    from . import _scrp_schronisko_lodz_pl
    from . import _scrp_ciapkowo_pl
    from . import _scrp_napaluchu_waw_pl

    scrapers = [{"name":"schronisko-lodz.pl",
                 "func":_scrp_schronisko_lodz_pl.scrape_schronisko_lodz_pl},
                {"name":"ciapkowo.pl",
                 "func":_scrp_ciapkowo_pl.scrape_ciapkowo_pl},
                {"name":"napaluchu.waw.pl",
                 "func":_scrp_napaluchu_waw_pl.scrape_napaluchu_waw_pl}]
    
    allData = []
    for scrp in scrapers:
        print(f"Scraping {scrp['name']}...")
        tempData = []
        try:
            tempData = scrp['func']()
        except Exception as e:
            print(f"Exception while scraping {scrp['name']}: {e}\nskipping...")
            continue
        
    print(f"Found {len(tempData)} listings.")
    allData.append(tempData)

        
    added = 0
    for item in allData:
        for cat_dict in item:
            if Listing.objects.filter(listing_url=cat_dict["listing_url"]).count() == 0:
                
                src = Source.objects.filter(url=cat_dict["source"]).first()
                if src == None:
                    print("Listing trying to add nonexistent source: ",cat_dict["source"])
                    continue

                l = Listing(
                    listing_url = cat_dict["listing_url"],
                    cat_name = cat_dict["cat_name"],
                    source = src,
                    image_url = cat_dict["image_url"],
                    cat_age = cat_dict["cat_age"],
                    cat_sex = cat_dict["cat_sex"],
                    added_date = timezone.now(),
                )

                print(f"Adding: {l.cat_name} - {l.listing_url}")
                l.save()

                added += 1

    return added

class Command(BaseCommand):
    help = "Adds all scraped data to database"
        
    def handle(self, *args, **options):
        added = add_data()
        self.stdout.write(f"Number of cats added: {added}")
from django.core.management.base import BaseCommand, CommandError
from listings.models import Source

class Command(BaseCommand):
    help = "Initializes the sources"
    
    def handle(self, *args, **options):
        sources = [
            Source(
                url = "schronisko-lodz.pl",
                full_name = "Schronisko dla Zwierząt w Łodzi",
                city = "Łódź",
                address = "Marmurowa 4",
            ),
            Source(
                url = "ciapkowo.pl",
                full_name = "\"Ciapkowo\" Schronisko dla Bezdomnych Zwierząt w Gdyni",
                city = "Gdynia",
                address = "Małokacka 3A",
            ),
            Source(
                url = "napaluchu.waw.pl",
                full_name = "Schronisko dla Bezdomnych Zwierząt Na Paluchu",
                city = "Warszawa",
                address = "Paluch 2",
            ),
            Source(
                url = "schronisko-zwierzaki.lublin.pl",
                full_name = "Schronisko dla bezdomnych zwierząt w Lublinie",
                city = "Lublin",
                address = "Metalurgiczna 5",
            )]
        
        for s in sources:
            if Source.objects.filter(url=s.url).count() == 0:
                self.stdout.write(f"Adding source {s.url}...")
                s.save()
            else:
                self.stdout.write(f"Updating source {s.url}...")
                old_source = Source.objects.get(url=s.url)
                old_source.delete()
                s.save()

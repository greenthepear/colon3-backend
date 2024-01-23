from django.core.management.base import BaseCommand, CommandError
from listings.models import Source

class Command(BaseCommand):
    help = "Initializes the sources"
    
    def handle(self, *args, **options):
        Source.objects.create(
            url = "schronisko-lodz.pl",
            full_name = "Schronisko dla Zwierząt w Łodzi",
            city = "Łódź",
            address = "Marmurowa 4",
        )

        Source.objects.create(
            url = "ciapkowo.pl",
            full_name = "Schronisko dla Bezdomnych Zwierząt w Gdyni",
            city = "Gdynia",
            address = "Małokacka 3A",
        )
import json

from django.core.management.base import BaseCommand
from apps.common.models import Region, District
from core.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Load all regions'

    def handle(self, *args, **options):
        # Load all regions
        try:
            with open(str(BASE_DIR) + '/data/regions.json', 'r') as file:
                regions = json.load(file)
                country = Region.objects.get(name="O'zbekiston", code="UZ")
                for region in regions:
                    Region.objects.get_or_create(name=region['name_uz'], country=country)

                self.stdout.write(self.style.SUCCESS("All Regions are loaded successfully"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
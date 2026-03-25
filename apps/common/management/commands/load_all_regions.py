import json

from django.core.management.base import BaseCommand
from apps.common.models import Region, Country
from core.settings import BASE_DIR


class Command(BaseCommand):
    help = 'Load all regions'

    def handle(self, *args, **options):
        try:
            with open(str(BASE_DIR) + '/data/regions.json', encoding='utf-8-sig') as file:
                regions = json.load(file)
                country = Country.objects.get(name="Uzbekiston", code="UZ")
                for region in regions:
                    Region.objects.get_or_create(name=region['name_uz'], country=country)

                self.stdout.write(self.style.SUCCESS("All Regions are loaded successfully"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f'Error: {e}'))
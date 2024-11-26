from django.core.management.base import BaseCommand
from blog.models import CertificationLevel


class Command(BaseCommand):
    help = 'Populates default certification levels'

    def handle(self, *args, **kwargs):
        certification_levels = [
            (1, 'PADI Open Water Diver', 'Entry-level certification for recreational scuba diving'),
            (2, 'PADI Advanced Open Water Diver', 'Advanced recreational diving certification'),
            (3, 'PADI Rescue Diver', 'Emergency response and rescue techniques certification'),
            (4, 'PADI Divemaster', 'Professional-level diving leadership certification'),
            (5, 'PADI Instructor', 'Professional teaching certification'),
            (6, 'SSI Open Water Diver', 'SSI entry-level certification'),
            (7, 'SSI Advanced Open Water Diver', 'SSI advanced certification'),
            (8, 'BSAC Ocean Diver', 'BSAC entry-level certification'),
            (9, 'BSAC Sports Diver', 'BSAC advanced recreational certification'),
            (10, 'Technical Diving Certification', 'Specialized technical diving certification')
        ]

        for level_number, name, description in certification_levels:
            CertificationLevel.objects.get_or_create(
                name=name,
                defaults={
                    'description': description,
                    'level_number': level_number
                }
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created certification level: {name}')
            )

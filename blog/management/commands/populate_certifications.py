from django.core.management.base import BaseCommand
from blog.models import CertificationLevel


class Command(BaseCommand):
    help = 'Populates default certification levels'

    def handle(self, *args, **kwargs):
        certification_levels = [
            {
                'name': 'PADI Open Water Diver',
                'description': 'Entry-level certification for recreational scuba diving',
                'level_number': 1
            },
            {
                'name': 'PADI Advanced Open Water Diver',
                'description': 'Advanced recreational diving certification',
                'level_number': 2
            },
            {
                'name': 'PADI Rescue Diver',
                'description': 'Emergency response and rescue techniques certification',
                'level_number': 3
            },
            {
                'name': 'PADI Divemaster',
                'description': 'Professional-level diving leadership certification',
                'level_number': 4
            },
            {
                'name': 'PADI Instructor',
                'description': 'Professional teaching certification',
                'level_number': 5
            },
            {
                'name': 'SSI Open Water Diver',
                'description': 'SSI entry-level certification',
                'level_number': 6
            },
            {
                'name': 'SSI Advanced Open Water Diver',
                'description': 'SSI advanced certification',
                'level_number': 7
            },
            {
                'name': 'BSAC Ocean Diver',
                'description': 'BSAC entry-level certification',
                'level_number': 8
            },
            {
                'name': 'BSAC Sports Diver',
                'description': 'BSAC advanced recreational certification',
                'level_number': 9
            },
            {
                'name': 'Technical Diving Certification',
                'description': 'Specialized technical diving certification',
                'level_number': 10
            }
        ]

        for level in certification_levels:
            cert, created = CertificationLevel.objects.get_or_create(
                name=level['name'],
                defaults={
                    'description': level['description'],
                    'level_number': level['level_number']
                }
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Created certification level: {cert.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Certification level already exists: {cert.name}')
                )

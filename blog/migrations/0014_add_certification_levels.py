from django.db import migrations

def add_certification_levels(apps, schema_editor):
    CertificationLevel = apps.get_model('blog', 'CertificationLevel')
    
    levels = [
        {
            'name': 'Open Water Diver',
            'description': 'Entry-level certification for recreational scuba diving'
        },
        {
            'name': 'Advanced Open Water Diver',
            'description': 'Advanced certification with specialized dive training'
        },
        {
            'name': 'Rescue Diver',
            'description': 'Emergency response and rescue techniques certification'
        },
        {
            'name': 'Divemaster',
            'description': 'Professional-level certification for dive leadership'
        },
        {
            'name': 'Instructor',
            'description': 'Professional certification to teach scuba diving'
        }
    ]
    
    for level in levels:
        CertificationLevel.objects.create(**level)

def remove_certification_levels(apps, schema_editor):
    CertificationLevel = apps.get_model('blog', 'CertificationLevel')
    CertificationLevel.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('blog', '####_previous_migration'),  # Replace with your last migration
    ]

    operations = [
        migrations.RunPython(add_certification_levels, remove_certification_levels),
    ]
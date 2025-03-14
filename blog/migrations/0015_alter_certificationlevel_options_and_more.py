# Generated by Django 4.2.10 on 2024-11-26 18:13

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            'blog',
            '0014_certificationlevel_userprofile_created_on_and_more'
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='certificationlevel',
            options={'ordering': ['level_number']},
        ),
        migrations.AddField(
            model_name='certificationlevel',
            name='level_number',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='available_for_buddy',
            field=models.BooleanField(
                default=False,
                help_text='Available for buddy diving'
            ),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='certification_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='certification_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='diving_since',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='equipment_details',
            field=models.TextField(
                blank=True,
                help_text='List your diving equipment'
            ),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='max_depth_reached',
            field=models.PositiveIntegerField(
                default=0,
                help_text='Maximum depth reached in meters'
            ),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='own_equipment',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='preferred_diving_type',
            field=models.CharField(
                choices=[
                    ('recreational', 'Recreational Diving'),
                    ('technical', 'Technical Diving'),
                    ('cave', 'Cave Diving'),
                    ('wreck', 'Wreck Diving'),
                    ('night', 'Night Diving'),
                    ('photography', 'Photography Diving'),
                    ('conservation', 'Conservation Diving')
                ],
                default='recreational',
                max_length=100
            ),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(
                default='placeholder',
                max_length=255,
                verbose_name='image'
            ),
        ),
    ]

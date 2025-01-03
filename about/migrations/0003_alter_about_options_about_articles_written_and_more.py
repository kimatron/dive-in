# Generated by Django 4.2.10 on 2024-11-26 19:05

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_collaboraterequest'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AddField(
            model_name='about',
            name='articles_written',
            field=models.PositiveIntegerField(default=0, help_text='Number of diving articles published'),
        ),
        migrations.AddField(
            model_name='about',
            name='contact_email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='about',
            name='contact_phone',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='about',
            name='dive_locations',
            field=models.PositiveIntegerField(default=0, help_text='Number of dive locations covered'),
        ),
        migrations.AddField(
            model_name='about',
            name='hero_image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='about',
            name='hero_subtitle',
            field=models.TextField(blank=True, default='Discover the underwater world with our diving community', help_text='A brief tagline or introduction'),
        ),
        migrations.AddField(
            model_name='about',
            name='hero_title',
            field=models.CharField(blank=True, default='Explore the Depths with Us', max_length=200),
        ),
        migrations.AddField(
            model_name='about',
            name='location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='about',
            name='team_description',
            field=models.TextField(blank=True, default='', help_text='Description of our team'),
        ),
        migrations.AddField(
            model_name='about',
            name='total_divers',
            field=models.PositiveIntegerField(default=0, help_text='Number of divers in our community'),
        ),
        migrations.AddField(
            model_name='about',
            name='vision',
            field=models.TextField(blank=True, default='', help_text='Our vision for the diving community'),
        ),
    ]

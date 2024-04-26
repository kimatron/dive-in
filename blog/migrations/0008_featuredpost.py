# Generated by Django 5.0.4 on 2024-04-26 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_category_subscriber_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_featured', models.BooleanField(default=False)),
                ('post', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
    ]

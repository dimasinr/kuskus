# Generated by Django 4.2.7 on 2023-11-30 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thread', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='title',
            field=models.SlugField(blank=True, null=True),
        ),
    ]

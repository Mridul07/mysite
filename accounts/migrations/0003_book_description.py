# Generated by Django 3.1.5 on 2021-01-08 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_book_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]

# Generated by Django 4.1 on 2022-08-27 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookinfo', '0002_bookinfo_category_bookinfo_isbn_bookinfo_language_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookinfo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

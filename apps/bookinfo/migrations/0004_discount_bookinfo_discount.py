# Generated by Django 4.1 on 2022-08-27 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookinfo', '0003_bookinfo_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='DisCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_book', models.CharField(max_length=30)),
                ('new_price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='bookinfo',
            name='discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookinfo.discount'),
        ),
    ]

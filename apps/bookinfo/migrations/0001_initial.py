# Generated by Django 4.1 on 2022-08-26 11:52

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BookInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('price', models.IntegerField()),
                ('description', ckeditor.fields.RichTextField()),
                ('on_sale', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookinfo.author')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0)),
                ('book_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookinfo.bookinfo')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BookImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='books/')),
                ('book_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookinfo.bookinfo')),
            ],
        ),
        migrations.CreateModel(
            name='BookDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('type_of_lang', models.CharField(max_length=20)),
                ('translator', models.CharField(max_length=20)),
                ('num_of_pages', models.IntegerField()),
                ('press', models.CharField(max_length=20)),
                ('publish_date', models.DateField()),
                ('bookinfo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookinfo.bookinfo')),
            ],
        ),
    ]

# Generated by Django 4.2.1 on 2023-06-02 10:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme', models.CharField(max_length=255, verbose_name='Тема')),
                ('company', models.CharField(max_length=255, verbose_name='Компания')),
                ('duration', models.IntegerField(verbose_name='Длительность')),
                ('start_time', models.DateTimeField()),
                ('seats', models.IntegerField(default=0)),
                ('speakers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

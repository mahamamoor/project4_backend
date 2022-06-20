# Generated by Django 4.0.5 on 2022-06-14 18:48

from decimal import Decimal
import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=50)),
                ('image', models.TextField(default='')),
                ('price', models.IntegerField()),
                ('quantity', models.PositiveIntegerField(default=0))
            ],
        ),
    ]
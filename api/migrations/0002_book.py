# Generated by Django 3.1.4 on 2020-12-24 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookId', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('price', models.CharField(max_length=64)),
            ],
        ),
    ]

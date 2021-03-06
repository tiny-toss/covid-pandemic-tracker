# Generated by Django 3.1.1 on 2020-09-26 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('population', models.IntegerField()),
                ('deaths', models.IntegerField()),
                ('confirmed', models.IntegerField()),
                ('recovered', models.IntegerField()),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
    ]

# Generated by Django 3.1 on 2020-08-14 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=400, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('mobile', models.CharField(blank=True, max_length=400, null=True)),
                ('place', models.CharField(blank=True, max_length=400, null=True)),
                ('booking_message', models.CharField(blank=True, max_length=1000, null=True)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]

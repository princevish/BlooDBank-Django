# Generated by Django 2.2.5 on 2019-10-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191015_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='bloodbank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(blank=True, max_length=100)),
                ('district', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=300)),
            ],
        ),
    ]

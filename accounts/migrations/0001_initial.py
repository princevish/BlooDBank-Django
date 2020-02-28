# Generated by Django 2.2.5 on 2019-09-16 18:20

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
            name='ProfileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgroup', models.CharField(blank=True, max_length=100)),
                ('mobile', models.PositiveIntegerField(blank=True, default=None)),
                ('other_mobile', models.PositiveIntegerField(blank=True, default=None)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('zipcode', models.PositiveIntegerField(blank=True, default=None)),
                ('avilable', models.CharField(blank=True, max_length=100)),
                ('birthdate', models.PositiveIntegerField(blank=True, default=None)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'profile',
                'verbose_name_plural': 'profiles',
            },
        ),
    ]

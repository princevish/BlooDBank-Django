# Generated by Django 2.2.5 on 2019-10-14 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191014_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportdoner',
            name='fullname',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.ProfileModel'),
        ),
    ]

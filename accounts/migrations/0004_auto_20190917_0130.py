# Generated by Django 2.2.5 on 2019-09-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profilemodel_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='profile_pic',
            field=models.ImageField(default='default.jpg', upload_to='media/profile'),
        ),
    ]

# Generated by Django 2.2.5 on 2019-09-16 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190917_0014'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilemodel',
            name='profile_pic',
            field=models.ImageField(default='media/default.jpg', upload_to='media/profile'),
        ),
    ]
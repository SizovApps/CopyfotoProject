# Generated by Django 2.0.13 on 2019-10-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191023_1935'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]

# Generated by Django 2.0.13 on 2019-10-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]

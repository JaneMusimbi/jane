# Generated by Django 4.1 on 2022-10-02 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profile_picture',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

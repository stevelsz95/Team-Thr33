# Generated by Django 2.1.1 on 2018-12-18 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bridges', '0002_auto_20181218_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
# Generated by Django 2.0.7 on 2018-10-18 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='e.g. John Smith', max_length=200)),
                ('year', models.CharField(blank=True, help_text='What school year', max_length=10, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
            ],
        ),
    ]

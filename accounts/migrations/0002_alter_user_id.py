# Generated by Django 4.0 on 2021-12-15 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.PositiveIntegerField(default='30001031100861', primary_key=True, serialize=False, unique=True),
        ),
    ]

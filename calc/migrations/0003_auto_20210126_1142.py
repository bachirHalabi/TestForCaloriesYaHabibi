# Generated by Django 3.1.5 on 2021-01-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_auto_20210126_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calcfield',
            name='age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='calcfield',
            name='height',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='calcfield',
            name='weight',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-14 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocabulary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='russian_word',
            field=models.TextField(),
        ),
    ]

# Generated by Django 3.2.5 on 2021-09-10 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=120, verbose_name='bookTitle'),
        ),
    ]

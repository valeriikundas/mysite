# Generated by Django 2.0.5 on 2018-05-21 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180521_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]

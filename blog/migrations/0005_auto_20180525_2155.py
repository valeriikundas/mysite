# Generated by Django 2.0.5 on 2018-05-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180525_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date published'),
        ),
    ]

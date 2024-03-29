# Generated by Django 2.0.5 on 2018-05-21 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('author', models.CharField(max_length=100)),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='date created')),
                ('publication_date', models.DateTimeField(verbose_name='date published')),
                ('views_count', models.IntegerField()),
            ],
        ),
    ]

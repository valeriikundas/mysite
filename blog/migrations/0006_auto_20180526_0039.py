# Generated by Django 2.0.5 on 2018-05-25 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180525_2155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]

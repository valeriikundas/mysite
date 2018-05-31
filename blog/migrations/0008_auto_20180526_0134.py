# Generated by Django 2.0.5 on 2018-05-25 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180526_0107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('name',)},
        ),
        migrations.RemoveField(
            model_name='tag',
            name='post',
        ),
        migrations.AddField(
            model_name='tag',
            name='post',
            field=models.ManyToManyField(blank=True, null=True, to='blog.Post'),
        ),
    ]

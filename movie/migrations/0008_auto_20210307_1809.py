# Generated by Django 3.1.7 on 2021-03-07 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20210307_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(default='/placeholder.png', null=True, upload_to='movies/', verbose_name='Постер'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-24 06:25

from django.db import migrations, models
import recommendation.models


class Migration(migrations.Migration):

    dependencies = [
        ('recommendation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fooditem',
            name='restaurant',
            field=models.ForeignKey(default='', on_delete=recommendation.models.Restaurant, to='recommendation.restaurant'),
            preserve_default=False,
        ),
    ]
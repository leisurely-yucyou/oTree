# Generated by Django 2.2.12 on 2021-03-25 17:55

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('double_auction', '0004_auto_20210326_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='chosen_round',
            field=otree.db.models.IntegerField(default=1, null=True),
        ),
    ]

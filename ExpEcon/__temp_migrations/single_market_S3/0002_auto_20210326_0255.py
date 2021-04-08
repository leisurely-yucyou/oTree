# Generated by Django 2.2.12 on 2021-03-25 17:55

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('single_market_S3', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='hist_buyer',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='hist_buyer_highest_price',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='hist_buyer_payoff',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='hist_buyer_traded_num',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='hist_seller',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='hist_seller_lowest_price',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='hist_seller_payoff',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='hist_seller_traded_num',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='hist_total_payoff',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='hist_traded_price',
            field=otree.db.models.LongStringField(default='', null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='amount',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='buyer_first_highest_price',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='buyer_second_highest_price',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='first_traded_price',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='num_of_trading',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='payoff_1',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='payoff_2',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='roll',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='roll_base',
            field=otree.db.models.StringField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='second_traded_price',
            field=otree.db.models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='seller_first_lowest_price',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='player',
            name='seller_second_lowest_price',
            field=otree.db.models.IntegerField(default=0, null=True),
        ),
    ]

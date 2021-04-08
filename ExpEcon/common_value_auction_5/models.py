from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
from statistics import mean


author = 'Yushi Nagao'

doc = """
5人で行う共通価値オークション
"""


class Constants(BaseConstants):
    name_in_url = 'common_value_auction_S1'
    players_per_group = 5
    num_rounds = 2

    min_allowable_bid = 0
    max_allowable_bid = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    true_value = models.IntegerField(initial=0) # 油田の本当の価格の初期設定。0にしておく
    highest_value = models.IntegerField() # 最も高い指値の保存場所

    def set_winner(self):
        import random
        self.highest_value = max([p.bid for p in self.get_players()])
        self.true_value = round(mean([p.estimated_value for p in self.get_players()])) # 油田の本当の価格の計算
        highest_player_box = [
            p for p in self.get_players() if p.bid == self.highest_value
        ]
        print(self.true_value)

        highest_player = random.choice( # 最高価格を入札したグループが複数いた場合はランダムに勝者を決定
            highest_player_box
        )

        highest_player.is_winner = True
        for p in self.get_players(): # 各プレイヤーの利得を計算
            p.set_payoff()

    def set_estimated_value(self): # 各グループの事前調査の価格を設定
        import random
        for p in self.get_players():
            p.estimated_value = random.randrange(Constants.min_allowable_bid, Constants.max_allowable_bid, 1)

class Player(BasePlayer):
    estimated_value = models.IntegerField() # 事前調査の価格の保存場所
    bid = models.IntegerField( # 入札価格
        min=Constants.min_allowable_bid,
        max=Constants.max_allowable_bid,
        label = "入札額",
    )
    bid_reason = models.LongStringField(
        label = "入札額の理由"
    )

    forecast_value = models.IntegerField( # 予測価格
        min=Constants.min_allowable_bid,
        label = "予測値",
    )
    forecast_reason = models.LongStringField(
        label="予測値の理由"
    )

    is_winner = models.BooleanField(
        initial=False, doc="""Indicates whether the player is the winner"""
    )

    utility = models.IntegerField()

    def set_payoff(self):
        if self.is_winner:
            self.utility = self.group.true_value - self.bid
        else:
            self.utility = 0

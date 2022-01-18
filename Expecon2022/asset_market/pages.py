from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import numpy as np #サイコロを実装するのにnumpyが必要


class Instruction(Page):
    # timeout_seconds = 480 #ページの時間制限
    def is_displayed(self): #ラウンド一回目の時だけ表示
        return self.subsession.round_number == 1

class ResultsWaitPage(WaitPage):
    pass

class Game(Page):
    timeout_seconds = 180 #ページの時間制限
    live_method = 'live_auction' #models.pyにあるlive_auctionという関数を呼び出す
    def vars_for_template(self):
        if self.subsession.round_number == 1:
            self.group.total_survive_stock = 6 * len(self.group.get_players())
        #ラウンド2以降では前のラウンドのお金と株式を引き継ぐように設定．これをしないとデータが引き継がれない
        if self.subsession.round_number > 1:
            self.player.money = self.player.in_round(self.subsession.round_number - 1).money
            self.player.num_stocks = self.player.in_round(self.subsession.round_number - 1).num_stocks

            self.group.total_bunkruptcy = self.group.in_round(self.subsession.round_number - 1).total_bunkruptcy
            self.group.total_survive_stock = 0
            for p in  self.group.get_players():
                self.group.total_survive_stock = self.group.total_survive_stock + p.in_round(self.subsession.round_number - 1).num_stocks

    def before_next_page(self):
        print(Constants.price_box)
        if len(Constants.price_box) == 0:
            self.group.average_of_traded_price = None
        else:
            self.group.average_of_traded_price = float(sum([d for d in Constants.price_box.values()]))/len(Constants.price_box)
            print(self.group.average_of_traded_price)

        if not(self.group.traded_or_not):
            Constants.price_box.clear()

class Game_Result(Page):
    timeout_seconds = 30 #ページの時間制限
    def before_next_page(self): #次のページに行く前に次のページで必要になる処理をしておく
        self.player.dividend = 100*self.player.num_stocks #配当金の計算
        self.player.money += self.player.dividend #配当金を加算した所持金


class Dividend(Page):
    timeout_seconds = 30 #ページの時間制限
    def before_next_page(self): #次のページに行く前の処理
        dice_arr = np.random.randint(1, 7, self.player.num_stocks).tolist()
        #一様乱数を用いてサイコロを再現．所有株式の数だけ乱数を出現させる
        j = 0
        for i in dice_arr: #HTMLにサイコロの出目を表示させるための前処理
            if j < len(dice_arr) - 1:
                self.player.dice_box += str(i) + ','
            elif j == len(dice_arr) - 1: #末尾に無駄に「,」が入るのが嫌だから条件分け
                self.player.dice_box += str(i)
            j += 1

        self.player.num_bunkruptcy = dice_arr.count(1) #倒産した会社の数は1の数
        self.player.num_stocks -= self.player.num_bunkruptcy #所有株式から倒産した会社の数を引く


class Bunkruptcy(Page):
    timeout_seconds = 30 #ページの時間制限
    # def is_displayed(self): #倒産は最終ラウンド以外で表示されるように設定
    def before_next_page(self):
        if self.subsession.round_number == Constants.num_rounds:
            #最終ラウンドでは買戻しによる処理を行う
            self.player.stock_return = self.player.num_stocks*600 #一株につき600円の買戻し
            self.player.money += self.player.stock_return #所持金に買戻しの額を加算しておく


class Breakout(Page):
    timeout_seconds = 60
    def is_displayed(self):
        return self.subsession.round_number < Constants.num_rounds

    def vars_for_template(self):
        if self.subsession.round_number == 1:
            self.group.total_bunkruptcy = 0
            self.group.total_survive_stock = 0
            for p in  self.group.get_players():
                self.group.total_bunkruptcy = self.group.total_bunkruptcy + p.num_bunkruptcy
                self.group.total_survive_stock = self.group.total_survive_stock + p.num_stocks
        else:
            self.group.total_bunkruptcy = self.group.in_round(self.subsession.round_number - 1).total_bunkruptcy
            self.group.total_survive_stock = 0
            for p in  self.group.get_players():
                self.group.total_bunkruptcy = self.group.total_bunkruptcy + p.num_bunkruptcy
                self.group.total_survive_stock = self.group.total_survive_stock + p.num_stocks

class Waitpage(WaitPage):
    def after_all_players_arrive(self): #全ての被験者が着くのを待つ
        pass

class Return(Page):
    timeout_seconds = 30 #ページの時間制限
    def is_displayed(self): #買戻しのページは最終ラウンドのみ表示
        return self.subsession.round_number == Constants.num_rounds

class End(Page):
    def is_displayed(self): #実験が終わったことを知らせるページは最終ラウンドの後にのみ表示
        return self.subsession.round_number == Constants.num_rounds

    def js_vars(self):
        lank_list = {}
        for p in self.group.get_players():
            lank_list[p.id_in_group] = p.money
            print(lank_list)
        return dict(lank_list=lank_list)

page_sequence = [Instruction,Waitpage, Game, Game_Result, Dividend, Bunkruptcy, Breakout, Return, End]

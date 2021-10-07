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



class Constants(BaseConstants):
    name_in_url = 'stock_trade'

    players_per_group = None #1グループの人数設定
    num_rounds = 10          #ラウンド数

    bids = {} #売り値の処理に使うdictionary
    asks = {} #買い値の処理に使うdictionary
    price_box={}

class Subsession(BaseSubsession):
    num_of_trade = models.IntegerField(initial=0)

    def js_vars(self):
        ave_prices = list([g.in_round(i).average_of_traded_price for i in range(1,Constants.num_rounds+1)] for g in self.get_groups())
        ave_prices_l = [float(ave_prices[0][i]) for i in range(Constants.num_rounds)]
        return dict(ave_prices=ave_prices_l)

class Group(BaseGroup):
    def example(self):
        self
        self.get_players()
    lowest_bidder = models.IntegerField() #最も低い売り値を入札した人の番号を保存
    lowest_bid = models.CurrencyField(initial=10000000) #最も低い売り値を記録，初期値は適当にありえない額面を設定
    highest_asker = models.IntegerField() #最も高い買い値を入札した人の番号を保存
    highest_ask = models.CurrencyField(initial=0) #最も高い買い値を記録.初期値として0を入れておく
    traded_or_not = models.BooleanField(initial=False) #取引が行われた場合にはTrueそうでないならFalseを返す．取引の有無で文章の表示変えるために必要.
    history_of_traded_price = models.LongStringField(initial='')
    history_of_traded_bidder = models.LongStringField(initial='')
    history_of_traded_asker = models.LongStringField(initial='')
    average_of_traded_price = models.CurrencyField()
    total_bunkruptcy = models.IntegerField(initial=0)
    total_survive_stock = models.IntegerField(initial=0)
    num_of_trade = models.IntegerField(initial=0)

class Player(BasePlayer):
    money = models.CurrencyField(initial=4000) #初期保有金額は4000
    num_stocks = models.IntegerField(initial=6) #初期保有株式は6枚
    dividend = models.IntegerField() #配当金を記録
    num_bunkruptcy= models.IntegerField() #倒産会社数を記録
    dice_box = models.LongStringField(initial='') #サイコロの出目を表示するのに必要
    stock_return = models.IntegerField() #買戻し金額の記録


    def live_auction(self, data):
        #HTMLから渡されたデータを処理する為の関数
        #リアルタイム取引で必要な処理を定義していく
        group = self.group #notationを軽くするための処理
        my_id = self.id_in_group #上に同じ
        num_of_trade = self.subsession.num_of_trade
        t = data['type'] #上に同じ
        if t == 'bid': #HTMLから渡されたデータのtypeが売り値の時の処理
            bid = data['value'] #notationを軽くするための処理
            if  self.num_stocks < 1: #株式を持っていないのに売ろうとしたときの処理
                response = dict(type='not_stock')
                return {my_id: response}

            elif my_id == group.highest_asker:
                response = dict(type='you_are_top_asker')
                return {my_id: response}

            elif bid < group.lowest_bid: #売り値が現在の最低売り値より低い時の処理
                group.lowest_bid = bid #最低売り値額を更新しておく
                group.lowest_bidder = my_id #最低売り値入札者を更新しておく
                Constants.bids[my_id] = bid #最も低い売り値を格納していく
                response = dict(type='bid',id_in_group=my_id, bid=bid) #HTMLに返す変数をそれぞれ格納

                if my_id == group.highest_asker:
                    response = dict(type='you_are_top_asker')
                    return {my_id: response}

                elif bid <= group.highest_ask: #取引成立した時
                    num_of_trade += 1
                    group.traded_or_not = True #取引が成立した場合の文章を表示させるためにTrueにしておく
                    traded_asker = group.highest_asker
                    traded_price = group.highest_ask
                    traded_bidder = my_id
                    group.history_of_traded_bidder += str(my_id) +','
                    group.history_of_traded_asker += str(group.highest_asker)+','
                    group.history_of_traded_price +=str(traded_price)+','
                    Constants.price_box[len(group.history_of_traded_price)]=traded_price
                    for p in group.get_players(): #各被験者の株式と所持金についての処理
                        if self.round_number == 1: #ラウンド一回目の場合に処理は単純に株式と所持金に加減すればいい
                            if p.id_in_group == group.lowest_bidder: #取引に成功した売り手の処理
                                p.money = p.money + traded_price
                                p.num_stocks -= 1
                            elif p.id_in_group == group.highest_asker: #取引に成功した買い手の処理
                                p.money = p.money - traded_price
                                p.num_stocks += 1
                        elif self.round_number > 1 and num_of_trade==0 : #ラウンド2回目以降は計算するにあたって所有株と所持金は前のラウンドの値を呼び出して処理する必要がある
                            if p.id_in_group == group.lowest_bidder: #売り手の処理
                                p.money = p.in_round(self.round_number - 1).money + traded_price
                                p.num_stocks -= 1
                            elif p.id_in_group == group.highest_asker: #買い手の処理
                                p.money = p.in_round(self.round_number - 1).money - traded_price
                                p.num_stocks += 1
                            else: #それ以外の人の処理
                                p.money = p.in_round(self.round_number - 1).money
                        elif self.round_number > 1 and num_of_trade > 0:
                            if p.id_in_group == group.lowest_bidder: #取引に成功した売り手の処理
                                p.money = p.money + traded_price
                                p.num_stocks -= 1
                            elif p.id_in_group == group.highest_asker: #取引に成功した買い手の処理
                                p.money = p.money - traded_price
                                p.num_stocks += 1

                    response_to_all = dict(
                        type='trade_success',
                        top_bidder = group.lowest_bidder,
                        top_asker = group.highest_asker,
                        traded_price=traded_price,
                        top_bidder_money = group.get_player_by_id(group.lowest_bidder).money,
                        top_asker_money =group.get_player_by_id(group.highest_asker).money,
                        top_bidder_stocks = group.get_player_by_id(group.lowest_bidder).num_stocks,
                        top_asker_stocks = group.get_player_by_id(group.highest_asker).num_stocks
                    )

                    group.lowest_bid = 10000000
                    group.lowest_bidder = None
                    group.highest_ask = 0
                    group.highest_asker = None
                    bids = {}
                    asks = {}

                    return {0: response_to_all}

                return {0: response} #処理したデータをHTMLに送り返す


        elif t == 'ask': #HTMLから受けとったデータのタイプが買い値の時の処理．基本的には売り値の時の逆
            ask = data['value'] #notationを軽くするための処理

            if ask > self.money: #買い値が所持金より高い場合の処理
                response = dict(type='no_money')
                print('kiteruyo')
                return {my_id: response}

            elif my_id == group.lowest_bidder:
                response = dict(type='you_are_top_bidder')
                return {my_id: response}

            elif ask > group.highest_ask: #買い値が更新された時の処理
                group.highest_ask = ask #買い値を更新しておく
                group.highest_asker = my_id #買い手を更新しておく
                Constants.asks[my_id] = ask #買い値を記録しておく
                response = dict(type='ask',id_in_group=my_id, ask=ask) #HTMLに返す変数をそれぞれ格納

                if my_id == group.lowest_bidder:
                    response = dict(type='you_are_top_bidder')
                    return {my_id: response}

                elif ask >= group.lowest_bid: #取引成立した時
                    num_of_trade += 1
                    group.traded_or_not = True #次のページの文章を変更する為に取引成立をTrueにしておく
                    traded_bidder = group.lowest_bidder
                    traded_asker = my_id
                    traded_price = group.lowest_bid
                    group.history_of_traded_bidder += str(group.lowest_bidder)+','
                    group.history_of_traded_asker += str(my_id)+','
                    group.history_of_traded_price +=str(traded_price)+','
                    Constants.price_box[len(group.history_of_traded_price)]=traded_price
                    for p in group.get_players():
                        if self.round_number == 1:
                            if p.id_in_group == group.lowest_bidder:
                                p.money = p.money + traded_price
                                p.num_stocks -= 1
                            elif p.id_in_group == group.highest_asker:
                                p.money = p.money - traded_price
                                p.num_stocks += 1
                        elif self.round_number > 1 and num_of_trade==0 :
                            if p.id_in_group == group.lowest_bidder:
                                p.money = p.in_round(self.round_number - 1).money + traded_price
                                p.num_stocks -= 1
                            elif p.id_in_group == group.highest_asker:
                                p.money = p.in_round(self.round_number - 1).money - traded_price
                                p.num_stocks += 1
                            else:
                                p.money = p.in_round(self.round_number - 1).money
                        elif self.round_number > 1 and num_of_trade > 0:
                            if p.id_in_group == group.lowest_bidder: #取引に成功した売り手の処理
                                p.money = p.money + traded_price
                                p.num_stocks -= 1
                            elif p.id_in_group == group.highest_asker: #取引に成功した買い手の処理
                                p.money = p.money - traded_price
                                p.num_stocks += 1

                    response_to_all = dict(
                        type='trade_success',
                        top_bidder = group.lowest_bidder,
                        top_asker = group.highest_asker,
                        traded_price=traded_price,
                        top_bidder_money = group.get_player_by_id(group.lowest_bidder).money,
                        top_asker_money =group.get_player_by_id(group.highest_asker).money,
                        top_bidder_stocks = group.get_player_by_id(group.lowest_bidder).num_stocks,
                        top_asker_stocks = group.get_player_by_id(group.highest_asker).num_stocks
                    )

                    group.lowest_bid = 10000000
                    group.lowest_bidder = None
                    group.highest_ask = 0
                    group.highest_asker = None
                    bids = {}
                    asks = {}

                    return {0: response_to_all}
                return {0: response}

        elif t == 'bid_accept': #売り値が承諾された時の処理
            if group.get_player_by_id(my_id).money < group.lowest_bid:
                response = dict(type='no_money')
                return {my_id: response}
            elif my_id != group.lowest_bidder: #承諾した被験者と売り手のIDが違うことをチェック，同じなら処理は行わない
                num_of_trade += 1
                group.traded_or_not = True #取引成立をTrueにしておく
                group.highest_ask = group.lowest_bid #買い値最高額を取引額に更新
                group.highest_asker = my_id #最高額の買い手を承諾を押した被験者に更新
                traded_asker = my_id
                traded_bidder = group.lowest_bidder
                traded_price = group.lowest_bid
                group.history_of_traded_bidder += str(group.lowest_bidder)+','
                group.history_of_traded_asker += str(my_id)+','
                group.history_of_traded_price +=str(traded_price)+','
                Constants.price_box[len(group.history_of_traded_price)]=traded_price
                for p in group.get_players():
                    if self.round_number == 1:
                        if p.id_in_group == group.lowest_bidder:
                            p.money = p.money + traded_price
                            p.num_stocks -= 1
                        elif p.id_in_group == group.highest_asker:
                            p.money = p.money - traded_price
                            p.num_stocks += 1
                    elif self.round_number > 1 and num_of_trade==0 :
                        if p.id_in_group == group.lowest_bidder:
                            p.money = p.in_round(self.round_number - 1).money + traded_price
                            p.num_stocks -= 1
                        elif p.id_in_group == group.highest_asker:
                            p.money = p.in_round(self.round_number - 1).money - traded_price
                            p.num_stocks += 1
                        else:
                            p.money = p.in_round(self.round_number - 1).money
                    elif self.round_number > 1 and num_of_trade > 0:
                        if p.id_in_group == group.lowest_bidder: #取引に成功した売り手の処理
                            p.money = p.money + traded_price
                            p.num_stocks -= 1
                        elif p.id_in_group == group.highest_asker: #取引に成功した買い手の処理
                            p.money = p.money - traded_price
                            p.num_stocks += 1

                response_to_all = dict(
                    type='trade_success',
                    top_bidder = group.lowest_bidder,
                    top_asker = group.highest_asker,
                    traded_price=traded_price,
                    top_bidder_money = group.get_player_by_id(group.lowest_bidder).money,
                    top_asker_money =group.get_player_by_id(group.highest_asker).money,
                    top_bidder_stocks = group.get_player_by_id(group.lowest_bidder).num_stocks,
                    top_asker_stocks = group.get_player_by_id(group.highest_asker).num_stocks
                )

                group.lowest_bid = 10000000
                group.lowest_bidder = None
                group.highest_ask = 0
                group.highest_asker = None
                bids = {}
                asks = {}

                return {0: response_to_all}

        elif t== 'ask_accept': #買い値が承諾された時の処理，基本的に売り値が承諾された時と同じ処理を行う
            if group.get_player_by_id(my_id).num_stocks < 1:
                response = dict(type='not_stock')
                return {my_id: response}
            elif my_id != group.highest_asker:
                num_of_trade += 1
                group.lowest_bidder=my_id
                group.lowest_bid=group.highest_ask
                group.traded_or_not = True
                traded_price = group.highest_ask
                traded_bidder = my_id
                traded_asker = group.highest_asker
                group.history_of_traded_bidder += str(my_id)+','
                group.history_of_traded_asker += str(group.highest_asker)+','
                group.history_of_traded_price += str(traded_price)+','
                Constants.price_box[len(group.history_of_traded_price)]=traded_price
                for p in group.get_players(): #各被験者の株式と所持金についての処理
                    if self.round_number == 1: #ラウンド一回目の場合に処理は単純に株式と所持金に加減すればいい
                        if p.id_in_group == group.lowest_bidder: #取引に成功した売り手の処理
                            p.money = p.money + traded_price
                            p.num_stocks -= 1
                        elif p.id_in_group == group.highest_asker: #取引に成功した買い手の処理
                            p.money = p.money - traded_price
                            p.num_stocks += 1
                    elif self.round_number > 1 and num_of_trade==0 : #ラウンド2回目以降は計算するにあたって所有株と所持金は前のラウンドの値を呼び出して処理する必要がある
                        if p.id_in_group == group.lowest_bidder: #売り手の処理
                            p.money = p.in_round(self.round_number - 1).money + traded_price
                            p.num_stocks -= 1
                        elif p.id_in_group == group.highest_asker: #買い手の処理
                            p.money = p.in_round(self.round_number - 1).money - traded_price
                            p.num_stocks += 1
                        else: #それ以外の人の処理
                            p.money = p.in_round(self.round_number - 1).money
                    elif self.round_number > 1 and num_of_trade > 0:
                        if p.id_in_group == group.lowest_bidder: #取引に成功した売り手の処理
                            p.money = p.money + traded_price
                            p.num_stocks -= 1
                        elif p.id_in_group == group.highest_asker: #取引に成功した買い手の処理
                            p.money = p.money - traded_price
                            p.num_stocks += 1

                response_to_all = dict(
                    type='trade_success',
                    top_bidder = group.lowest_bidder,
                    top_asker = group.highest_asker,
                    traded_price=traded_price,
                    top_bidder_money = group.get_player_by_id(group.lowest_bidder).money,
                    top_asker_money =group.get_player_by_id(group.highest_asker).money,
                    top_bidder_stocks = group.get_player_by_id(group.lowest_bidder).num_stocks,
                    top_asker_stocks = group.get_player_by_id(group.highest_asker).num_stocks
                )

                group.lowest_bid = 10000000
                group.lowest_bidder = None
                group.highest_ask = 0
                group.highest_asker = None
                bids = {}
                asks = {}

                return {0: response_to_all}

            return {0: response}

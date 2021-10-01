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

import numpy as np


author = 'Yushi Nagao'

doc = """ """


class Constants(BaseConstants):
    name_in_url = 'session_3'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    hist_traded_price = models.LongStringField(initial='')
    hist_total_payoff = models.LongStringField(initial='')

    hist_seller = models.LongStringField(initial='')
    hist_seller_lowest_price = models.LongStringField(initial='')
    hist_seller_payoff = models.LongStringField(initial='')
    hist_seller_traded_num = models.LongStringField(initial='')

    hist_buyer = models.LongStringField(initial='')
    hist_buyer_highest_price = models.LongStringField(initial='')
    hist_buyer_payoff = models.LongStringField(initial='')
    hist_buyer_traded_num = models.LongStringField(initial='')

    def allotment(self):
        for p in self.get_players():
            p.allot_role()
            if p.roll == 'seller_1_3':
                p.amount = 2
                p.seller_first_lowest_price = 100
                p.seller_second_lowest_price = 160
            elif p.roll == 'seller_4':
                p.amount = 2
                p.seller_first_lowest_price = 110
                p.seller_second_lowest_price = 160
            elif p.roll == 'seller_5_6':
                p.amount = 2
                p.seller_first_lowest_price = 110
                p.seller_second_lowest_price = 150
            elif p.roll == 'seller_7_8':
                p.amount = 2
                p.seller_first_lowest_price = 125
                p.seller_second_lowest_price = 130
            elif p.roll == 'seller_9':
                p.amount = 2
                p.seller_first_lowest_price = 125
                p.seller_second_lowest_price = 150
            elif p.roll == 'seller_10':
                p.amount = 2
                p.seller_first_lowest_price = 130
                p.seller_second_lowest_price = 150

            elif p.roll == 'buyer_1_3':
                p.amount = 0
                p.buyer_first_highest_price = 170
                p.buyer_second_highest_price = 110
            elif p.roll == 'buyer_4':
                p.amount = 0
                p.buyer_first_highest_price = 160
                p.buyer_second_highest_price = 110
            elif p.roll == 'buyer_5_6':
                p.amount = 0
                p.buyer_first_highest_price = 160
                p.buyer_second_highest_price = 120
            elif p.roll == 'buyer_7_8':
                p.amount = 0
                p.buyer_first_highest_price = 145
                p.buyer_second_highest_price = 140
            elif p.roll == 'buyer_9':
                p.amount = 0
                p.buyer_first_highest_price = 145
                p.buyer_second_highest_price = 120
            elif p.roll == 'buyer_10':
                p.amount = 0
                p.buyer_first_highest_price = 140
                p.buyer_second_highest_price = 120





class Player(BasePlayer):
    amount = models.IntegerField(initial=0)

    buyer_first_highest_price = models.IntegerField(initial=0)
    buyer_second_highest_price = models.IntegerField(initial=0)

    seller_first_lowest_price = models.IntegerField(initial=0)
    seller_second_lowest_price = models.IntegerField(initial=0)

    payoff_1 = models.IntegerField(initial=0)
    payoff_2 = models.IntegerField(initial=0)
    first_traded_price = models.IntegerField(initial=None)
    second_traded_price = models.IntegerField(initial=None)
    num_of_trading = models.IntegerField(initial=0)
    roll = models.StringField()
    roll_base = models.StringField()

    def allot_role(self):
        # if self.id_in_group == 1:
        #     self.roll_base = 'buyer'
        #     self.roll = 'buyer_9'
        # elif self.id_in_group == 2:
        #     self.roll_base = 'seller'
        #     self.roll = 'seller_10'
        # elif self.id_in_group == 3:
        #     self.roll_base = 'buyer'
        #     self.roll = 'buyer_10'
        if self.id_in_group <= 10: #seller
            self.roll_base = 'seller'
            if self.id_in_group <= 3:
                self.roll = 'seller_1_3'
            elif self.id_in_group == 4:
                self.roll = 'seller_4'
            elif self.id_in_group >= 5 and self.id_in_group <= 6:
                self.roll = 'seller_5_6'
            elif self.id_in_group >= 7 and self.id_in_group <= 8:
                self.roll = 'seller_7_8'
            elif self.id_in_group == 9:
                self.roll = 'seller_9'
            else:
                self.roll = 'seller_10'

        elif self.id_in_group > 10: #buyer
            self.roll_base = 'buyer'
            if self.id_in_group <= 13:
                self.roll = 'buyer_1_3'
            elif self.id_in_group == 14:
                self.roll = 'buyer_4'
            elif self.id_in_group >= 15 and self.id_in_group <= 16:
                self.roll = 'buyer_5_6'
            elif self.id_in_group >= 17 and self.id_in_group <= 18:
                self.roll = 'buyer_7_8'
            elif self.id_in_group == 19:
                self.roll = 'buyer_9'
            else:
                self.roll = 'buyer_10'

    def live_auction(self, data):
        group = self.group
        type = data['type']

        if type == 'sell':
            id_in_group = self.id_in_group
            price = data['price']
            print(price)
            if self.num_of_trading == 2:
                response = dict(
                    type = 'trade_enough'
                )
                return {id_in_group: response}
            elif price == None or price <= 0:
                response = dict(
                    type = 'not_input'
                )
                return {id_in_group: response}
            elif self.num_of_trading == 0:
                if price < self.seller_first_lowest_price:
                    response = dict(type='lower_price')
                    return {id_in_group: response}
                else:
                    response = dict(
                        type = 'sell',
                        id_in_group = id_in_group,
                        price = price
                    )
                    return {0: response}
            elif self.num_of_trading == 1:
                if price < self.seller_second_lowest_price:
                    response = dict(type='lower_price')
                    return {seller: response}
                else:
                    response = dict(
                        type = 'sell',
                        id_in_group = id_in_group,
                        price = price
                    )
                    return {0: response}

        elif type == 'buy':
            id_in_group = self.id_in_group
            price = data['price']
            if self.num_of_trading == 2:
                response = dict(
                    type = 'trade_enough'
                )
                return {id_in_group: response}
            elif price == None or price <= 0:
                response = dict(
                    type = 'not_input'
                )
                return {id_in_group: response}
            elif self.num_of_trading == 0:
                if price + 40 > self.buyer_first_highest_price:
                    response = dict(type='higher_price')
                    return {id_in_group: response}
                else:
                    response = dict(
                        type = 'buy',
                        id_in_group = id_in_group,
                        price = price
                    )
                    return {0: response}
            elif self.num_of_trading == 1:
                if price + 40 > self.buyer_second_highest_price:
                    response = dict(type='higher_price')
                    return {seller: response}
                else:
                    response = dict(
                        type = 'buy',
                        id_in_group = id_in_group,
                        price = price
                    )
                    return {0: response}

        elif type == 'sell_cancel':
            print('kiteruyo')
            id_in_group = self.id_in_group
            response = dict(
                type = 'sell_cancel',
                id_in_group = id_in_group
            )
            return {0: response}

        elif type == 'buy_cancel':
            id_in_group = self.id_in_group
            response = dict(
                type = 'buy_cancel',
                id_in_group = id_in_group
            )
            return {0: response}

        elif type == 'sell_accept':
            seller = data['seller']
            buyer = self.id_in_group
            price = data['price']
            print(self.buyer_first_highest_price, price, self.num_of_trading)
            if self.num_of_trading >= 2: #買い手の取引が2回行われていた時
                response = dict(
                    type = 'trade_enough'
                )
                return {self.id_in_group: response}
            elif self.num_of_trading == 0: #買い手の取引一回目
                print('kiteruttay')
                if self.buyer_first_highest_price < price + 40: #買い手の許容価格より価格が高い時
                    response = dict(type='higher_price')
                    return {buyer: response}
                else: #取引成立
                    group.hist_traded_price += str(price) + ','

                    group.get_player_by_id(buyer).amount += 1
                    group.get_player_by_id(buyer).num_of_trading += 1
                    group.get_player_by_id(buyer).first_traded_price = price
                    group.get_player_by_id(buyer).payoff_1 = group.get_player_by_id(buyer).buyer_first_highest_price - price - 40
                    group.hist_buyer += str(buyer) + ','
                    group.hist_buyer_highest_price += str(group.get_player_by_id(buyer).buyer_first_highest_price) + ','
                    group.hist_buyer_payoff += str(group.get_player_by_id(buyer).payoff_1) + ','
                    group.hist_buyer_traded_num += str(group.get_player_by_id(buyer).num_of_trading) + ','

                    group.get_player_by_id(seller).amount -= 1
                    group.hist_seller += str(seller) + ','
                    if group.get_player_by_id(seller).num_of_trading == 0: #売り手の取引回数が一回目の時
                        group.get_player_by_id(seller).num_of_trading += 1
                        group.get_player_by_id(seller).first_traded_price = price
                        group.get_player_by_id(seller).payoff_1 = price - group.get_player_by_id(seller).seller_first_lowest_price
                        group.hist_seller_payoff += str(group.get_player_by_id(seller).payoff_1) + ','
                        group.hist_seller_lowest_price += str(group.get_player_by_id(seller).seller_first_lowest_price) + ','
                        group.hist_seller_traded_num += str(group.get_player_by_id(seller).num_of_trading) + ','

                        response = dict(
                            type = 'sell_accept', #s_1_b_1
                            seller = seller,
                            buyer = buyer,
                            price = price,
                            seller_num_of_trade = 1,
                            buyer_num_of_trade = 1,
                            seller_payoff = group.get_player_by_id(seller).payoff_1,
                            buyer_payoff = group.get_player_by_id(buyer).payoff_1
                        )
                        return {0: response}

                    elif group.get_player_by_id(seller).num_of_trading == 1: #売り手の取引回数が二回目の時
                        group.get_player_by_id(seller).num_of_trading += 1
                        group.get_player_by_id(seller).second_traded_price = price
                        group.get_player_by_id(seller).payoff_2 = price - group.get_player_by_id(seller).seller_second_lowest_price
                        group.hist_seller_payoff += str(group.get_player_by_id(seller).payoff_2) + ','
                        group.hist_seller_lowest_price += str(group.get_player_by_id(seller).seller_second_lowest_price) + ','
                        group.hist_seller_traded_num += str(group.get_player_by_id(seller).num_of_trading) + ','

                        response = dict(
                            type = 'sell_accept',#'s_2_b_1',
                            seller = seller,
                            buyer = buyer,
                            price = price,
                            seller_num_of_trade = 2,
                            buyer_num_of_trade = 1,
                            seller_payoff = group.get_player_by_id(seller).payoff_2,
                            buyer_payoff = group.get_player_by_id(buyer).payoff_1
                        )
                        return {0: response}

            elif self.num_of_trading == 1: #買い手の取引２回目
                if self.buyer_second_highest_price < price + 40: #買い手の許容価格より価格が高い時
                    response = dict(type='higher_price')
                    return {buyer: response}
                else: #取引成立
                    group.hist_traded_price += str(price) + ','

                    group.get_player_by_id(buyer).amount += 1
                    group.get_player_by_id(buyer).num_of_trading += 1
                    group.get_player_by_id(buyer).second_traded_price = price
                    group.get_player_by_id(buyer).payoff_2 = group.get_player_by_id(buyer).buyer_second_highest_price - price - 40
                    group.hist_buyer += str(buyer) + ','
                    group.hist_buyer_highest_price += str(group.get_player_by_id(buyer).buyer_second_highest_price) + ','
                    group.hist_buyer_payoff += str(group.get_player_by_id(buyer).payoff_2) + ','
                    group.hist_buyer_traded_num += str(group.get_player_by_id(buyer).num_of_trading) + ','

                    group.get_player_by_id(seller).amount -= 1
                    group.hist_seller += str(seller) + ','
                    if group.get_player_by_id(seller).num_of_trading == 0: #売り手の取引回数が一回目の時
                        group.get_player_by_id(seller).num_of_trading += 1
                        group.get_player_by_id(seller).first_traded_price = price
                        group.get_player_by_id(seller).payoff_1 = price - group.get_player_by_id(seller).seller_first_lowest_price
                        group.hist_seller_payoff += str(group.get_player_by_id(seller).payoff_1) + ','
                        group.hist_seller_lowest_price += str(group.get_player_by_id(seller).seller_first_lowest_price) + ','
                        group.hist_seller_traded_num += str(group.get_player_by_id(seller).num_of_trading) + ','

                        response = dict(
                            type = 'sell_accept',#'s_1_b_2',
                            seller = seller,
                            buyer = buyer,
                            price = price,
                            seller_num_of_trade = 1,
                            buyer_num_of_trade = 2,
                            seller_payoff = group.get_player_by_id(seller).payoff_1,
                            buyer_payoff = group.get_player_by_id(buyer).payoff_2
                        )
                        return {0: response}

                    elif group.get_player_by_id(seller).num_of_trading == 1: #売り手の取引回数が二回目の時
                        group.get_player_by_id(seller).num_of_trading += 1
                        group.get_player_by_id(seller).second_traded_price = price
                        group.get_player_by_id(seller).payoff_2 = price - group.get_player_by_id(seller).seller_second_lowest_price
                        group.hist_seller_payoff += str(group.get_player_by_id(seller).payoff_2) + ','
                        group.hist_seller_lowest_price += str(group.get_player_by_id(seller).seller_second_lowest_price) + ','
                        group.hist_seller_traded_num += str(group.get_player_by_id(seller).num_of_trading) + ','

                        response = dict(
                            type = 'sell_accept',#'s_2_b_2',
                            seller = seller,
                            buyer = buyer,
                            price = price,
                            seller_num_of_trade = 2,
                            buyer_num_of_trade = 2,
                            seller_payoff = group.get_player_by_id(seller).payoff_2,
                            buyer_payoff = group.get_player_by_id(buyer).payoff_2
                        )
                        return {0: response}

        elif type == 'buy_accept':
            buyer = data['buyer']
            seller = self.id_in_group
            price = data['price']
            if self.num_of_trading >= 2: #売り手の取引が2回行われていた時
                response = dict(
                    type = 'trade_enough'
                )
                return {self.id_in_group: response}
            elif self.num_of_trading == 0: #売り手の取引一回目
                if self.seller_first_lowest_price > price: #売り手の許容価格より価格が低い時
                    response = dict(type='lower_price')
                    return {seller: response}
                else:
                    group.hist_traded_price += str(price) + ','

                    group.get_player_by_id(seller).amount -= 1
                    group.get_player_by_id(seller).num_of_trading += 1
                    group.get_player_by_id(seller).first_traded_price = price
                    group.get_player_by_id(seller).payoff_1 = price - group.get_player_by_id(seller).seller_first_lowest_price
                    group.hist_seller += str(seller) + ','
                    group.hist_seller_lowest_price += str(group.get_player_by_id(seller).seller_first_lowest_price) + ','
                    group.hist_seller_payoff += str(group.get_player_by_id(seller).payoff_1) + ','
                    group.hist_seller_traded_num += str(group.get_player_by_id(seller).num_of_trading) + ','

                    group.get_player_by_id(buyer).amount += 1
                    group.hist_buyer += str(buyer) + ','
                    if group.get_player_by_id(buyer).num_of_trading == 0: #買い手の取引回数が一回目の時
                        group.get_player_by_id(buyer).num_of_trading += 1
                        group.get_player_by_id(buyer).first_traded_price = price
                        group.get_player_by_id(buyer).payoff_1 = group.get_player_by_id(buyer).buyer_first_highest_price - price - 40
                        group.hist_buyer_payoff += str(group.get_player_by_id(buyer).payoff_1) + ','
                        group.hist_buyer_highest_price += str(group.get_player_by_id(buyer).buyer_first_highest_price) + ','
                        group.hist_buyer_traded_num += str(group.get_player_by_id(buyer).num_of_trading) + ','

                        response = dict(
                            type = 'buy_accept',#'s_1_b_1',
                            seller = seller,
                            buyer = buyer,
                            price = price,
                            seller_num_of_trade = 1,
                            buyer_num_of_trade = 1,
                            seller_payoff = group.get_player_by_id(seller).payoff_1,
                            buyer_payoff = group.get_player_by_id(buyer).payoff_1
                        )
                        return {0: response}

                    elif group.get_player_by_id(buyer).num_of_trading == 1: #買い手の取引回数が二回目の時
                        group.get_player_by_id(buyer).num_of_trading += 1
                        group.get_player_by_id(buyer).second_traded_price = price
                        group.get_player_by_id(buyer).payoff_2 = group.get_player_by_id(buyer).buyer_second_highest_price - price - 40
                        group.hist_buyer_payoff += str(group.get_player_by_id(buyer).payoff_2) + ','
                        group.hist_buyer_highest_price += str(group.get_player_by_id(buyer).buyer_second_highest_price) + ','
                        group.hist_buyer_traded_num += str(group.get_player_by_id(buyer).num_of_trading) + ','

                        response = dict(
                            type = 'buy_accept',#'s_1_b_2',
                            seller = seller,
                            buyer = buyer,
                            price = price,
                            seller_num_of_trade = 1,
                            buyer_num_of_trade = 2,
                            seller_payoff = group.get_player_by_id(seller).payoff_1,
                            buyer_payoff = group.get_player_by_id(buyer).payoff_2
                        )
                        return {0: response}

            elif self.num_of_trading == 1: #売り手の取引２回目
                if self.seller_second_lowest_price > price: #売り手の許容価格より価格が低い時
                    response = dict(type='lower_price')
                    return {seller: response}
                else:
                    group.hist_traded_price += str(price) + ','

                    group.get_player_by_id(seller).amount -= 1
                    group.get_player_by_id(seller).num_of_trading += 1
                    group.get_player_by_id(seller).second_traded_price = price
                    group.get_player_by_id(seller).payoff_2 = price - group.get_player_by_id(seller).seller_second_lowest_price
                    group.hist_seller += str(seller) + ','
                    group.hist_seller_lowest_price += str(group.get_player_by_id(seller).seller_second_lowest_price) + ','
                    group.hist_seller_payoff += str(group.get_player_by_id(seller).payoff_2) + ','
                    group.hist_seller_traded_num += str(group.get_player_by_id(seller).num_of_trading) + ','

                    group.get_player_by_id(buyer).amount += 1
                    group.hist_buyer += str(buyer) + ','
                    if group.get_player_by_id(buyer).num_of_trading == 0: #買い手の取引回数が一回目の時
                        group.get_player_by_id(buyer).num_of_trading += 1
                        group.get_player_by_id(buyer).first_traded_price = price
                        group.get_player_by_id(buyer).payoff_1 = group.get_player_by_id(buyer).buyer_first_highest_price - price - 40
                        group.hist_buyer_payoff += str(group.get_player_by_id(buyer).payoff_1) + ','
                        group.hist_buyer_highest_price += str(group.get_player_by_id(buyer).buyer_first_highest_price) + ','
                        group.hist_buyer_traded_num += str(group.get_player_by_id(buyer).num_of_trading) + ','

                        response = dict(
                            type = 'buy_accept',#'s_2_b_1',
                            seller = seller,
                            buyer = buyer,
                            price = price,
                            seller_num_of_trade = 2,
                            buyer_num_of_trade = 1,
                            seller_payoff = group.get_player_by_id(seller).payoff_2,
                            buyer_payoff = group.get_player_by_id(buyer).payoff_1
                        )
                        return {0: response}

                    elif group.get_player_by_id(buyer).num_of_trading == 1: #買い手の取引回数が二回目の時
                        group.get_player_by_id(buyer).num_of_trading += 1
                        group.get_player_by_id(buyer).second_traded_price = price
                        group.get_player_by_id(buyer).payoff_2 = group.get_player_by_id(buyer).buyer_second_highest_price - price - 40
                        group.hist_buyer_payoff += str(group.get_player_by_id(buyer).payoff_2) + ','
                        group.hist_buyer_highest_price += str(group.get_player_by_id(buyer).buyer_second_highest_price) + ','
                        group.hist_buyer_traded_num += str(group.get_player_by_id(buyer).num_of_trading) + ','

                        response = dict(
                            type = 'buy_accept',#'s_2_b_2',
                            seller = seller,
                            buyer = buyer,
                            price = price,
                            seller_num_of_trade = 2,
                            buyer_num_of_trade = 2,
                            seller_payoff = group.get_player_by_id(seller).payoff_2,
                            buyer_payoff = group.get_player_by_id(buyer).payoff_2
                        )
                        return {0: response}

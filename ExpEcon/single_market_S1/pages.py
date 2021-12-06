from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instruction(Page):
    pass


class Allotment(WaitPage):
    after_all_players_arrive = 'allotment'

class Roll(Page):
    timeout_seconds = 60

class Waiting(WaitPage):
    pass

class Game(Page):
    timeout_seconds = 360
    live_method = 'live_auction'

class Results(Page):
    def js_vars(self):
        lank_list = {}
        for p in self.group.get_players():
            lank_list[p.id_in_group] = p.payoff_1 + p.payoff_2
            print(lank_list)

        price = []
        buyer = []
        seller = []
        history_price = self.group.hist_traded_price.split(',')
        history_seller = self.group.hist_seller.split(',')
        history_buyer = self.group.hist_buyer.split(',')
        history_price.pop(-1)
        history_seller.pop(-1)
        history_buyer.pop(-1)
        for i in history_price:
            price.append(int(i))
        for i in history_seller:
            seller.append(int(i))
        for i in history_buyer:
            buyer.append(int(i))

        return dict(
            lank_list=lank_list,
            price = price,
            seller = seller,
            buyer = buyer
        )



page_sequence = [Instruction, Allotment, Roll, Waiting,Game, Results]

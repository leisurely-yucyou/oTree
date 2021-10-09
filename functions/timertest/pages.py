from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    live_method = 'live_count'

    def before_next_page(self):
        self.player.time = (self.player.finishsec - self.player.startsec) / 1000
        print(self.player.time)




class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    def vars_for_template(self):
        time = self.player.time
        return dict(time = time)


page_sequence = [MyPage, ResultsWaitPage, Results]

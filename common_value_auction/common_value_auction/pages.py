from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instruction(Page):
    def is_displayed(self):
        return self.subsession.round_number == 1

class FirstWaitPage(WaitPage):
    after_all_players_arrive = 'set_estimated_value'

class Game(Page):
    form_model = 'player'
    form_fields = ['bid','bid_reason','forecast_value','forecast_reason']

class ResultWaitPage(WaitPage):
    after_all_players_arrive = 'set_winner'

class Result(Page):
    timeout_seconds = 90
    def vars_for_template(self):
        return dict(is_greedy=self.group.true_value - self.player.bid < 0)

class End(Page):
    def is_displayed(self):
        return self.subsession.round_number == Constants.num_rounds

    def vars_for_template(self):
        bids={}
        estimated_values={}
        forecast_values={}
        highest_values={}
        true_values={}
        utilities={}
        for i in range(2):
            bids[i+1]=(self.player.in_round(i+1).bid)
            estimated_values[i+1]=(self.player.in_round(i+1).estimated_value)
            forecast_values[i+1]=(self.player.in_round(i+1).forecast_value)
            highest_values[i+1]=(self.group.in_round(i+1).highest_value)
            true_values[i+1]=(self.group.in_round(i+1).true_value)
            utilities[i+1]=(self.player.in_round(i+1).utility)
        return dict(
            bids_1=bids[1],
            bids_2=bids[2],
            estimated_values_1=estimated_values[1],
            estimated_values_2=estimated_values[2],
            forecast_values_1 = forecast_values[1],
            forecast_values_2 = forecast_values[2],
            highest_values_1=highest_values[1],
            highest_values_2=highest_values[2],
            true_values_1=true_values[1],
            true_values_2=true_values[2],
            utilities_1=utilities[1],
            utilities_2=utilities[2],
        )

page_sequence = [Instruction, FirstWaitPage, Game, ResultWaitPage, Result, End]

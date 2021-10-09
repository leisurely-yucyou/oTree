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


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'timertest'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    startsec = models.IntegerField()
    finishsec = models.IntegerField()
    time = models.FloatField()

    def live_count(self, data):
        t = data['type']
        if t == 'startsec':
            self.startsec = data['value']
            print(self.startsec)
        else:
            self.finishsec = data['value']
            print(self.finishsec)

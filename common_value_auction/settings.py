from os import environ

SESSION_CONFIGS = [
    dict(
        name = 'common_value_auction_S1',
        display_name = '共通価値オークション_S1',
        num_demo_participants = 5,
        app_sequence=['common_value_auction']
    ),
    dict(
        name = 'common_value_auction_S2',
        display_name = '共通価値オークション_S2',
        num_demo_participants = 10,
        app_sequence=['common_value_auction_10']
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'ja'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'JPY'
REAL_WORLD_CURRENCY_DECIMAL_PLACES=0
USE_POINTS = False

ROOMS = [
    dict(
    name='common_value_auction',
    display_name='共通価値オークション',
    participant_label_file='_rooms/common_value_auction.txt',
    use_secure_urls=False
    )
]

DEBUG = False

AUTH_LEVEL='STUDY'

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'economics2020'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '!s6%qi%ygh!6u@7(u_0#q$pa)^!*e0j_mslp%d#^6w*6qst1$&'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

from os import environ

SESSION_CONFIGS = [
    dict(
        name='asset_market',
        display_name = '株取引実験',
        num_demo_participants=3,
        app_sequence=['asset_market']
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

ROOMS = [dict(
    name='asset_market',
    display_name='資産市場実験',
    participant_label_file='_rooms/asset_market.txt',
    use_secure_urls=False
    ),
]

#DEBUG = False
AUTH_LEVEL='STUDY'

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = 'expecon2022'

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'nks_4&60lor-_1j!1u_x0cdy!vtwqrysnmm-=9y+b-v@qn1r)_'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']

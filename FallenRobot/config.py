class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 22403100
    API_HASH = "ccbc3f662735abfa604ef6309ba76e67"

    CASH_API_KEY = "C6EYHI1BZZ3RC3VC"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgresql://neondb_owner:npg_lmQi28aNAont@ep-broad-sunset-a4jci5hi-pooler.us-east-1.aws.neon.tech/neondb?sslmode=require"  # A sql database url from elephantsql.com

    EVENT_LOGS = ()  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://sumitsajwan135:gameno01@cluster0.ja0i0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://i.ibb.co/HLKLTtgj/file-00000000050c62308b5f75b572396b9b-conversation-id-67fbb6cd-f8d0-800a-bdeb-9630b41378f8-message-i.png"

    SUPPORT_CHAT = "AnimeFantasyG"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "7942335745:AAGFVnS-sEK-y1ZSL1Bsk8CtqTH4Pp7mb_U"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "EAFFDU85P3L9"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 7950514048  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True

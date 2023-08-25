import urllib

from config import Settings, get_env

settings: Settings = get_env()


def get_database():
    db_password = urllib.parse.quote_plus(settings.db_pass)
    url = f'postgresql://{settings.db_username}:{db_password}@{settings.db_host}:{settings.db_port}/{settings.db_name}'
    return url

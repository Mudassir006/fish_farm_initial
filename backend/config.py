from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings


class Settings(BaseSettings):
    debug: bool = False
    db_name: str = ''
    db_host: str = ''
    db_username: str = ''
    db_pass: str = ''
    db_port: int = 5432

    class config:
        env_file = '.env'


@lru_cache()
def get_env():
    load_dotenv()
    return Settings()

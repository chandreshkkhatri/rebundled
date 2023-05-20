import os
from pydantic import BaseSettings

from commons.enums.environment import Environment

class Settings(BaseSettings):
    env_name: str = os.getenv('ENV_NAME', Environment.LOCAL)
    db_name: str = os.getenv('DB_NAME', 'local')
    db_host: str = os.getenv('DB_HOST', 'localhost')
    RESOURCES_DIR: str = os.getenv('RESOURCES_DIR', 'resources')
    local_fe_host: str = os.getenv('LOCAL_FE_HOST', 'http://localhost:3000')
    production_fe_host: str = os.getenv('PRODUCTION_FE_HOST', 'https://www.example.com')
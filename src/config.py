from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_PORT: str
    MYSQL_DATABASE: str
    JWT_SECRET: str

    model_config = SettingsConfigDict(env_file=".env")


def get_config() -> Config:
    return Config()
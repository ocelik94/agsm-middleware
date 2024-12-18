from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    server_host: str = "localhost"
    server_port: int = 8000
    database_url: str = "sqlite:///agsm.db"
    database_username: str = "agsm"
    database_password: str = "<PASSWORD>"
    docker_sock: str = "unix:///var/run/docker.sock"

    class Config:
        env_file = ".env"


settings = Settings()

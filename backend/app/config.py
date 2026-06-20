from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application settings for ProyectaDi.

    Values can be loaded from environment variables or from a local .env file.
    The .env file must not be committed to the repository.
    """

    app_name: str = "ProyectaDi API"
    app_version: str = "0.1.0"
    environment: str = "development"
    api_prefix: str = "/api/v1"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings = Settings()
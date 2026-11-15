"""Application configuration and settings."""

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Central runtime settings loaded from environment variables."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    # Database
    database_url: str | None = None
    database_url_unpooled: str | None = None

    # Auth / security
    jwt_secret: str = "change-me-in-env-min-16-chars"
    demo_mode: bool = False

    # Email
    smtp_host: str | None = None
    smtp_port: int | None = None
    smtp_user: str | None = None
    smtp_password: str | None = None
    email_from: str | None = None

    # External services
    openai_api_key: str | None = None
    openai_base_url: str = "https://api.openai.com/v1"
    advisor_model: str = "gpt-4o-mini"
    app_control_model: str | None = None
    openweather_api_key: str | None = None
    ollama_host: str = "http://localhost:11434"
    ollama_embed_model: str = "nomic-embed-text"

    # Cron / ingest secrets
    prices_cron_secret: str | None = None
    cron_secret: str | None = None
    advisor_cron_secret: str | None = None
    pest_cron_secret: str | None = None

    # Misc
    next_public_app_url: str = "http://localhost:3000"

    @field_validator("smtp_port", mode="before")
    @classmethod
    def parse_optional_smtp_port(cls, value):
        """Treat empty env values as unset so optional int fields parse cleanly."""
        if value is None or value == "":
            return None
        return value


settings = Settings()

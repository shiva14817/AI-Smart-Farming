import os
from functools import lru_cache

from dotenv import load_dotenv

load_dotenv()


class Settings:
    # ==========================
    # Project
    # ==========================
    PROJECT_NAME: str = "FarmGenius Backend"

    # ==========================
    # API Keys
    # ==========================
    GEMINI_API_KEY: str = os.getenv(
        "GEMINI_API_KEY",
        "YOUR_GEMINI_API_KEY_NOT_SET"
    )

    GROQ_API_KEY: str = os.getenv(
        "GROQ_API_KEY",
        "YOUR_GROQ_API_KEY_NOT_SET"
    )

    # ==========================
    # Gemini Models
    # ==========================
    GEMINI_TEXT_MODEL: str = os.getenv(
        "GEMINI_TEXT_MODEL",
        "gemini-3.5-flash"
    )

    GEMINI_VISION_MODEL: str = os.getenv(
        "GEMINI_VISION_MODEL",
        "gemini-3.6-flash"
    )

    # ==========================
    # Upload
    # ==========================
    MAX_FILE_SIZE_MB: int = int(
        os.getenv("MAX_FILE_SIZE_MB", 5)
    )


@lru_cache
def get_settings():
    return Settings()
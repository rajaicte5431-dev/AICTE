"""
Application configuration — reads from .env via pydantic-settings
"""
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # IBM watsonx.ai
    IBM_WATSONX_API_KEY: str = Field(default="", env="IBM_WATSONX_API_KEY")
    IBM_WATSONX_URL: str = Field(default="https://us-south.ml.cloud.ibm.com", env="IBM_WATSONX_URL")
    IBM_WATSONX_PROJECT_ID: str = Field(default="", env="IBM_WATSONX_PROJECT_ID")

    # Granite model IDs
    GRANITE_MODEL_ID: str = Field(default="ibm/granite-13b-instruct-v2", env="GRANITE_MODEL_ID")
    GRANITE_CODE_MODEL_ID: str = Field(default="ibm/granite-20b-code-instruct", env="GRANITE_CODE_MODEL_ID")
    GRANITE_EMBEDDING_MODEL_ID: str = Field(default="ibm/slate-125m-english-rtrvr", env="GRANITE_EMBEDDING_MODEL_ID")

    # Model parameters
    GRANITE_MAX_TOKENS: int = Field(default=2048, env="GRANITE_MAX_TOKENS")
    GRANITE_TEMPERATURE: float = Field(default=0.7, env="GRANITE_TEMPERATURE")
    GRANITE_TOP_P: float = Field(default=0.95, env="GRANITE_TOP_P")

    # App
    APP_NAME: str = Field(default="Syllabus & Curriculum Design Optimizer", env="APP_NAME")
    APP_HOST: str = Field(default="0.0.0.0", env="APP_HOST")
    APP_PORT: int = Field(default=8000, env="APP_PORT")
    APP_DEBUG: bool = Field(default=False, env="APP_DEBUG")

    # Upload
    UPLOAD_DIR: str = Field(default="./uploads", env="UPLOAD_DIR")
    MAX_FILE_SIZE_MB: int = Field(default=10, env="MAX_FILE_SIZE_MB")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    database_url: str
    ollama_url: str = "http://ollama:11434"
    embed_model: str = "all-MiniLM-L6-v2"
    llm_model: str = "qwen3:4b"
    class Config:
        env_file = "SecondBrainAI/.env"

settings = Settings()
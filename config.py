from pydantic import BaseModel


class Settings(BaseModel):
    days_to_prepare: int = 30


settings = Settings()

from datetime import datetime

from pydantic import BaseModel


class CreateTestPayload(BaseModel):
    name: str = ...

    class Config:
        orm_mode = True


class TestDetail(BaseModel):
    name: str
    created_at: datetime

    class Config:
        orm_mode = True

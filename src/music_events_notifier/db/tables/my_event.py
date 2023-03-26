import datetime

from typing import Optional

from sqlmodel import Field, SQLModel


class MyEvent(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime.datetime
    location: str = Field(max_length=70)
    name: str = Field(max_length=70)
    created_at: Optional[datetime.datetime] = datetime.datetime.now



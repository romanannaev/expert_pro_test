from typing import List
from pydantic import BaseModel, validator


class HourEntry(BaseModel):
    type: str
    value: int

    @validator("type")
    def check_type(cls, v):
        if v not in {"open", "close"}:
            raise ValueError('type must be "open" or "close"')
        return v


class DayHours(BaseModel):
    __root__: List[HourEntry]


class OpeningHoursInput(BaseModel):
    monday: DayHours
    tuesday: DayHours
    wednesday: DayHours
    thursday: DayHours
    friday: DayHours
    saturday: DayHours
    sunday: DayHours

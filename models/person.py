from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import date
class Person(BaseModel):
    uni: str = Field(..., description="Columbia UNI, e.g. abc1234")
    first_name: str
    last_name: str
    email: EmailStr
    phone: Optional[str] = None
    birth_date: Optional[date] = None

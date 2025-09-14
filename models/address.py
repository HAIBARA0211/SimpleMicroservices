from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID, uuid4
class Address(BaseModel):
    id: UUID = Field(default_factory=uuid4, description="Server-generated")
    street: str
    city: str
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: str

from pydantic import BaseModel, Field
from typing import Optional

class nameResponse(BaseModel):
    name: str
    first_name: bool
    last_name: bool
    language: Optional[str] = Field(None)
    country: Optional[str] = Field(None)
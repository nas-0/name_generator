from pydantic import BaseModel, Field
from typing import Optional

class nameResponse(BaseModel):

    first_name: str
    last_name: str
    language: str
    country: str
    first_name_meaning: Optional[str] = Field(None)
    last_name_meaning: Optional[str] = Field(None)
    gender: str
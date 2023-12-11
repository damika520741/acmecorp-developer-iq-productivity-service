from typing import Optional
from pydantic import BaseModel

class Developer(BaseModel):
    id: Optional[int]
    git_username: str
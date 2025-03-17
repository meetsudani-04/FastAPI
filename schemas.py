from pydantic import BaseModel

class NameCreate(BaseModel):
    id: int
    name: str
    email: str
# 
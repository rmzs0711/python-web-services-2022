from pydantic import BaseModel


class Guest(BaseModel):
    """Contract for item."""

    name: str
    age: int
    social_rating: int = 42

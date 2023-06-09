from typing import List
from pydantic import BaseModel, Field, constr


class BasicInfo(BaseModel):
    """
    Represents basic information of an event.

    Attributes:
        title (str): Title of the event.
        organizer (str): Organizer of the event.
        category (str): Category of the event.
        sub_category (str): Sub-category of the event.
        tags (List[str]): Tags of the event (max 10 items, each with max 25 characters).
    """

    title: str = Field(..., description="Title of the event")
    organizer: str = Field(..., description="Organizer of the event")
    category: str = Field(..., description="Category of the event")
    sub_category: str = Field(..., description="Sub-category of the event")
    tags: List[constr(max_length=25)] = Field(..., max_items=10,
                                              description="Tags of the event (max 10 items, each with max 25 characters)")

    class Config:
        """
        Pydantic configuration settings for BasicInfo model.
        """
        schema_extra = {
            "example": {
                "title": "Example Event",
                "organizer": "Example Organizer",
                "category": "Example Category",
                "sub_category": "Example Sub-category",
                "tags": ["tag1", "tag2", "tag3"]
            }
        }
        orm_mode = True

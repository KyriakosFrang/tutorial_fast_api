from typing import Optional
from pydantic import BaseModel

__all__ = ["GamingItem"]


class BaseItem(BaseModel):
    name: str
    price: float
    description: Optional[str]
    model: Optional[str]
    sale: bool = False


class GamingItem(BaseItem):
    id_: str


class HomeItem(BaseItem):
    id_: str


class GardenItem(BaseItem):
    id_: str


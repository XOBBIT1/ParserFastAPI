from pydantic import BaseModel
from typing import TypeVar, Optional

T = TypeVar("T")


class Message(BaseModel):
    message: str


class Clothes(BaseModel):
    id: str
    url_clothe: str
    brand_name: str = None
    product_name: str = None
    prise: float


class Response(BaseModel):
    code: int
    status: str
    message: str
    result: Optional[T] = None
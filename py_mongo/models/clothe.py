from pydantic import BaseModel


class Clothes(BaseModel):
    url_clothe: str
    brand_name: str
    product_name: str
    prise: float


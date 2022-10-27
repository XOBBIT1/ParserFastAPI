import uuid

from mg_db.models.clothe import Clothes
from mg_db.config.mongo_db import database


class ClotheRepo:

    @staticmethod
    async def retrieve():
        _clothe = []
        collections = database.get_collection('clothe').find()
        async for clothe in collections:
            _clothe.append(clothe)
        return _clothe

    @staticmethod
    async def insert(clothe: Clothes):
        id = str(uuid.uuid4())
        _clothe = {
            "_id": id,
            "url_clothe": clothe.url_clothe,
            "brand_name": clothe.brand_name,
            "product_name": clothe.product_name,
            "prise": clothe.prise,
        }
        await database.get_collection("clothe").insert_one(_clothe)

    @staticmethod
    async def update(id: str, clothe: Clothes):
        _clothe = await database.get_collections('clothe').findone({"_id": id})
        _clothe["url_clothe"] = clothe.url_clothe
        _clothe["brand_name"] = clothe.brand_name
        _clothe["product_name"] = clothe.product_name
        _clothe["prise"] = clothe.prise
        await database.get_collection("clothe").update_one({"_id": id}, {"$set": _clothe})

    @staticmethod
    async def retrieve_id(id: str):
        return await database.get_collection("clothe").find_one({"id": id})

    @staticmethod
    async def delete(id: str):
        await database.delete_collection("clothe").delete_one({"_id": id})

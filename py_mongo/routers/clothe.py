from fastapi import APIRouter
from py_mongo.models.clothe import Clothes
from py_mongo.config.mongo_db import connaction
from py_mongo.schemas.clothe import clothe_entity, clothes_entity

clothe = APIRouter()


@clothe.get("/")
async def find_all_clothes():
    return await clothes_entity(connaction.local.clothe.find())


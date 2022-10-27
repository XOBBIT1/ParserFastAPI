from fastapi import APIRouter
from mg_db.commands.command import ClotheRepo
from mg_db.models.clothe import Clothes, Response

router = APIRouter()


@router.get("/")
async def find_all_clothes():
    clothe_list = await ClotheRepo.retrieve()
    return Response(code=200, status="OK", message="Success retrieve all data",
                    result=clothe_list).dict(exclude_none=True)


@router.get("/{id}")
async def find_clothe(id: int):
    clothe = await ClotheRepo.retrieve_id(id)
    return Response(status_code=200, status="OK", message="Success save all data",
                    result=clothe).dict(exclude_none=True)


@router.put("/{id}")
async def update(clothe: Clothes):
    await ClotheRepo.update(clothe)
    return Response(status_code=200, status="OK", message="Success change all data").dict(exclude_none=True)


@router.delete("/{id}")
async def delete(id: int):
    await ClotheRepo.delete(id)
    return Response(status_code=200, status="OK", message="Success change all data").dict(exclude_none=True)

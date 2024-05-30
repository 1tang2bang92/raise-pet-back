from typing import Optional

from fastapi import APIRouter, Request, Form
from ..service import breed_info as bi
from fastapi import File, UploadFile

router = APIRouter()

@router.get('/breed', status_code=200)
async def breed_info(request: Request):
    return bi.get_breed_info()


@router.post('/breed/upload', status_code=201)
async def upload_breed(file: bytes = UploadFile):
    return bi.save_breed(file)
from fastapi import APIRouter
from fastapi.responses import Response

router = APIRouter()


@router.get("/login")
def login():
    return Response(content="Login ")
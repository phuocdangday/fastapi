from fastapi import APIRouter, status

from src.auth.schemas import LoginDTO

router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/login', status_code=status.HTTP_200_OK)
def login(loginDTO: LoginDTO):
    pass

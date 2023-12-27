from fastapi import APIRouter, status, HTTPException
from src.users.schemas import CreateUserDTO, UpdateUserDTO
from src.users.service import UserService

router = APIRouter(prefix='/users', tags=['users'])
user_service = UserService()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create(create_user_dto: CreateUserDTO):
    return user_service.create(create_user_dto)


@router.put('/{id}', status_code=status.HTTP_200_OK)
def update(id, update_user_dto: UpdateUserDTO):
    user = user_service.find_by_id(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    user_service.update(id, update_user_dto)


@router.delete('/{id}', status_code=status.HTTP_200_OK)
def delete(id):
    user = user_service.find_by_id(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    user_service.delete(id)


@router.get('/{id}', status_code=status.HTTP_200_OK)
def get(id):
    user = user_service.find_by_id(id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    return user


@router.get('/', status_code=status.HTTP_200_OK)
def get_all():
    return user_service.find_all()

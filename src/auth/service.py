from fastapi import HTTPException, status

from src.auth.schemas import LoginDTO
from src.auth.utils.bcrypt import hash_password, verify_password
from src.auth.utils.jwt import create_access_token
from src.users.repository import UserRepository
from src.users.schemas import CreateUserDTO


class AuthService():
    user_repository = UserRepository()

    def login(self, loginDTO: LoginDTO):
        user = self.user_repository.find_by_username(loginDTO.username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail='Username or password wrong')

        is_match_password = verify_password(
            password=loginDTO.password,
            hashed_password=user.password
        )
        if not is_match_password:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail='Username or password wrong')

        access_token = create_access_token(
            data={'id': user.id}
        )

        return {
            'access_token': access_token
        }

    def register(self, registerDTO):
        create_user_dto = CreateUserDTO(
            name=registerDTO.name,
            username=registerDTO.username,
            password=hash_password(registerDTO.password)
        )

        self.user_repository.create(create_user_dto)

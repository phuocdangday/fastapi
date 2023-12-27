from pydantic import BaseModel


class CreateUserDTO(BaseModel):
    name: str


class UpdateUserDTO(BaseModel):
    name: str

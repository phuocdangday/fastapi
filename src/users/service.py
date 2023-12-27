from src.users.repository import UserRepository
from src.users.schemas import CreateUserDTO, UpdateUserDTO


class UserService():
    repository = UserRepository()

    def __init__(self):
        pass

    def create(self, create_user_dto: CreateUserDTO):
        return self.repository.create(create_user_dto)

    def update(self, id, update_user_dto: UpdateUserDTO):
        return self.repository.update(id, update_user_dto)

    def find_by_id(self, id):
        return self.repository.find_by_id(id)

    def find_all(self):
        return self.repository.find_all()

    def delete(self, id):
        return self.repository.delete(id)

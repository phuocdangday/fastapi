from src.users.models import User
from src.repository import BaseRepository


class UserRepository(BaseRepository):
    def __init__(self):
        super().__init__(User)

    def find_by_username(self, username):
        return self.session.query(User).filter_by(username).first()

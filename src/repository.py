from pydantic import BaseModel
from src.database import get_session


class BaseRepository():
    session = get_session()

    def __init__(self, model):
        self.model = model

    def create(self, data: BaseModel):
        db_data = self.model(**data.model_dump())
        self.session.add(db_data)
        self.session.commit()
        self.session.refresh(db_data)

        return db_data

    def update(self, id, data: BaseModel):
        self.session.query(self.model).filter_by(
            id=id).update(data.model_dump())
        self.session.commit()

    def delete(self, id):
        self.session.query(self.model).filter_by(id=id).delete()
        self.session.commit()

    def find_by_id(self, id):
        return self.session.query(self.model).filter_by(id=id).first()

    def find_all(self):
        return self.session.query(self.model).all()

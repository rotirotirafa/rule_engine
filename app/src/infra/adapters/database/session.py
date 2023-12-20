from sqlalchemy.orm import Session
from app.src.infra.adapters.database.base import SessionLocal


class DBSession:
    def __enter__(self) -> Session:
        self.db = SessionLocal()
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


def get_db() -> DBSession:
    return DBSession()

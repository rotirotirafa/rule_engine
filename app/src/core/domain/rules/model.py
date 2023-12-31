from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.src.infra.adapters.database.base import Base


class RulesModel(Base):
    __tablename__ = "rules"

    rule_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(Integer)
    condition = Column(String)
    action = Column(String)
    parameters = Column(String)
    message = Column(String)
    description = Column(String)
    created_date = Column(DateTime, default=datetime.now())

    class Config:
        orm_mode = True


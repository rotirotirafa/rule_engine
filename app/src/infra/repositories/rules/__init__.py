from typing import List

from sqlalchemy.orm import Session

from app.src.core.domain.rules.model import RulesModel
from app.src.core.schemas import RuleSchema, RuleUpdateSchemaRequest, RulesPostSchema
from app.src.exceptions import RuleNotFoundException


class RulesRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_one(self, rule_id: int):
        rule = self.db.query(RulesModel).get(rule_id)
        if not rule:
            raise RuleNotFoundException(rule_id)
        return rule

    def get_all(self) -> List[RulesModel] or List:
        rules = self.db.query(RulesModel).all()
        return rules

    def insert(self, rule: RulesPostSchema) -> RuleSchema:
        create_object = RulesModel(
            name=rule.name,
            condition=rule.condition,
            action=rule.action
        )
        self.db.add(create_object)
        self.db.commit()
        self.db.refresh(create_object)
        return create_object

    def update(self, rule_id: int, rule: RuleUpdateSchemaRequest) -> RuleSchema:
        old_object = self.db.query(RulesModel).filter_by(rule_id=rule_id)
        old_object.update(
            {
                "name": rule.name or old_object['name'],
                "condition": rule.condition or old_object['condition'],
                "action": rule.action or old_object['action'],
            }
        )
        self.db.commit()
        return self.get_one(rule_id)

    def delete(self, rule_id: int):
        self.db.query(RulesModel).filter_by(rule_id=rule_id).delete()
        self.db.commit()
        return

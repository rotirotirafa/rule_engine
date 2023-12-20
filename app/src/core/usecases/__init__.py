from typing import List

from app.src.core.schemas import RulesPostSchema, RuleUpdateSchemaRequest, RuleSchema
from app.src.infra.adapters.database.session import get_db
from app.src.infra.repositories.rules import RulesRepository


class RulesUseCases:

    def __init__(self):
        with get_db() as db:
            self.rules_repo = RulesRepository(db)

    def get_one_rule(self, rule_id: int):
        rule = self.rules_repo.get_one(rule_id)
        return rule

    def get_rules(self) -> List[RuleSchema] or RuleSchema:
        rules = self.rules_repo.get_all()
        return rules

    def insert_rules(self, rule: RulesPostSchema):
        rule = self.rules_repo.insert(rule)
        return rule

    def update_rule(self, rule_id: int,  rule: RuleUpdateSchemaRequest):
        rule = self.rules_repo.update(rule_id, rule)
        return rule

    def delete_rule(self, rule_id: int):
        rule = self.rules_repo.delete(rule_id)
        return

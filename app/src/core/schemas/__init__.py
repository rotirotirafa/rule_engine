from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class RuleSchema(BaseModel):
    rule_id: Optional[int]
    name: str
    condition: str
    action: str


class RulesPostSchema(BaseModel):
    name: str
    condition: str
    action: str


class RuleUpdateSchemaRequest(BaseModel):
    name: Optional[str]
    condition: Optional[str]
    action: Optional[str]

from typing import Optional

from pydantic import BaseModel


class RuleSchema(BaseModel):
    rule_id: Optional[int]
    name: str
    condition: str
    action: str
    code: int
    parameters: str
    message: str
    description: str


class RulesPostSchema(BaseModel):
    name: str
    condition: str
    action: str
    code: int
    parameters: str
    message: str
    description: str


class RuleUpdateSchemaRequest(BaseModel):
    name: Optional[str]
    condition: Optional[str]
    action: Optional[str]
    code: Optional[int]
    parameters: Optional[str]
    message: Optional[str]
    description: Optional[str]

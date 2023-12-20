from typing import List

from fastapi import APIRouter
from fastapi.responses import ORJSONResponse

from app.src.core.schemas import RuleSchema, RulesPostSchema, RuleUpdateSchemaRequest
from app.src.core.usecases import RulesUseCases

RulesRoute = APIRouter(
    prefix='/rules'
)


@RulesRoute.get('/{rule_id}', response_model=RuleSchema)
def get_rules(rule_id: int):
    try:
        rule_use_case = RulesUseCases()
        return rule_use_case.get_one_rule(rule_id)
    except Exception as ex:
        raise ex


@RulesRoute.get('/', response_model=List[RuleSchema] or RuleSchema)
def get_rules():
    try:
        rule_use_case = RulesUseCases()
        return rule_use_case.get_rules()
    except Exception as ex:
        raise ex


@RulesRoute.post('/', response_model=RuleSchema)
def post_rules(payload: RulesPostSchema) -> RuleSchema:
    try:
        rule_use_case = RulesUseCases()
        return rule_use_case.insert_rules(payload)
    except Exception as ex:
        raise ex


@RulesRoute.put('/{rule_id}', response_model=RuleSchema)
def put_rules(rule_id: int, payload: RuleUpdateSchemaRequest) -> RuleSchema:
    try:
        rule_use_case = RulesUseCases()
        return rule_use_case.update_rule(rule_id, payload)
    except Exception as ex:
        raise ex


@RulesRoute.delete('/{rule_id}')
def delete_rule(rule_id: int) -> ORJSONResponse:
    try:
        rule_use_case = RulesUseCases()
        rule_use_case.delete_rule(rule_id)
        return ORJSONResponse({'message': 'Regra deletada com sucesso'})
    except Exception as ex:
        raise ex

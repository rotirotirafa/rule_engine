class CustomException(Exception):
    def __init__(self, message: str, status_code: int):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class RuleNotFoundException(CustomException):
    def __init__(self, rule_id):
        message = f"Regra com ID {rule_id} não encontrada."
        super().__init__(message, status_code=404)

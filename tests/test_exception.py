import unittest

from app.src.exceptions import CustomException, RuleNotFoundException


class TestCustomExceptions(unittest.TestCase):

    def test_custom_exception(self):
        # Testar CustomException
        try:
            raise CustomException("Mensagem de erro personalizada", status_code=400)
        except CustomException as e:
            self.assertEqual(e.message, "Mensagem de erro personalizada")
            self.assertEqual(e.status_code, 400)

    def test_rule_not_found_exception(self):
        # Testar RuleNotFoundException
        rule_id = 123
        try:
            raise RuleNotFoundException(rule_id)
        except RuleNotFoundException as e:
            expected_message = f"Regra com ID {rule_id} não encontrada."
            self.assertEqual(e.message, expected_message)
            self.assertEqual(e.status_code, 404)


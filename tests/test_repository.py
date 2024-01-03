import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.src.exceptions import RuleNotFoundException
from app.src.infra.adapters.database.base import Base

from app.src.core.domain.rules.model import RulesModel
from app.src.core.schemas import RulesPostSchema, RuleUpdateSchemaRequest
from app.src.infra.repositories.rules import RulesRepository

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


class TestRulesRepository(unittest.TestCase):

    def setUp(self):
        rule1 = RulesModel(name="Test Rule 1", condition="test_condition_1", action="test_action_1")
        rule2 = RulesModel(name="Test Rule 2", condition="test_condition_2", action="test_action_2")
        rule3 = RulesModel(name="Test Rule 3", condition="test_condition_3", action="test_action_3")

        self.db = TestingSessionLocal()
        self.repository = RulesRepository(self.db)

        self.db.add_all([rule1, rule2, rule3])
        self.db.commit()

    def tearDown(self):
        self.db.close()

    def test_get_one(self):
        retrieved_rule = self.repository.get_one(1)
        self.assertEqual(retrieved_rule.name, "Test Rule 1")

        with self.assertRaises(RuleNotFoundException):
            self.repository.get_one(10000)

    def test_get_all(self):
        retrieved_rules = self.repository.get_all()

        self.assertGreater(len(retrieved_rules), 2)

    def test_insert(self):
        new_rule = RulesPostSchema(
            name="New Test Rule",
            condition="new_condition",
            action="new_action",
            code=20000,
            parameters="new_parameters",
            message="new_message",
            description="new_description"
        )

        inserted_rule = self.repository.insert(new_rule)

        self.assertIsNotNone(inserted_rule.rule_id)
        self.assertEqual(inserted_rule.name, "New Test Rule")

    def test_update(self):
        rule = RulesModel(name="Test Rule 213131", condition="test_condition", action="test_action")
        self.db.add(rule)
        self.db.commit()

        updated_rule_data = RuleUpdateSchemaRequest(
            name="atualizada Test Rule",
            condition="condition",
            action="action",
            code=20001,
            parameters="params",
            message="msg",
            description="desc"
        )

        updated_rule = self.repository.update(rule.rule_id, updated_rule_data)

        self.assertEqual(updated_rule.name, "atualizada Test Rule")
        self.assertEqual(updated_rule.condition, "condition")
        self.assertEqual(updated_rule.action, "action")

    def test_delete(self):
        rule = RulesModel(name="Test Rulex", condition="test_condition", action="test_action")
        self.db.add(rule)
        self.db.commit()

        self.repository.delete(rule.rule_id)

        with self.assertRaises(RuleNotFoundException):
            self.repository.get_one(rule.rule_id)

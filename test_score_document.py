import unittest
from docubot import DocuBot


class TestScoreDocument(unittest.TestCase):
    """
    Validates DocuBot.score_document relevance scoring logic.

    Usage:
        bot = DocuBot()
        score = bot.score_document(query="...", text="...")
    """

    def setUp(self):
        # Empty folder prevents disk reads during unit tests
        self.bot = DocuBot(docs_folder="/tmp")

    def test_exact_term_match(self):
        query = "connect database"
        text = "How to connect to PostgreSQL database"
        score = self.bot.score_document(query, text)
        self.assertEqual(score, 2)

    def test_case_and_punctuation_insensitivity(self):
        query = "AUTH, Token!"
        text = "The auth token is required."
        score = self.bot.score_document(query, text)
        self.assertEqual(score, 2)

    def test_zero_match(self):
        query = "billing invoice"
        text = "This document only covers auth and database setup."
        score = self.bot.score_document(query, text)
        self.assertEqual(score, 0)


if __name__ == "__main__":
    unittest.main()

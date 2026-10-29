import unittest
from docubot import DocuBot


class TestBuildIndex(unittest.TestCase):
    def setUp(self):
        self.bot = DocuBot.__new__(DocuBot)

    def test_build_index_happy_case(self):
        docs = [
            ("doc1.md", "Hello world! Database connection."),
            ("doc2.md", "World database, query engine.")
        ]
        index = self.bot.build_index(docs)

        self.assertEqual(index["hello"], ["doc1.md"])
        self.assertEqual(sorted(index["world"]), ["doc1.md", "doc2.md"])
        self.assertEqual(sorted(index["database"]), ["doc1.md", "doc2.md"])
        self.assertEqual(index["engine"], ["doc2.md"])

    def test_build_index_failure_case(self):
        with self.assertRaises(TypeError):
            self.bot.build_index(None)


if __name__ == "__main__":
    unittest.main()

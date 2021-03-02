import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    def test_id_1(self):
        self.assertTrue(TestLexer.checkLexeme("ab4", "ab4,<EOF>", 101))

    def test_id_2(self):
        self.assertTrue(TestLexer.checkLexeme("abcd", "abcd,<EOF>", 102))

    def test_id_3(self):
        self.assertTrue(TestLexer.checkLexeme("4bcd", "Error Token 4", 103))

    def test_real_1(self):
        self.assertTrue(TestLexer.checkLexeme("43e-1", "43e-1,<EOF>", 104))

    def test_real_2(self):
        self.assertTrue(TestLexer.checkLexeme("4.3e0", "4.3e0,<EOF>", 105))

    def test_real_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "-4.3e+33", "-4.3e+33,<EOF>", 105))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme("'sfee4'", "'sfee4',<EOF>", 106))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme("'aada'", "'aada',<EOF>", 101))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'aad''a'", "'aad''a',<EOF>", 101))

    def test_all(self):
        self.assertTrue(TestLexer.checkLexeme(
            "'aad''a' d3a -43e-5", "'aad''a',d3a,-43e-5,<EOF>", 101))

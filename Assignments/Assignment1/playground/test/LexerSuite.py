from TestUtils import TestLexer
import unittest


class LexerSuite(unittest.TestCase):

    def test_unterminated_comment(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r'''
a1122
''',

            r'''Unclosed String: \n''',
            147
        ))

    def test_unterminated_comment1(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r'''
a*2 
''',

            r'''Unclosed String: \n''',
            147
        ))

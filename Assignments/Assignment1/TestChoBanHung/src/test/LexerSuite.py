import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):
    '''
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))

'''

    def test_intlit_hex(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("0xFF", "0xFF,<EOF>", 101))

    def test_intlit_hex2(self):
        self.assertTrue(TestLexer.checkLexeme("0xFFo", "0xFF,o,<EOF>", 102))

    def test_intlit_octal(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o770x11", "0o77,0x11,<EOF>", 103))

    def test_intlit_zero(self):
        self.assertTrue(TestLexer.checkLexeme("0", "0,<EOF>", 106))

    def test_floatlit(self):
        self.assertTrue(TestLexer.checkLexeme("720e-1", "720e-1,<EOF>", 104))

    def test_floatlit2(self):
        self.assertTrue(TestLexer.checkLexeme("12.3", "12.3,<EOF>", 105))

    def test_normal_string_with_escape(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107))

    def test_normal_string_with_doublequote(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "day la cau '"ksks'"kdmckmc" """, """day la cau '"ksks'"kdmckmc,<EOF>""", 108))

    def test_normal_string(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ "mothaiba"  """, """mothaiba,<EOF>""", 109))

    def test_intlit_hex3(self):
        self.assertTrue(TestLexer.checkLexeme("0x0", """0,x0,<EOF>""", 110))

    def test_arraylit_int_1dems(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{2,3,4}", """{2,3,4},<EOF>""", 111))

    def test_arraylit_int_2dems(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{2,3,4},{4,5,6}}", "{{2,3,4},{4,5,6}},<EOF>", 112))

    def test_arraylit_int_3dems(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{2,3,4},{4,5,6},{7,8,9}}", "{{2,3,4},{4,5,6},{7,8,9}},<EOF>", 113))

    def test_arraylit_float_1dems(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{2.2,3.12,4.982}", "{2.2,3.12,4.982},<EOF>", 114))

    def test_arraylit_float_2dems(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{{2.3,3.12,4.23},{4.23,5.11,6.222}}", "{{2.3,3.12,4.23},{4.23,5.11,6.222}},<EOF>", 115))

    def test_arraylit_float_3dems(self):
        self.assertTrue(TestLexer.checkLexeme("{{2.123,3.123,4.23},{4.121,5.654,6.35},{7.3423,8.5345,9.2332}}",
                                              "{{2.123,3.123,4.23},{4.121,5.654,6.35},{7.3423,8.5345,9.2332}},<EOF>", 116))

    # keyword operator separator
    def test_keyword_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Body Else EndFor If Var EndDo", "Body,Else,EndFor,If,Var,EndDo,<EOF>", 117))

    def test_keyword_2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Break ElseIf EndWhile Parameter While", "Break,ElseIf,EndWhile,Parameter,While,<EOF>", 118))

    def test_keyword_3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Continue EndBody For Return True", "Continue,EndBody,For,Return,True,<EOF>", 119))

    def test_keyword_4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Do EndIf Function Then False", "Do,EndIf,Function,Then,False,<EOF>", 120))

    def test_operator_1(self):
        self.assertTrue(TestLexer.checkLexeme("- -. + +. * *. \\ \\. % ! && || == != < > <= >= =/= <. >. <=. >=. =",
                                              "-,-.,+,+.,*,*.,\\,\\.,%,!,&&,||,==,!=,<,>,<=,>=,=/=,<.,>.,<=.,>=.,=,<EOF>", 121))

    def test_separator_1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "( ) { } [ ] , ; : .", "(,),{,},[,],,,;,:,.,<EOF>", 122))

    def test_var(self):
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 123))

    def test_var2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "Var: x;", "Var,:,x,;,<EOF>", 124))

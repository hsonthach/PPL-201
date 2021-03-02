from TestUtils import TestLexer
import unittest


class LexerSuite(unittest.TestCase):

    def test_hex(self):
        """test  hex"""
        self.assertTrue(TestLexer.checkLexeme(
            "0x123Anfcb", "0x123A,nfcb,<EOF>", 100))

    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var", "Var,<EOF>", 102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?svn", "ab,Error Token ?", 103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;", "Var,x,;,<EOF>", 104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc\\h def"  """, """Illegal Escape In String: abc\\h""", 105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "abc def  """, """Unclosed String: abc def  """, 106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(
            """ "ab'"c\\n def"  """, """ab'"c\\n def,<EOF>""", 107))

    def test_1_valid_lowercase_keywords(self):
        """ Test Valid Lowercase Keywords """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
Body Break Continue Do
Else ElseIf EndBody EndIf
EndFor EndWhile For Function
If Parameter Return Then
Var While True False
EndDo
""",
            r"Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,If,Parameter,Return,Then,Var,While,True,False,EndDo,<EOF>",
            108
        ))

    def test_3_valid_specific_characters(self):
        """ Test Specific Characters """
        self.assertTrue(TestLexer.checkLexeme(
            """
% ! && ||
== ! = < >
<= >= =/= <.
>. <=. >=.
""",

            "%,!,&&,||,==,!,=,<,>,<=,>=,=/=,<.,>.,<=.,>=.,<EOF>",
            109
        ))

    def test_5_block_comment(self):
        """ Test Block Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
** Comment with multiple lines
    Hello comments
**
""",

            "<EOF>",
            110
        ))

    def test_7_mix_comment(self):
        """ Test Mix Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
** This is a block comment **


** This is a line comment **

** Comment with multiple lines
    Hello comments
**
""",

            "<EOF>",
            111
        ))

    def test_8_int_lit(self):
        """ Test Integer Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
0 1 2 3 4 123 123456789
""",

            "0,1,2,3,4,123,123456789,<EOF>",
            112
        ))

    def test_12_invalid_id(self):
        """ Test Invalid Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
123abc 123 abc 123
""",

            "123,abc,123,abc,123,<EOF>",
            113
        ))

    def test_14_invalid_real(self):
        """ Test Invalid Real Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
e-12 e12 . 1e 12e 12.05e .05e ee e01
""",

            "e,-,12,e12,.,1,e,12,e,12.05,e,.,0,5,e,ee,e01,<EOF>",
            114
        ))

    def test_15_arr_decl(self):
        """ Test Array Declare """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
array[13] = {1,2,3} ;
""",

            "array,[,13,],=,{,1,,,2,,,3,},;,<EOF>",
            115
        ))

    def test_16_unclose_without_endline(self):
        """ Test Unclose String without endline """
        self.assertTrue(TestLexer.checkLexeme(
            r"""  " hello lexer """,

            "Unclosed String:  hello lexer ",
            116
        ))

    def test_17_unclose_with_endline(self):
        """ Test Unclose String with endline """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abcxyz
""",

            r"""Unclosed String:  abcxyz""",
            117
        ))

    def test_18_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc \n xyz "
" abc \\n xyz "
""",

            r''' abc \n xyz , abc \\n xyz ,<EOF>''',
            118
        ))

    def test_19_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" hello lexer \t "     asdf
""",

            r' hello lexer \t ,asdf,<EOF>',
            119
        ))

    def test_20_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Backspace  \b"
""",

            r'Backspace  \b,<EOF>',
            120
        ))

    def test_21_escape(self):
        """ Test Escape String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Formfeed   \f"
""",

            r'Formfeed   \f,<EOF>',
            121
        ))

    def test_22_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Return     \r"
""",

            r'''Return     \r,<EOF>''',
            122
        ))

    def test_23_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Newline    \n"
""",

            r'''Newline    \n,<EOF>''',
            123
        ))

    def test_24_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Newline    '""
""",

            r'''Newline    '",<EOF>''',
            124
        ))

    def test_25_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Tab        \t"
""",

            r'Tab        \t,<EOF>',
            125
        ))

    def test_26_escape(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"Backslash  \\ "
""",

            r"Backslash  \\ ,<EOF>",
            126
        ))

    def test_27_illegal(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
illegal: "\a"
""",

            r'''illegal,:,Illegal Escape In String: \a''',
            127
        ))

    def test_28_illegal(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi \c \d "
""",

            "Illegal Escape In String:  Hi Hi \c",
            128
        ))

    def test_29_illegal(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi \m\n\c\s\d\\f "
""",

            "Illegal Escape In String:  Hi Hi \m",
            129
        ))

    def test_30_nevermind(self):
        """ Test Nevermind :) """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" asdf ` asdf"
""",

            " asdf ` asdf,<EOF>",
            130
        ))

    def test_29_illegal1(self):
        """ Test Illegal Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" Hi Hi ' "
""",

            "Illegal Escape In String:  Hi Hi ' ",
            131
        ))

    def test_32_escape_singlequote(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
" abc \' xyz "
""",

            r" abc \' xyz ,<EOF>",
            132
        ))

    def test_string_literal(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''"He asked me: '"Where is John?'""''', r'''He asked me: '"Where is John?'",<EOF>''', 133))

    def test_34_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc" 123 123 "abc xyz"
" abc\m "
""",

            "abc,123,123,abc xyz,Illegal Escape In String:  abc\m",
            134
        ))

    def test_string_literal1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r'''
"This is a string containing tab \t"
''', r'''This is a string containing tab \t,<EOF>''', 135))

    def test_11_id(self):
        """ Test Identifiers """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
a abc a123 a_ a_bc a_bc123 a_123 a_123bc a_bc_123

""",

            "a,abc,a123,a_,a_bc,a_bc123,a_123,a_123bc,a_bc_123,<EOF>",
            136
        ))

    def test_37_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
a = a & 1
""",

            "a,=,a,Error Token &",
            137
        ))

    def test_38_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
xyz
$a = 5
""",

            "xyz,Error Token $",
            138
        ))

    def test_39_err_tok(self):
        """ Test Error Token """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
# define for 1
""",

            "Error Token #",
            139
        ))

    def test_40_num_leading_0(self):
        """ Test Number leading 0 """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1234 1231231234 12321343123
""",

            "1234,1231231234,12321343123,<EOF>",
            140
        ))

    def test_41_num_leading_0(self):
        """ Test Real Leading 0 """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
00001.1111000000
0e-4
000000001e-40000
""",

            "00001.1111000000,0e-4,000000001e-40000,<EOF>",
            141
        ))

    def test_42_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \ xyz"
""",

            "abc - xyz,Illegal Escape In String: abc \ ",
            142
        ))

    def test_43_illegal(self):
        """ Test Error String """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc - xyz"
"abc \yyz"
""",

            "abc - xyz,Illegal Escape In String: abc \y",
            143
        ))

    def test_44_escape_backsplash_spacing(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"abc \\ xyz"
""",

            r"abc \\ xyz,<EOF>",
            144
        ))

    def test_45_escape_backsplash_trim(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\\"
""",

            r'''\\,<EOF>''',
            145
        ))

    def test_46_escape_backsplash_tail_spacing(self):
        """ Test Escape """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
"\\ "
""",

            r"\\ ,<EOF>",
            146
        ))

    def test_47_unclose_use_escape(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r'''
"\n
''',

            r'''Unclosed String: \n''',
            147
        ))

    def test_illegal_escape8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"1.2+1.3+1.4\\o'\"123", "Illegal Escape In String: 1.2+1.3+1.4\\o", 148))

    def test_illegal_escape9(self):
        self.assertTrue(TestLexer.checkLexeme(
            "+1.1 \"ba\\qm\f\"", "+,1.1,Illegal Escape In String: ba\\q", 149))

    def test_illegal_escape10(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"concaheo\\uabc\"", "Illegal Escape In String: concaheo\\u", 150))

    def test_unclose_String1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"bacxyc", "Unclosed String: bacxyc", 151))

    def test_unclose_String2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "smkobsn+s1+\"`sS2h.s(", "smkobsn,+,s1,+,Unclosed String: `sS2h.s(", 152))

    def test_unclose_String3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"acnv \" \"abc", "acnv ,Unclosed String: abc", 153))

    def test_unclose_String4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"acms!,lds \"  123\"abc", "acms!,lds ,123,Unclosed String: abc", 154))

    def test_unclose_String5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "a+11.2+\"mam.123\" 12 \"%^&", "a,+,11.2,+,mam.123,12,Unclosed String: %^&", 155))

    def test_unclose_String6(self):
        self.assertTrue(TestLexer.checkLexeme(
            "38n\"[#Ffs?0ED\"0.\"T`#!7n", "38,n,[#Ffs?0ED,0.,Unclosed String: T`#!7n", 156))

    def test_unclose_String7(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\".Hub`22Y\"<\"Y`=DxXhZKh", ".Hub`22Y,<,Unclosed String: Y`=DxXhZKh", 157))

    def test_unclose_String8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"ULxM*`~.~+C_DISD2", "Unclosed String: ULxM*`~.~+C_DISD2", 158))

    def test_unclose_String9(self):
        self.assertTrue(TestLexer.checkLexeme(
            "\"Nk8U;\"rA\"@Y3*\"oV\"bh1", "Nk8U;,rA,@Y3*,oV,Unclosed String: bh1", 159))

    def test_unclose_String10(self):
        self.assertTrue(TestLexer.checkLexeme("\"o|s&)sqX\"+>s+\"#Fft",
                                              "o|s&)sqX,+,>,s,+,Unclosed String: #Fft", 160))

    def test_9_real_lit(self):
        """ Test Real Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
1.2 1.  1e2 1.2E-2 1.2e-2  9.0 12e8 0.33E-3 128e-42
12.          12.05 1e-5      1.5e-6  0.0005e3   2e21
""",

            "1.2,1.,1e2,1.2E-2,1.2e-2,9.0,12e8,0.33E-3,128e-42,12.,12.05,1e-5,1.5e-6,0.0005e3,2e21,<EOF>",
            161
        ))

    def test_10_string_lit(self):
        """ Test String Literal """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
""      "A"
"Mulitiple Characters"
""",

            ',A,Mulitiple Characters,<EOF>',
            162
        ))

    def test_111_unclose_use_escape(self):
        """ Test Unclosed String """
        self.assertTrue(TestLexer.checkLexeme(
            r'''
"\\
''',

            r'''Unclosed String: \\''',
            163
        ))

    def test_4(self):
        """ Test Inline Comment """
        self.assertTrue(TestLexer.checkLexeme(
            r"""
** This is a line comment **
""",

            "<EOF>",
            164
        ))

    def test_array(self):
        self.assertTrue(TestLexer.checkLexeme(
            r"""{{1,2},{3,4},{5,6}}""", "{{{{1,2}},{{4,5}},{{3,5}}}},<EOF>", 165))

    def test_array1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{1,3,5,7}", "{,1,,,3,,,5,,,7,},<EOF>", 166))

    def test_array(self):
        self.assertTrue(TestLexer.checkLexeme(
            "{}", "{,},<EOF>", 167))

    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "** a\n **", "<EOF>", 168))

    def test_float_literal5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "120000e-1", "120000e-1,<EOF>", 169))

    def test_float_literal3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.0e3", "12.0e3,<EOF>", 170))

    def test_float_literal4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12000.", "12000.,<EOF>", 171))

    def test_float_literal2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.e5", "12.e5,<EOF>", 172))

    def test_float_literal1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12e3", "12e3,<EOF>", 173))

    def test_float_literal(self):
        self.assertTrue(TestLexer.checkLexeme(
            "12.0e3", "12.0e3,<EOF>", 174))

    def test_integer_literal5(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0o56", "0o56,<EOF>", 175))

    def test_integer_literal4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0O77", "0O77,<EOF>", 176))

    def test_integer_literal3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "199", "199,<EOF>", 177))

    def test_integer_literal2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0", "0,<EOF>", 178))

    def test_error_char1(self):
        self.assertTrue(TestLexer.checkLexeme(
            " 11.+12*#$", "11.,+,12,*,Error Token #", 179))

    def test_error_char2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "arj4AORqwExkrCxZPi`:", "arj4AORqwExkrCxZPi,Error Token `", 180))

    def test_error_char3(self):
        self.assertTrue(TestLexer.checkLexeme(
            "o%jvhs'Ty{*(0Ay0s&n|", "o,%,jvhs,Error Token '", 181))

    def test_error_char4(self):
        self.assertTrue(TestLexer.checkLexeme(
            "(s*.=22sta!0=&o", "(,s,*.,=,22,sta,!,0,=,Error Token &", 182))

    def test_error_char5(self):
        self.assertTrue(TestLexer.checkLexeme(
            ";s~%IbnQL!x-OBd", ";,s,Error Token ~", 183))

    def test_integer_literal2(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0xFF", "0xFF,<EOF>", 184))

    def test_error_char7(self):
        self.assertTrue(TestLexer.checkLexeme("kz-70s9+0s)f<)?0gg",
                                              "kz,-,70,s9,+,0,s,),f,<,),Error Token ?", 185))

    def test_error_char8(self):
        self.assertTrue(TestLexer.checkLexeme(
            "s+9and+es9{?r2v}hFAX|>", "s,+,9,and,+,es9,{,Error Token ?", 186))

    def test_error_char9(self):
        self.assertTrue(TestLexer.checkLexeme(
            "pQ*6'q0+Y@}f(^9Xn", "pQ,*,6,Error Token '", 187))

    def test_error_char10(self):
        self.assertTrue(TestLexer.checkLexeme(
            "aFG[@WQS{QBW7Y6]le$5", "aFG,[,Error Token @", 188))

    def test_random1(self):
        self.assertTrue(TestLexer.checkLexeme(
            r""" "hel\\\"l\\\'o\\\\hehe" """, "Illegal Escape In String: hel\\\\\\\"", 189))

    def test_random2(self):
        self.assertTrue(TestLexer.checkLexeme(
            """ 2+3 andthen 6 """, "2,+,3,andthen,6,<EOF>", 190))

    def test_random3(self):
        self.assertTrue(TestLexer.checkLexeme("""
        "abcd
        efg
        """, "Unclosed String: abcd", 191))

    def test_random4(self):
        self.assertTrue(TestLexer.checkLexeme("""
        "abcd \b
        efg
        """, "Unclosed String: abcd ", 192))

    def test_random5(self):
        self.assertTrue(TestLexer.checkLexeme("""
        "t \f
        efg
        """, "Unclosed String: t ", 193))

    def test_random6(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
        "t \f efg"
        """, "Unclosed String: t ", 194))

    def test_random7(self):
        self.assertTrue(TestLexer.checkLexeme(""" 
        "t \\\\x efg"
        """, "t \\\\x efg,<EOF>", 195))

    def test_integer_literal1(self):
        self.assertTrue(TestLexer.checkLexeme(
            "0XABC", "0XABC,<EOF>", 196))

    def test_integer_literal(self):
        self.assertTrue(TestLexer.checkLexeme(
            "09", "0,9,<EOF>", 197))

    def test_comment(self):
        """test  comment"""
        self.assertTrue(TestLexer.checkLexeme(
            "** a **", "<EOF>", 198))

    def test_func_call(self):
        """test  func call"""
        self.assertTrue(TestLexer.checkLexeme(
            "fact()", "fact,(,),<EOF>", 199))

    def test_parameter(self):
        """test  parameter"""
        self.assertTrue(TestLexer.checkLexeme(
            "Parameter: n,arr", "Parameter,:,n,,,arr,<EOF>", 200))

    def test_func_def(self):
        """test  func def"""
        self.assertTrue(TestLexer.checkLexeme(
            "Function: fact", "Function,:,fact,<EOF>", 99))

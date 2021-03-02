import unittest
from TestUtils import TestLexer


class LexerSuite(unittest.TestCase):

    """ Empty file """

    def test_101(self):
        input = ""
        expect = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 101))

    """ White-space """

    def test_102(self):
        input = " \t\f\r\n"
        expect = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))

    """ Comment """

    def test_103(self):
        input = r""" ** Single-line comment ** """
        expect = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))

    def test_104(self):
        input = r""" ** Multiple-line
                      * Comment
                      ** """
        expect = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 104))

    def test_105(self):
        input = r""" ** Unterminated Comment """
        expect = r"""Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))

    def test_106(self):
        input = r"""**** empty comment"""
        expect = r"""empty,comment,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))

    def test_107(self):
        input = r""" ** comment ** not a comment"""
        expect = r"""not,a,comment,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 107))

    def test_108(self):
        input = r""" ** comment ** not a comment **"""
        expect = r"""not,a,comment,Unterminated Comment"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))

    def test_109(self):
        input = r""" ** comment ** not a comment ** comment **"""
        expect = r"""not,a,comment,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))

    def test_110(self):
        input = r""" *****"""
        expect = r"""*,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 110))

    def test_111(self):
        input = r""" ** ***"""
        expect = r"""*,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 111))

    def test_112(self):
        input = r""" *** **"""
        expect = r"""<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 112))

    """ Keyword """

    def test_113(self):
        input = r""" Var """
        expect = r"""Var,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 113))

    def test_114(self):
        input = r""" Function """
        expect = r"""Function,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 114))

    def test_115(self):
        input = r""" Parameter """
        expect = r"""Parameter,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 115))

    def test_116(self):
        input = r""" Body """
        expect = r"""Body,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 116))

    def test_117(self):
        input = r""" EndBody """
        expect = r"""EndBody,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 117))

    def test_118(self):
        input = r""" If """
        expect = r"""If,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 118))

    def test_119(self):
        input = r""" Then """
        expect = r"""Then,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test_120(self):
        input = r""" ElseIf """
        expect = r"""ElseIf,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 120))

    def test_121(self):
        input = r""" Else """
        expect = r"""Else,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 121))

    def test_122(self):
        input = r""" EndIf """
        expect = r"""EndIf,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 122))

    def test_123(self):
        input = r""" While """
        expect = r"""While,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 123))

    def test_124(self):
        input = r""" For """
        expect = r"""For,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 124))

    def test_125(self):
        input = r""" Do """
        expect = r"""Do,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 125))

    def test_126(self):
        input = r""" EndWhile """
        expect = r"""EndWhile,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 126))

    def test_127(self):
        input = r""" EndDo """
        expect = r"""EndDo,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 127))

    def test_128(self):
        input = r""" EndFor """
        expect = r"""EndFor,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 128))

    def test_129(self):
        input = r""" Break """
        expect = r"""Break,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 129))

    def test_130(self):
        input = r""" Continue """
        expect = r"""Continue,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 130))

    def test_131(self):
        input = r""" Return """
        expect = r"""Return,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 131))

    def test_132(self):
        input = r""" True """
        expect = r"""True,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 132))

    def test_133(self):
        input = r""" False """
        expect = r"""False,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 133))

    def test_134(self):
        input = r""" Body. """
        expect = r"""Body,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 134))

    """ Operator """

    def test_135(self):
        input = r""" +-*\% """
        expect = r"""+,-,*,\,%,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 135))

    def test_136(self):
        input = r""" +.-.*.\. """
        expect = r"""+.,-.,*.,\.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 136))

    def test_137(self):
        input = r""" !&&|| """
        expect = r"""!,&&,||,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 137))

    def test_138(self):
        input = r""" ==!==/= """
        expect = r"""==,!=,=/=,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 138))

    def test_139(self):
        input = r""" <><=>= """
        expect = r"""<,>,<=,>=,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 139))

    def test_140(self):
        input = r""" <.>.<=.>=. """
        expect = r"""<.,>.,<=.,>=.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 140))

    def test_141(self):
        input = r""" = """
        expect = r"""=,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 141))

    """ Seperator """

    def test_142(self):
        input = r""" (){}[]:;., """
        expect = r"""(,),{,},[,],:,;,.,,,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 142))

    """ Identifier """

    def test_143(self):
        input = r""" a b c d e f g h i j k l m n o p q r s t u v w x y z """
        expect = r"""a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 143))

    def test_144(self):
        input = r""" a_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ """
        expect = r"""a_0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 144))

    def test_145(self):
        input = r""" 1234abcd ABCDdefg """
        expect = r"""1234,abcd,Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 145))

    def test_146(self):
        input = r""" _abcd """
        expect = r"""Error Token _"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 146))

    def test_147(self):
        input = r""" Abcd """
        expect = r"""Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 147))

    """ Decimal integer literal """

    def test_148(self):
        input = r""" 0 """
        expect = r"""0,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 148))

    def test_149(self):
        input = r""" 1 2 3 4 5 6 7 8 9 """
        expect = r"""1,2,3,4,5,6,7,8,9,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 149))

    def test_150(self):
        input = r"""
100000000
111111111 222222222 333333333
444444444 555555555 666666666
777777777 888888888 999999999
"""
        expect = r"""100000000,111111111,222222222,333333333,444444444,555555555,666666666,777777777,888888888,999999999,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 150))

    def test_151(self):
        input = r""" 0001234 """
        expect = r"""0,0,0,1234,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 151))

    def test_152(self):
        input = r""" -1234 +5678"""
        expect = r"""-,1234,+,5678,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 152))

    def test_153(self):
        input = r""" 123A """
        expect = r"""123,Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 153))

    """ Hexa integer literal """

    def test_154(self):
        input = r""" 0x1 0X1 """
        expect = r"""0x1,0X1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 154))

    def test_155(self):
        input = r""" 0x1 0x2 0x3 0x4 0x5 0x6 0x7 0x8 0x9 0xA 0xB 0xC 0xD 0xE 0xF"""
        expect = r"""0x1,0x2,0x3,0x4,0x5,0x6,0x7,0x8,0x9,0xA,0xB,0xC,0xD,0xE,0xF,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 155))

    def test_156(self):
        input = r"""
0x100000000
0x111111111 0x222222222 0x333333333 0x444444444 0x555555555
0x666666666 0x777777777 0x888888888 0x999999999 0xAAAAAAAAA
0xBBBBBBBBB 0xCCCCCCCCC 0xDDDDDDDDD 0xEEEEEEEEE 0xFFFFFFFFF
"""
        expect = r"""0x100000000,0x111111111,0x222222222,0x333333333,0x444444444,0x555555555,0x666666666,0x777777777,0x888888888,0x999999999,0xAAAAAAAAA,0xBBBBBBBBB,0xCCCCCCCCC,0xDDDDDDDDD,0xEEEEEEEEE,0xFFFFFFFFF,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 156))

    def test_157(self):
        input = r""" 0x0123 """
        expect = r"""0,x0123,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 157))

    def test_158(self):
        input = r""" 0X0123 """
        expect = r"""0,Error Token X"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 158))

    def test_159(self):
        input = r""" 0x123abcd """
        expect = r"""0x123,abcd,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 159))

    """ Octal integer literal """

    def test_160(self):
        input = r""" 0o1 0O1 """
        expect = r"""0o1,0O1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 160))

    def test_161(self):
        input = r""" 0o1 0o2 0o3 0o4 0o5 0o6 0o7 """
        expect = r"""0o1,0o2,0o3,0o4,0o5,0o6,0o7,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 161))

    def test_162(self):
        input = r"""
0o100000000
0o111111111 0o222222222 0o333333333
0o444444444 0o555555555 0o666666666 0o777777777
"""
        expect = r"""0o100000000,0o111111111,0o222222222,0o333333333,0o444444444,0o555555555,0o666666666,0o777777777,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 162))

    def test_163(self):
        input = r""" 0o0123 0O0123 """
        expect = r"""0,o0123,0,Error Token O"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 163))

    def test_164(self):
        input = r""" 0o56789 """
        expect = r"""0o567,89,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 164))

    def test_165(self):
        input = r""" 0o98765 """
        expect = r"""0,o98765,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 165))

    def test_166(self):
        input = r""" 0o123ABCD """
        expect = r"""0o123,Error Token A"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 166))

    """ Float literal """

    def test_167(self):
        input = r"""
000000000.000000000e000000000
111111111.111111111e111111111
222222222.222222222e222222222
333333333.333333333e333333333
444444444.444444444e444444444
555555555.555555555e555555555
666666666.666666666e666666666
777777777.777777777e777777777
888888888.888888888e888888888
999999999.999999999e999999999
"""
        expect = r"""000000000.000000000e000000000,111111111.111111111e111111111,222222222.222222222e222222222,333333333.333333333e333333333,444444444.444444444e444444444,555555555.555555555e555555555,666666666.666666666e666666666,777777777.777777777e777777777,888888888.888888888e888888888,999999999.999999999e999999999,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 167))

    def test_168(self):
        input = r""" 1.1 1. """
        expect = r"""1.1,1.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 168))

    def test_169(self):
        input = r""" 1E1 1E+1 1E-1 1e1 1e+1 1e-1  """
        expect = r"""1E1,1E+1,1E-1,1e1,1e+1,1e-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 169))

    def test_170(self):
        input = r"""1e1 1.1e1 1.e1 1E1 1.1E1 1.E1 """
        expect = r"""1e1,1.1e1,1.e1,1E1,1.1E1,1.E1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 170))

    def test_171(self):
        input = r""" 1e-1 1.1e-1 1.e-1 1E-1 1.1E-1 1.E-1  """
        expect = r"""1e-1,1.1e-1,1.e-1,1E-1,1.1E-1,1.E-1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 171))

    def test_172(self):
        input = r""" 1e+1 1.1e+1 1.e+1 1E+1 1.1E+1 1.E+1 """
        expect = r"""1e+1,1.1e+1,1.e+1,1E+1,1.1E+1,1.E+1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 172))

    def test_173(self):
        input = r""" 1e """
        expect = r"""1,e,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 173))

    def test_174(self):
        input = r""" .1 """
        expect = r""".,1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 174))

    def test_175(self):
        input = r""" e1 """
        expect = r"""e1,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 175))

    """ String literal """

    def test_176(self):
        input = """
"0123456789"
"abcdefghijklmnopqrstuvwxyz"
"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
"!#$%&()*+,-./:;<=>?@[]^_`{|}~"
" "
"""
        expect = "0123456789,abcdefghijklmnopqrstuvwxyz,ABCDEFGHIJKLMNOPQRSTUVWXYZ,!#$%&()*+,-./:;<=>?@[]^_`{|}~, ,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 176))

    def test_177(self):
        input = r""" "\b\f\r\n\t\'\\" """
        expect = r"""\b\f\r\n\t\'\\,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 177))

    def test_178(self):
        input = r""" "str'"" """
        expect = r"""str'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_179(self):
        input = r""" "Next line:\n'"str'"" """
        expect = r"""Next line:\n'"str'",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 179))

    def test_180(self):
        input = r""" "str\'" """
        expect = r"""str\',<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 180))

    """ Array literals"""

    def test_181(self):
        input = r""" {"1", 1, 1., True} """
        expect = r"""{,1,,,1,,,1.,,,True,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 181))

    def test_182(self):
        input = r""" {{{{{{1, {2}, {{3}}}}}}}, {{{2}}}, {3}, 4} """
        expect = r"""{,{,{,{,{,{,1,,,{,2,},,,{,{,3,},},},},},},},,,{,{,{,2,},},},,,{,3,},,,4,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 182))

    def test_183(self):
        input = r""" {1,2, ** cmt **, 3} """
        expect = r"""{,1,,,2,,,,,3,},<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 183))

    """ Illegal escape """

    def test_184(self):
        input = r""" "it's a dog" """
        expect = r"""Illegal Escape In String: it's"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))

    def test_185(self):
        input = r""" "it''s a dog" """
        expect = r"""Illegal Escape In String: it''"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 185))

    def test_186(self):
        input = r""" "it'\" """
        expect = "Illegal Escape In String: it'\\"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 186))

    def test_187(self):
        input = r""" "it' " """
        expect = r"""Illegal Escape In String: it' """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 187))

    def test_188(self):
        input = r""" "str\1str" """
        expect = r"""Illegal Escape In String: str\1"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 188))

    def test_189(self):
        input = r""" "str\zstr" """
        expect = r"""Illegal Escape In String: str\z"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 189))

    def test_190(self):
        input = r""" "str\"str" """
        expect = "Illegal Escape In String: str\\\""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 190))

    def test_191(self):
        input = r""" "str\ str" """
        expect = r"""Illegal Escape In String: str\ """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 191))

    """ Unclosed string """

    def test_192(self):
        input = r""""str
"""
        expect = r"""Unclosed String: str"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 192))

    def test_193(self):
        input = r""" "str"""
        expect = r"""Unclosed String: str"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 193))

    def test_194(self):
        input = r""" "
"""
        expect = r"""Unclosed String: """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 194))

    def test_195(self):
        input = " \""
        expect = r"""Unclosed String: """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 195))

    def test_196(self):
        input = " \"str'\""
        expect = "Unclosed String: str'\""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 196))

    """ Error token """

    def test_197(self):
        input = r""" abcd? """
        expect = r"""abcd,Error Token ?"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 197))

    def test_198(self):
        input = r""" 1 / 2 """
        expect = r"""1,Error Token /"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 198))

    """ Free style """

    def test_199(self):
        input = r""" Var: b[2][3] = {{2,3,4},{4,5,6}}, a, c = 6, a, a; """
        expect = r"""Var,:,b,[,2,],[,3,],=,{,{,2,,,3,,,4,},,,{,4,,,5,,,6,},},,,a,,,c,=,6,,,a,,,a,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 199))

    def test_200(self):
        input = r"""
Function: foo
    Parameter: a[5], b
    Body:
        Var: i = 0;
        While (i < 5)
            a[i] = b +. 1.0;
            i = i + 1;
        EndWhile.
        If n == 0 Then
            Return 1;
        Else
            Return n * fact (n - 1);
        EndIf.
        v = (4. \. 3.) *. 3.14 *. r *. r *. r;
    EndBody.
    If bool_of_string ("True") Then
        a = int_of_string (read ());
        b = float_of_int (a) +. 2.0;
    EndIf.
    foo (2 + x, 4. \. y);
    a[3 + foo(2)] = a[b[2][3]] + 4;
    writeln(i);
EndIf.
"""
        expect = r"""Function,:,foo,Parameter,:,a,[,5,],,,b,Body,:,Var,:,i,=,0,;,While,(,i,<,5,),a,[,i,],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,If,n,==,0,Then,Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,v,=,(,4.,\.,3.,),*.,3.14,*.,r,*.,r,*.,r,;,EndBody,.,If,bool_of_string,(,True,),Then,a,=,int_of_string,(,read,(,),),;,b,=,float_of_int,(,a,),+.,2.0,;,EndIf,.,foo,(,2,+,x,,,4.,\.,y,),;,a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,;,writeln,(,i,),;,EndIf,.,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 200))

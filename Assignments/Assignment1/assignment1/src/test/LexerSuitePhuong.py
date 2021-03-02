import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
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
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def" ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab '" c\\n def"  ""","""ab '" c\\n def,<EOF>""",107))
    def test8(self):
        
        self.assertTrue(TestLexer.checkLexeme(" { {1, 2, 3}, {4, 5, 6} }  ","{ {1, 2, 3}, {4, 5, 6} },<EOF>",108))
    def test9(self):
        
        self.assertTrue(TestLexer.checkLexeme(" {1, 2, 3}  ","{1, 2, 3},<EOF>",109))
    def test10(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "abc dfe  ""","""Unclosed String: abc dfe  """,110))
    def test11(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" **this is a comment**  ""","""<EOF>""",111))
    def test12(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" **this is 
        a block of 
        comment** ""","""<EOF>""",112))
    def test13(self):
        
        self.assertTrue(TestLexer.checkLexeme("a123dng","a123dng,<EOF>",113))
    def test14(self):
        
        self.assertTrue(TestLexer.checkLexeme("1ahdi","1,ahdi,<EOF>",114))
    def test15(self):
        
        self.assertTrue(TestLexer.checkLexeme("abc @","abc,Error Token @",115))
    def test16(self):
        
        self.assertTrue(TestLexer.checkLexeme("If x == 10 Then x = x + 1","If,x,==,10,Then,x,=,x,+,1,<EOF>",116))
    def test17(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" Var: x; ""","Var,:,x,;,<EOF>",117))
    def test18(self):
        
        self.assertTrue(TestLexer.checkLexeme("""Break;""","Break,;,<EOF>",118))
    def test19(self):
        
        self.assertTrue(TestLexer.checkLexeme("""While""","While,<EOF>",119))
    def test20(self):
        
        self.assertTrue(TestLexer.checkLexeme("""Continue""","Continue,<EOF>",120))
    def test21(self):
        
        self.assertTrue(TestLexer.checkLexeme("""**this is a comment unclosed""","Unterminated Comment",121))
    def test22(self):
        
        self.assertTrue(TestLexer.checkLexeme("""**this is 
        a block comment 
        unclosed""","Unterminated Comment",122))
    def test23(self):
        
        self.assertTrue(TestLexer.checkLexeme("""ancdefghjkl""","ancdefghjkl,<EOF>",123))
    def test24(self):
        
        self.assertTrue(TestLexer.checkLexeme("""a_A_0""","a_A_0,<EOF>",124))
    def test25(self):
        
        self.assertTrue(TestLexer.checkLexeme("""Abcdef""","Error Token A",125))
    def test26(self):
        
        self.assertTrue(TestLexer.checkLexeme("""ab@did""","ab,Error Token @",126))
    def test27(self):
        
        self.assertTrue(TestLexer.checkLexeme("""abd!did""","abd,!,did,<EOF>",127))
    def test28(self):
        
        self.assertTrue(TestLexer.checkLexeme("""abd#done""","abd,Error Token #",128))
    def test29(self):
        
        self.assertTrue(TestLexer.checkLexeme("""abd$done""","abd,Error Token $",129))
    def test30(self):
        
        self.assertTrue(TestLexer.checkLexeme("""abd%done""","abd,%,done,<EOF>",130))
    def test31(self):
        
        self.assertTrue(TestLexer.checkLexeme("""abd&done""","abd,Error Token &",131))
    def test32(self):
        
        self.assertTrue(TestLexer.checkLexeme("""abd^done""","abd,Error Token ^",132))
    def test33(self):
        
        self.assertTrue(TestLexer.checkLexeme("""abd*done""","abd,*,done,<EOF>",133))
    def test34(self):
        
        self.assertTrue(TestLexer.checkLexeme("""abd`done""","abd,Error Token `",134))
    def test35(self):
        
        self.assertTrue(TestLexer.checkLexeme("""abd~done""","abd,Error Token ~",135))
    def test36(self):
        
        self.assertTrue(TestLexer.checkLexeme("""Function""","Function,<EOF>",136))
    def test37(self):
        
        self.assertTrue(TestLexer.checkLexeme("""If  EndIf  Else  ElseIf""","If,EndIf,Else,ElseIf,<EOF>",137))
    def test38(self):
        
        self.assertTrue(TestLexer.checkLexeme("""True
        False""","True,False,<EOF>",138))
    def test39(self):
        
        self.assertTrue(TestLexer.checkLexeme("""Parameter  For EndFor""","Parameter,For,EndFor,<EOF>",139))
    def test40(self):
        
        self.assertTrue(TestLexer.checkLexeme("""+ +. -  -.""","+,+.,-,-.,<EOF>",140))
    def test41(self):
        
        self.assertTrue(TestLexer.checkLexeme("""*  *. \\ \\. ""","*,*.,\\,\\.,<EOF>",141))
    def test42(self):
        
        self.assertTrue(TestLexer.checkLexeme("""% ! &&  ||""","%,!,&&,||,<EOF>",142))
    def test43(self):
        
        self.assertTrue(TestLexer.checkLexeme(""".\\ .+ .- .*""",".,\\,.,+,.,-,.,*,<EOF>",143))
    def test44(self):
        
        self.assertTrue(TestLexer.checkLexeme("""==  !=  < > <= >==/= >.<.""","==,!=,<,>,<=,>=,=/=,>.,<.,<EOF>",144))
    def test45(self):
        
        self.assertTrue(TestLexer.checkLexeme("""0123""","0123,<EOF>",145))
    def test46(self):
        
        self.assertTrue(TestLexer.checkLexeme("""1234320""","1234320,<EOF>",146))
    def test47(self):
        
        self.assertTrue(TestLexer.checkLexeme("""0xFF""","0xFF,<EOF>",147))
    def test48(self):
        
        self.assertTrue(TestLexer.checkLexeme("""0XACB""","0XACB,<EOF>",148))
    def test49(self):
        
        self.assertTrue(TestLexer.checkLexeme("""0o07  0O07""","0o07,0O07,<EOF>",149))
    def test50(self):
        
        self.assertTrue(TestLexer.checkLexeme("""12.0e3""","12.0e3,<EOF>",150))
    def test51(self):
        
        self.assertTrue(TestLexer.checkLexeme("""0.00012e3""","0.00012e3,<EOF>",151))
    def test52(self):
        
        self.assertTrue(TestLexer.checkLexeme("""12000.""","12000.,<EOF>",152))
    def test53(self):
        
        self.assertTrue(TestLexer.checkLexeme("""12.0e-3""","12.0e-3,<EOF>",153))
    def test54(self):
        
        self.assertTrue(TestLexer.checkLexeme("""12.e5""","12.e5,<EOF>",154))
    def test55(self):
        
        self.assertTrue(TestLexer.checkLexeme("""1200e-3""","1200e-3,<EOF>",155))
    def test56(self):
        
        self.assertTrue(TestLexer.checkLexeme("""  "This is a string containing a tab \\t" ""","""This is a string containing a tab \\t,<EOF>""",156))
    def test57(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "This is a '"" ""","""This is a '",<EOF>""",157))
    def test58(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "this is backspace \\b" ""","""this is backspace \\b,<EOF>""",158))
    def test59(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "He ask: '"Where is monney?'"" ""","""He ask: '"Where is monney?'",<EOF>""",159))
    def test60(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "this is \\h" ""","""Illegal Escape In String: this is \\h""",160))
    def test61(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "supported escape \\f \\\\ \\' \\n \\r" ""","""supported escape \\f \\\\ \\' \\n \\r,<EOF>""",161))
    def test62(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" " other illegal escape \\p " ""","""Illegal Escape In String:  other illegal escape \\p""",162))
    def test63(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" {1,2,3,4,5} ""","""{1,2,3,4,5},<EOF>""",163)),
    def test64(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" {{1,2,3},{4,5,6}} ""","""{{1,2,3},{4,5,6}},<EOF>""",164))
    def test65(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" { 1, 2, 3 } ""","""{ 1, 2, 3 },<EOF>""",165))
    def test66(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" a[5] ""","""a,[,5,],<EOF>""",166))
    def test67(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" If n == 0 Then Return 0; Else Continue ""","""If,n,==,0,Then,Return,0,;,Else,Continue,<EOF>""",167))
    def test68(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" Var: x, y, u = 9, t; ""","""Var,:,x,,,y,,,u,=,9,,,t,;,<EOF>""",168))
    def test69(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" Function: fact ""","""Function,:,fact,<EOF>""",169))
    def test70(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" Parameter: n ""","""Parameter,:,n,<EOF>""",170))
    def test71(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "illegal escape \\c" ""","""Illegal Escape In String: illegal escape \\c""",171))
    def test72(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "illegal escape \\x" ""","""Illegal Escape In String: illegal escape \\x""",172))
    def test73(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "illegal escape \\m" ""","""Illegal Escape In String: illegal escape \\m""",173))
    def test74(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" ** this is comment unclosed ""","""Unterminated Comment""",174))
    def test75(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 1ahs ""","""1,ahs,<EOF>""",175))
    def test76(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" _ahd ""","""Error Token _""",176))
    def test77(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" abhd_( ""","""abhd_,(,<EOF>""",177))
    def test78(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" abkd) ""","""abkd,),<EOF>""",178))
    def test79(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" sd~df ""","""sd,Error Token ~""",179))
    def test80(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 1234^123 ""","""1234,Error Token ^""",180))
    def test81(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 012e3 ""","""012e3,<EOF>""",181))
    def test82(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 00000.00000e-4 ""","""00000.00000e-4,<EOF>""",182))
    def test83(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 0asdf ""","""0,asdf,<EOF>""",183))
    def test84(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 0o2345 ""","""0o2345,<EOF>""",184))
    def test85(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 0XABCDEF ""","""0XABCDEF,<EOF>""",185))
    def test86(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" True False ""","""True,False,<EOF>""",186))
    def test87(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" foo(2 + x, 4. \\. y) ""","""foo,(,2,+,x,,,4.,\\.,y,),<EOF>""",187))
    def test88(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" For (i = 0, i < 20, 2) Do
            writeln(i);
            EndFor. ""","""For,(,i,=,0,,,i,<,20,,,2,),Do,writeln,(,i,),;,EndFor,.,<EOF>""",188))
    def test89(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" x = x + y \\ z -. 12.e3 *. 12 ""","""x,=,x,+,y,\\,z,-.,12.e3,*.,12,<EOF>""",189))
    def test90(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" a && b || c && !d ""","""a,&&,b,||,c,&&,!,d,<EOF>""",190))
    def test91(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "this is a long long long 
        string " ""","""Unclosed String: this is a long long long """,191))
    def test92(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" " this is string containing '" but not close ""","""Unclosed String:  this is string containing '" but not close """,192))
    def test93(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" "others chars in string !@#$%^&*()~`" ""","""others chars in string !@#$%^&*()~`,<EOF>""",193))
    def test94(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" { { { 1 }, { 1, 2 } }, { 1, 2, 3 } } ""","""{ { { 1 }, { 1, 2 } }, { 1, 2, 3 } },<EOF>""",194))
    def test95(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" a[2][5] ""","""a,[,2,],[,5,],<EOF>""",195))
    def test96(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 0.0000e3 ""","""0.0000e3,<EOF>""",196))
    def test97(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 12E+90 ""","""12E+90,<EOF>""",197))
    def test98(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 0O012345671234 ""","""0O012345671234,<EOF>""",198))
    def test99(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" 0x1 0X1 012 0 ""","""0x1,0X1,012,0,<EOF>""",199))
    def test100(self):
        
        self.assertTrue(TestLexer.checkLexeme(""" abdn"idi ""","""abdn,Unclosed String: idi """,200))
    
    
    
import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme(""" **abcxyz ""","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Else EndIf ElseIf","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "a'bc\\"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" {   1  ,  2,3  , 4}  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme("""   ""","""ab'"c\\n def,<EOF>""",107))
    
    def test_identifier8(self):
        self.assertTrue(TestLexer.checkLexeme("rdad 40oBhenK292aWfTSFLt6","rdad,40,oBhenK292aWfTSFLt6,<EOF>",108))
    def test_identifier9(self):
        self.assertTrue(TestLexer.checkLexeme("vJozdspl3p1iOcRiAI12 dUB 1.NM 2cY2","vJozdspl3p1iOcRiAI12,dUB,1.,Error Token N",109))
    def test_identifier10(self):
        self.assertTrue(TestLexer.checkLexeme("0gChhrlnd8xI1dsxd s dwdski6E","0,gChhrlnd8xI1dsxd,s,dwdski6E,<EOF>",110))


    def test_keyword1(self):
        self.assertTrue(TestLexer.checkLexeme("01anc mds For c brEaK 21mc continuE km","0,1,anc,mds,For,c,brEaK,21,mc,continuE,km,<EOF>",111))
    def test_keyword2(self):
        self.assertTrue(TestLexer.checkLexeme("tO doWnto Do if thEn elSE return1","tO,doWnto,Do,if,thEn,elSE,return1,<EOF>",112))
    def test_keyword3(self):
        self.assertTrue(TestLexer.checkLexeme("reTuRn whILe beGin eND function o","reTuRn,whILe,beGin,eND,function,o,<EOF>",113))
    def test_keyword4(self):
        self.assertTrue(TestLexer.checkLexeme("pROCEDURE TRUe 1.12VAR45 ARRay OF 12REAL","pROCEDURE,Error Token T",114))
    def test_keyword5(self):
        self.assertTrue(TestLexer.checkLexeme("BOOLEAN int 1.12INTEGER sTRIng not 12and","Error Token B",115))
    def test_keyword6(self):
        self.assertTrue(TestLexer.checkLexeme("oR diVModNTEGER Mod nottrEu","oR,diVModNTEGER,Error Token M",116))
    def test_keyword7(self):
        self.assertTrue(TestLexer.checkLexeme("If then else diMod 12String true ds false","If,then,else,diMod,12,Error Token S",117))
    def test_keyword8(self):
        self.assertTrue(TestLexer.checkLexeme("anD then elsediMod doWnTO.1trueds false","anD,then,elsediMod,doWnTO,.,1,trueds,false,<EOF>",118))
    def test_keyword9(self):
        self.assertTrue(TestLexer.checkLexeme("anD thadenelsediMod doWnTO.1truedsfalse BOOLEAN float 1.12INTEGER sTRIng noT d15s0and","anD,thadenelsediMod,doWnTO,.,1,truedsfalse,Error Token B",119))
    def test_keyword10(self):
        self.assertTrue(TestLexer.checkLexeme("12while int 1.12 INTEGER oR 12function","12,while,int,1.12,Error Token I",120))

    def test_string1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \\t" """,""" "This is a string containing tab \\t",<EOF>""",121))
    def test_string2(self):
        self.assertTrue(TestLexer.checkLexeme("\"He asked me: \'\"Where is John?\'\"\"","\"\",Error Token N,<EOF>",122))
    def test_string3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "John isn'"t me" ""","\"abc	a\\nbc\",<EOF>",123))
    def test_string4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","\"abc\",0,\"12ab\\fc0.1\",<EOF>",124))
    def test_string5(self):
        self.assertTrue(TestLexer.checkLexeme("\"0.1anc\\'cv\" 0.mne \"12\\\\3\"","\"0.1anc\\'cv\",0.,mne,\"12\\\\3\",<EOF>",125))
    def test_string6(self):
        self.assertTrue(TestLexer.checkLexeme("abc \"abc1!!@#$$%^i\\n\" 12yz","abc,\"abc1!!@#$$%^i\\n\",12,yz,<EOF>",126))
    def test_string7(self):
        self.assertTrue(TestLexer.checkLexeme("\"!h$5FBi6\"_q\"!SZR,H}\"sIfpw","\"!h$5FBi6\",Error Token _",127))
    def test_string8(self):
        self.assertTrue(TestLexer.checkLexeme("4\"&J^1a_.\" QGn\"?67Sp\"{,}6Asz\"Yx](\"","4,\"&J^1a_.\",Error Token Q",128))
    def test_string9(self):
        self.assertTrue(TestLexer.checkLexeme("0f1_\"^VLR@\\\\OusM;\"uGM+jE","0,f1_,\"^VLR@\\OusM;\",uGM,+,jE,<EOF>",129))
    def test_string10(self):
        self.assertTrue(TestLexer.checkLexeme("\"(IFq+lq(\"IhK6we(*.*)GdvS{(}","\"(IFq+lq(\",Error Token I",130))

    def test_operator1(self):
        self.assertTrue(TestLexer.checkLexeme("ddsls<l>02>=d1s<=123","ddsls,<,l,>,0,2,>=,d1s,<=,123,<EOF>",131))
    def test_operator2(self):
        self.assertTrue(TestLexer.checkLexeme("dlsd+1ds-*dmdsa/<>mdks","dlsd,+,1,ds,-,*,dmdsa,Error Token /",132))
    def test_operator3(self):
        self.assertTrue(TestLexer.checkLexeme("lsddl<>=1<>=112>=<=d1","lsddl,<,>=,1,<,>=,112,>=,<=,d1,<EOF>",133))
    def test_operator4(self):
        self.assertTrue(TestLexer.checkLexeme("13ek3<9e=9eend<>=Edasdndm<=>erE","13,ek3,<,9,e,Error Token =",134))
    def test_operator5(self):
        self.assertTrue(TestLexer.checkLexeme("djeiwjd1A<=>12>=<=d","djeiwjd1A,<=,>,12,>=,<=,d,<EOF>",135))
    def test_operator6(self):
        self.assertTrue(TestLexer.checkLexeme("<-mod>=not+mod+and+not","<,-,mod,>=,not,+,mod,+,and,+,not,<EOF>",136))
    def test_operator7(self):
        self.assertTrue(TestLexer.checkLexeme("*and<=>mod</<=","*,and,<=,>,mod,<,Error Token /",137))
    def test_operator8(self):
        self.assertTrue(TestLexer.checkLexeme("=or<=<><>=-<=>","Error Token =",138))
    def test_operator9(self):
        self.assertTrue(TestLexer.checkLexeme("not<>=and>=mod<=-and","not,<,>=,and,>=,mod,<=,-,and,<EOF>",139))
    def test_operator10(self):
        self.assertTrue(TestLexer.checkLexeme("mod<=<===mod/<=<","mod,<=,<=,==,mod,Error Token /",140))


    def test_illegal_escape1(self):
        self.assertTrue(TestLexer.checkLexeme("\"bac\\ma\"","Illegal Escape In String: bac\\m",141))
    def test_illegal_escape2(self):
        self.assertTrue(TestLexer.checkLexeme("\"baMD\\HLSc\\na\"","Illegal Escape In String: baMD\\H",142))
    def test_illegal_escape3(self):
        self.assertTrue(TestLexer.checkLexeme("\",dls\\F12!LS\\kc\\na\"","Illegal Escape In String: ,dls\\F",143))
    def test_illegal_escape4(self):
        self.assertTrue(TestLexer.checkLexeme("\"ado\\mado\"","Illegal Escape In String: ado\\m",144))
    def test_illegal_escape5(self):
        self.assertTrue(TestLexer.checkLexeme("123abc \"xyz\k 456","123,abc,Illegal Escape In String: xyz\\k",145))
    def test_illegal_escape6(self):
        self.assertTrue(TestLexer.checkLexeme("\"aa\wb\"","Illegal Escape In String: aa\\w",146))
    def test_illegal_escape7(self):
        self.assertTrue(TestLexer.checkLexeme("ba+12+\"na\"\"md+1.2-468\lb","ba,+,12,+,\"na\",Illegal Escape In String: md+1.2-468\\l",147))
    def test_illegal_escape8(self):
        self.assertTrue(TestLexer.checkLexeme("\"1.2+1.3+1.4\\o'\"123","Illegal Escape In String: 1.2+1.3+1.4\\o",148))
    def test_illegal_escape9(self):
        self.assertTrue(TestLexer.checkLexeme("**nac**+1.1 \"ba\\qm\f\"","+,1.1,Illegal Escape In String: ba\\q",149))
    def test_illegal_escape10(self):
        self.assertTrue(TestLexer.checkLexeme("\"concaheo\\uabc","Illegal Escape In String: concaheo\\u",150))

    def test_unclose_String1(self):
        self.assertTrue(TestLexer.checkLexeme("\"bacxyc","Unclosed String: bacxyc",151))
    def test_unclose_String2(self):
        self.assertTrue(TestLexer.checkLexeme("NmkobYn{!}+I1+\"`YS2h.J(","Error Token N",152))
    def test_unclose_String3(self):
        self.assertTrue(TestLexer.checkLexeme("\"acnv \" \"abc","\"acnv \",Unclosed String: abc",153))
    def test_unclose_String4(self):
        self.assertTrue(TestLexer.checkLexeme("\"acms!,lds \" {\"abc\"} 123\"abc","\"acms!,lds \",{,\"abc\",},123,Unclosed String: abc",154))
    def test_unclose_String5(self):
        self.assertTrue(TestLexer.checkLexeme("a+11.2+\"mam.123\" 12 \"%^&","a,+,11.2,+,\"mam.123\",12,Unclosed String: %^&",155))
    def test_unclose_String6(self):
        self.assertTrue(TestLexer.checkLexeme("38n\"[#Ffs?0ED\"0.\"T`#!7n","38,n,\"[#Ffs?0ED\",0.,Unclosed String: T`#!7n",156))
    def test_unclose_String7(self):
        self.assertTrue(TestLexer.checkLexeme("\".Hub`22Y\"<{;}\"Y`=DxXhZKh","\".Hub`22Y\",<,{,;,},Unclosed String: Y`=DxXhZKh",157))
    def test_unclose_String8(self):
        self.assertTrue(TestLexer.checkLexeme("\"ULxM*`~.~+C_DISD2","Unclosed String: ULxM*`~.~+C_DISD2",158))
    def test_unclose_String9(self):
        self.assertTrue(TestLexer.checkLexeme("{SRs}\"Nk8U;\"rA\"@Y3*\"oV\"bh1","{,Error Token S",159))
    def test_unclose_String10(self):
        self.assertTrue(TestLexer.checkLexeme("\"o|F&)LqX\"+>X+\"#Fft","\"o|F&)LqX\",+,>,Error Token X",160))


    def test_integer_real1(self):
        self.assertTrue(TestLexer.checkLexeme("12.e5","12.e5,<EOF>",161))
    def test_integer_real2(self):
        self.assertTrue(TestLexer.checkLexeme("01","0,1,<EOF>",162))
    def test_integer_real3(self):
        #TODO: fix -42
        self.assertTrue(TestLexer.checkLexeme("Var x0.12e51.2","Var,x0,.,12e51,.,2,<EOF>",163))
    def test_integer_real4(self):
        self.assertTrue(TestLexer.checkLexeme(".",".,<EOF>",164))
    def test_integer_real5(self):
        #TODO:  fix -15
        self.assertTrue(TestLexer.checkLexeme("e--12 e12 E-15 99e 1 1. 1","e,-,-,12,e12,Error Token E",165))
    def test_integer_real6(self):
        self.assertTrue(TestLexer.checkLexeme("e-12.1 11.e11 12..12 2. .2 11e11 .1e-3","e,-,12.1,11.e11,12.,.,12,2.,.,2,11e11,.,1e-3,<EOF>",166))
    def test_integer_real7(self):
        self.assertTrue(TestLexer.checkLexeme("12.e0 -101 11.E 11.1e2","12.e0,-,101,11.,Error Token E",167))


    def test_comment1(self):
        self.assertTrue(TestLexer.checkLexeme("**12.e0 -101** 11.e 11.1e2","11.,e,11.1e2,<EOF>",168))
    def test_comment2(self):
        self.assertTrue(TestLexer.checkLexeme("**12.e0} -101** 11.1e2","11.1e2,<EOF>",169))
    def test_comment3(self):
        self.assertTrue(TestLexer.checkLexeme("{abc} 1.abc","{,abc,},1.,abc,<EOF>",170))
    def test_comment4(self):
        self.assertTrue(TestLexer.checkLexeme("**1.e0 - 101** {11.E} //22.12\\n","{,11.,Error Token E",171))
    def test_comment5(self):
        #TODO: Fix reallit , intlit
        self.assertTrue(TestLexer.checkLexeme("**12.e0\\nabc -101","",172))
    def test_comment6(self):
        self.assertTrue(TestLexer.checkLexeme("13ek3<9e=9eendE//dasd1.ndm<>d1.02erE","13,ek3,<,9,e,Error Token =",173))
    def test_comment7(self):
        self.assertTrue(TestLexer.checkLexeme("//dasd1.ndm\\n<>d1.02erE","Error Token /",174))
    def test_comment8(self):
        self.assertTrue(TestLexer.checkLexeme("{ +abc<>xyzb>cv } **12mds<>dsd=(*dsd*)*)**","*,),*{,+,abc,<,>,xyzb,>,cv,},<EOF>",175))
    def test_comment9(self):
        self.assertTrue(TestLexer.checkLexeme(""" * **""","\"**\",<EOF>",176))
    def test_comment10(self):
        self.assertTrue(TestLexer.checkLexeme("*** **","",177))
    def test_comment11(self):
        self.assertTrue(TestLexer.checkLexeme("***** \"\"\"","<EOF>",178))
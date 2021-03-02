import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_1_var_decl(self):
        """ Test Var Declare 1 line 1 var """
        input = r"""
Var : a= 3;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_2_var_decl(self):
        """ Test Var Declare 1 line n var """
        input = r"""
Var :a, b, c= 4;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_3_var_decl(self):
        """ Test Var Declare n line """
        input = r"""
Var :a, b, c= 3;
Var :x, y= 3.e2;
Var :z= "string";
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_4_Var_decl(self):
        """ Test Var Declare array """
        input = r"""
Var :a ,  array[1][3] ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_5_Var_decl(self):
        """ Test Var Declare """
        input = r"""
Var :a, B, c,array[1][3]  ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_6_Var_decl(self):
        """ Test Var Declare """
        input = r"""
Var : a, B, c = 3;
 Var : z = False ;
 Var   :garray[1][3] ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_var_dec3(self):
        input = """Var:m,n[10] ; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 97))

    def test_var_dec2(self):
        input = """Var: c,d = 6,e,f ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 98))

    def test_var_dec1(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 99))

    def test_var_dec(self):
        input = """Var: a=5 ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 100))

    def test_simple_program(self):
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

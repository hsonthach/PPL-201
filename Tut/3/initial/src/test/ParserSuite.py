import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_var(self):
        input = """
            int c; float F;     int wqdas, sadadqAD, sadad;
            float joqeo123_213;
            int qweqw;  int asdqwe


            ;   float qweqwe                             ;


        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 200))

    def test_var1(self):
        input = """
            int   ;
        """
        expect = "Error on line 2 col 18: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_var3(self):
        input = """
            int a
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_var4(self):
        input = """
            int a, b,   c,      d
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_var5(self):
        input = """
            int float, y, x;
        """
        expect = "Error on line 2 col 16: float"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_var6(self):
        input = """
            int a, b, c;
            float x, y, z;
            int         float;
        """
        expect = "Error on line 4 col 24: float"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_func(self):
        input = """
            int foo() {}
            
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_func_error_1(self):
        input = """
            int foo()
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_func_error_2(self):
        input = """
            int foo() {
        """
        expect = "Error on line 3 col 8: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_func_error_3(self):
        input = """
            int foo() }
        """
        expect = "Error on line 2 col 22: }"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_func_error_4(self):
        input = """
            int foo {}
        """
        expect = "Error on line 2 col 20: {"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_func_error_5(self):
        input = """
            int foo(int) {}
        """
        expect = "Error on line 2 col 23: )"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_func_error_6(self):
        input = """
            int foo(int x;) {}
        """
        expect = "Error on line 2 col 26: )"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_func_error_7(self):
        input = """
            int foo(float x,) {}
        """
        expect = "Error on line 2 col 28: )"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_statement(self):
        input = """
            int main() {
                int a;
                float b;
                int a, b, c, d, e;
                float x, y, z, u, v;
                a = 0; 
                b= 0 ;
                c= 0 ;
                return a+b+c;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

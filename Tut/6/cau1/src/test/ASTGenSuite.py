import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """array[1]of int a,b;"""
        expect = "11"
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

    def test_more_complicated_program(self):
        """Simple program: int main() {} """
        input = """array[1] of int a,b;
        			int c,d;
        			float m;"""
        expect = "19"
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    
   
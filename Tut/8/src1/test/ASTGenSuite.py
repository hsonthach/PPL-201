import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """a := 4=b+=6"""
        expect = """Binary( := , Id(a), Binary( := , Id(b), IntLiteral(4)))"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

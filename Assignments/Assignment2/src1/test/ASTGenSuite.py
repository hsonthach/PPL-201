import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int a;"""
        expect = """Program([VarDecl(Id(a),IntType)])"""
        self.assertTrue(TestAST.checkASTGen(input, expect, 300))

import unittest
from TestUtils import TestChecker
from AST import *


class CheckSuite(unittest.TestCase):
    # def test_401(self):
    #     input = Program([
    #         VarDecl("a", IntType()),
    #         ConstDecl("b", IntLit(3)),
    #         FuncDecl("a", [], [])
    #     ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 401))
    def test_401(self):
        input = BinOp("/", BinOp("/", IntLit(3), IntLit(3)), IntLit(3))
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_402(self):
        input = BinOp("/", IntLit(3), BoolLit(False))
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))

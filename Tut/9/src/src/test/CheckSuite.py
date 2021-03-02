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
    # def test_401(self):
    #     input = Program([VarDecl("x")], [Assign(Id("x"), BinOp(
    #         "*", BinOp("+", Id("x"), IntLit(3.4)), BinOp("-", Id("x"), FloatLit(2.1))))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_402(self):
    #     input = Program([VarDecl("x"), VarDecl("y"), VarDecl("z")], [Assign(Id("x"), BinOp(">b", BinOp("&&", Id(
    #         "x"), Id("y")), BinOp("||", BoolLit(False), BinOp(">", Id("z"), IntLit(3))))), Assign(Id("z"), Id("x"))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_403(self):
    #     input = Program([VarDecl("x"), VarDecl("y")],
    #                     [Assign(Id("x"), Id("y"))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    # def test_403(self):
    #     input = Program([VarDecl("x"), VarDecl("y")],
    #                     [Assign(Id("x"), Id("y"))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 401))

    def test_403(self):
        input = Program([VarDecl("x"), VarDecl("y"), VarDecl("z")], [Assign(
            Id("t"), BinOp("||", BoolLit(True), BinOp(">", IntLit(3), Id("z"))))])

        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 401))

# def test_404(self):
#     input = Program([VarDecl("x"), VarDecl("y"), VarDecl("z"), VarDecl('k'), VarDecl('l'), VarDecl('m')],
#                     [Assign(Id("x"), BinOp(">b", BinOp("&&", Id("x"), Id("y")),
#                                            BinOp("||", BoolLit(False),
#                                                  BinOp(">", Id("z"),
#                                                        IntLit(3))))),
#                      Assign(Id("z"), Id("k")), Assign(Id('m'), UnOp('-.', Id('m')))])
#     expect = ""
#     self.assertTrue(TestChecker.test(input, expect, 401))

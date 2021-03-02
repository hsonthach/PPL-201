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

        x = Id('x')
        a = Id('a')
        b = Id('b')
        c = Id('c')
        y = Id('y')
        z = Id('z')
        m = Id('m')
        n = Id('n')

        input = Program([
            VarDecl("x"), VarDecl("y"), VarDecl("z"),
            FuncDecl('test',
                     [
                         VarDecl("a")
                     ],
                     [

                     ],
                     [
                         Assign(a, IntLit(3))
                     ]
                     )
        ],
            [
            CallStmt('test',
                     [
                         y
                     ]),
            Assign(y, FloatLit(3))
        ])
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

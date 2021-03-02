import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *


float_lit = FloatLiteral(3)
int_lit = IntLiteral(3)

bool_lit = BooleanLiteral(False)


array_lit1 = ArrayLiteral([IntLiteral(1), IntLiteral(2)])
array_lit2 = ArrayLiteral([IntLiteral(1), int_lit, int_lit])
array_lit3 = ArrayLiteral([array_lit2, array_lit2])  # [2][3]

list_of_func_decl = [
    FuncDecl(Id("func1"), [], ([], [])),
    FuncDecl(Id("func2"), [], ([], [])),
    FuncDecl(Id("func3"), [], ([], [])),
    FuncDecl(Id("func4"), [], ([], [])),
]
list_of_var_decl = [
    VarDecl(Id("id1"), [], None),
    VarDecl(Id("id2"), [], None),
    VarDecl(Id("id3"), [], None),
    VarDecl(Id("id4"), [], None),
    VarDecl(Id("id5"), [], None),
    VarDecl(Id("id6"), [], None),
    VarDecl(Id("arr1"), [1], array_lit1),
    VarDecl(Id("arr2"), [1], array_lit1),

]

list_of_param = [
    VarDecl(Id("param1"), [], None),
    VarDecl(Id("param2"), [], None),
    VarDecl(Id("param3"), [], None),
]


class CheckSuite(unittest.TestCase):

    # def test_no_entry_point(self):
    #     """Complex program"""
    #     input = Program([
    #         FuncDecl(Id("test"), [], ([], [
    #             CallStmt(Id("printStrLn"), [])]))])
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_list_of_func(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], ([], [])), *list_of_func_decl])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_reclared(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("func1"), [], ([], [])), *list_of_func_decl])
    #     expect = str(Redeclared(Function(), "func1"))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_reclared_1(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             For(Id('id1'), int_lit, BinaryOp('<', Id('id1'), int_lit), int_lit,
    #                 (
    #                 [
    #                     VarDecl(Id('id1'), [], None),
    #                     VarDecl(Id('main'), [], None),
    #                     VarDecl(Id('c'), [], None),
    #                     VarDecl(Id('c'), [], None),
    #                 ],
    #                 [

    #                 ]
    #             ))
    #         ]))])
    #     expect = str(Redeclared(Variable(), 'c'))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_reclared_param(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [VarDecl(Id("id1"), [], None), *list_of_var_decl], ([], []))])
    #     expect = str(Redeclared(Parameter(), "id1"))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_reclared_var(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], ([VarDecl(Id("id1"), [], None), *list_of_var_decl], []))])
    #     expect = str(Redeclared(Variable(), "id1"))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_array_lit(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], ([VarDecl(Id("id1"), [], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))], []))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_array_lit1(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], ([VarDecl(Id("id1"), [], ArrayLiteral([array_lit1, array_lit1]))], []))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_array_lit2(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           Assign(Id('id1'), array_lit1),
    #                                           Assign(Id('id1'), array_lit2),
    #                                       ]
    #                                       )),
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                  ]
    #                                                  )),

    #         ])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id1'), array_lit2)))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_lit3(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           Assign(Id('id1'), array_lit1),
    #                                           Assign(Id('id1'), array_lit3),
    #                                       ]
    #                                       )),
    #         ])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id1'), array_lit3)))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_assign_stmt(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), IntLiteral(3))
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_assign_stmt1(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), IntLiteral(3)),
    #             Assign(Id('id1'), FloatLiteral(3))
    #         ]))])
    #     expect = str(TypeMismatchInStatement(
    #         Assign(Id('id1'), FloatLiteral(3))))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_assign_stmt2(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), array_lit1),
    #             Assign(Id('id1'), array_lit1),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_assign_stmt3(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), IntLiteral(3)),
    #             Assign(Id('id2'), Id('id1')),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_assign_stmt4(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), IntLiteral(3)),
    #             Assign(Id('id2'), Id('id2')),
    #         ]))])
    #     expect = str(TypeCannotBeInferred(Assign(Id('id2'), Id('id2'))))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_assign_stmt5(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), IntLiteral(3)),
    #             Assign(Id('id1'), Id('id2')),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_assign_stmt6(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), IntLiteral(3)),
    #             Assign(Id('id1'), Id('id2')),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_assign_stmt7(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), array_lit1),
    #             Assign(Id('id1'), int_lit),
    #         ]))])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id1'), int_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op1(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), FloatLiteral(3)),
    #             Assign(Id('id1'), BinaryOp('+', IntLiteral(3), IntLiteral(4))),
    #         ]))])
    #     expect = str(TypeMismatchInStatement(
    #         Assign(Id('id1'), BinaryOp('+', IntLiteral(3), IntLiteral(4)))))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op2(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), FloatLiteral(3)),
    #             Assign(Id('id1'), BinaryOp(
    #                 '+', IntLiteral(3), FloatLiteral(4))),
    #         ]))])
    #     expect = str(TypeMismatchInExpression(
    #         BinaryOp(
    #             '+', IntLiteral(3), FloatLiteral(4))))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op3(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), int_lit),
    #             Assign(Id('id1'), BinaryOp(
    #                 '+', Id('id2'), Id('id3'))),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op4(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), int_lit),
    #             Assign(Id('id1'), BinaryOp(
    #                 '+', Id('id2'), float_lit)),
    #         ]))])
    #     expect = str(TypeMismatchInExpression(BinaryOp(
    #         '+', Id('id2'), float_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op5(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), int_lit),
    #             Assign(Id('id1'), BinaryOp(
    #                 '+', Id('id2'), int_lit)),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op6(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id1'), BinaryOp(
    #                 '+.', float_lit, float_lit)),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op7(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id1'), BinaryOp('+.', Id('id2'), Id('id3'))),
    #             Assign(Id('id2'), int_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id2'), int_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op8(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), BinaryOp('>=', Id('id2'), Id('id3'))),
    #             Assign(Id('id4'), float_lit),

    #         ]))])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id4'), float_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op9(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), BinaryOp('>=', Id('id2'), float_lit)),

    #         ]))])
    #     expect = str(TypeMismatchInExpression(
    #         BinaryOp('>=', Id('id2'), float_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op10(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), BinaryOp('=/=', Id('id2'), float_lit)),

    #         ]))])
    #     expect = ''
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op11(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), BinaryOp('=/=', Id('id2'), bool_lit)),

    #         ]))])
    #     expect = str(TypeMismatchInExpression(
    #         BinaryOp('=/=', Id('id2'), bool_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op12(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), BinaryOp('=/=', Id('id2'), Id('id3'))),
    #             Assign(Id('id4'), bool_lit)
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op13(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), BinaryOp('&&', Id('id2'), Id('id3'))),
    #             Assign(Id('id4'), bool_lit)
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op14(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), BinaryOp('&&', bool_lit, Id('id3'))),
    #             Assign(Id('id4'), bool_lit)
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_bin_op15(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), BinaryOp('&&', bool_lit, Id('id3'))),
    #             Assign(Id('id3'), float_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id3'), float_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_unary_op(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), UnaryOp('-', int_lit)),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_unary_op1(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), UnaryOp('-', int_lit)),
    #             Assign(Id('id4'), int_lit),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_unary_op2(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), UnaryOp('-.', float_lit)),
    #             Assign(Id('id4'), float_lit),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_unary_op3(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), float_lit),
    #             Assign(Id('id4'), UnaryOp('!', bool_lit)),
    #             Assign(Id('id4'), bool_lit),
    #         ]))])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_if_stmt(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             If(
    #                 # If
    #                 [
    #                     (
    #                         BinaryOp('==', Id('id1'), int_lit),
    #                         [
    #                             # Var declare
    #                         ],
    #                         [

    #                         ]
    #                     ),
    #                 ],
    #                 # Else
    #                 (
    #                     [

    #                     ],
    #                     [

    #                     ]
    #                 )
    #             ),
    #             Assign(Id('id1'), float_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id1'), float_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_if_stmt1(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             If(
    #                 # If
    #                 [
    #                     (
    #                         BinaryOp('==', Id('id1'), int_lit),
    #                         [
    #                             # Var declare
    #                             VarDecl(Id("id10"), [], None),
    #                         ],
    #                         [
    #                             Assign(Id('id10'), float_lit)
    #                         ]
    #                     ),
    #                 ],
    #                 # Else
    #                 (
    #                     [

    #                     ],
    #                     [
    #                         Assign(Id('id10'), float_lit)
    #                     ]
    #                 )
    #             ),
    #             Assign(Id('id1'), float_lit)
    #         ]))])
    #     expect = str(Undeclared(Identifier(), "id10"))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_if_stmt3(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             If(
    #                 # If
    #                 [
    #                     (
    #                         Id('id1'),
    #                         [
    #                             # Var declare
    #                         ],
    #                         [

    #                         ]
    #                     ),
    #                 ],
    #                 # Else
    #                 (
    #                     [

    #                     ],
    #                     [

    #                     ]
    #                 )
    #             ),
    #             Assign(Id('id1'), float_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id1'), float_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_for_stmt(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             For(Id('id10'), int_lit, BinaryOp('<', Id('id1'), int_lit), int_lit,
    #                 (
    #                 [

    #                 ],
    #                 [

    #                 ]
    #             )),
    #             Assign(Id('id1'), float_lit)
    #         ]))])
    #     expect = str(Undeclared(Identifier(), "id10"))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_for_stmt1(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             For(Id('id1'), int_lit, BinaryOp('-', Id('id1'), int_lit), int_lit,
    #                 (
    #                 [

    #                 ],
    #                 [

    #                 ]
    #             )),
    #             Assign(Id('id1'), float_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(
    #         For(Id('id1'), int_lit, BinaryOp('-', Id('id1'), int_lit), int_lit, ([], []))))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_for_stmt2(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             For(Id('id1'), int_lit, BinaryOp('<', Id('id1'), int_lit), float_lit,
    #                 (
    #                 [

    #                 ],
    #                 [

    #                 ]
    #             )),
    #             Assign(Id('id1'), float_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(
    #         For(Id('id1'), int_lit, BinaryOp('<', Id('id1'), int_lit), float_lit, ([], []))))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_for_stmt3(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             For(Id('id1'), float_lit, BinaryOp('<', Id('id1'), int_lit), int_lit,
    #                 (
    #                 [

    #                 ],
    #                 [

    #                 ]
    #             )),
    #             Assign(Id('id1'), float_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(
    #         For(Id('id1'), float_lit, BinaryOp('<', Id('id1'), int_lit), int_lit, ([], []))))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_for_stmt4(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             For(Id('id1'), int_lit, BinaryOp('<', Id('id1'), int_lit), int_lit,
    #                 (
    #                 [

    #                 ],
    #                 [

    #                 ]
    #             )),
    #             Assign(Id('id1'), float_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(
    #         Assign(Id('id1'), float_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_for_stmt5(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             For(Id('id1'), int_lit, BinaryOp('<', Id('id2'), int_lit), int_lit,
    #                 (
    #                 [

    #                 ],
    #                 [

    #                 ]
    #             )),
    #             Assign(Id('id2'), float_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(
    #         Assign(Id('id2'), float_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_for_stmt6(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             For(Id('id1'), int_lit, BinaryOp('<', Id('id2'), int_lit), int_lit,
    #                 (
    #                 [
    #                     VarDecl(Id("id10"), [], float_lit),
    #                 ],
    #                 [
    #                     Assign(Id('id10'), float_lit)
    #                 ]
    #             )),
    #             Assign(Id('id10'), int_lit)
    #         ]))])
    #     expect = str(Undeclared(Identifier(), "id10"))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_while_stmt(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             While(Id('id1'),
    #                   (
    #                 [

    #                 ],
    #                 [

    #                 ]
    #             )),
    #             Assign(Id('id1'), int_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id1'), int_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_while_stmt1(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), int_lit),
    #             While(Id('id1'),
    #                   (
    #                 [

    #                 ],
    #                 [

    #                 ]
    #             )),

    #         ]))])
    #     expect = str(TypeMismatchInStatement(While(Id('id1'), ([], []))))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_while_stmt2(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             While(Id('id1'),
    #                   (
    #                 [
    #                     VarDecl(Id('id10'), [], None)
    #                 ],
    #                 [
    #                     Assign(Id('id10'), int_lit)
    #                 ]
    #             )),
    #             Assign(Id('id10'), int_lit),

    #         ]))])
    #     expect = str(Undeclared(Identifier(), "id10"))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_do_while_stmt(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Dowhile(
    #                   (
    #                       [

    #                       ],
    #                       [

    #                       ]
    #                   ), Id('id1')),
    #             Assign(Id('id1'), int_lit)
    #         ]))])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id1'), int_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_do_while_stmt1(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Assign(Id('id1'), int_lit),
    #             Dowhile(
    #                   (
    #                       [

    #                       ],
    #                       [

    #                       ]
    #                   ), Id('id1'),),

    #         ]))])
    #     expect = str(TypeMismatchInStatement(Dowhile(
    #         (
    #             [

    #             ],
    #             [

    #             ]
    #         ), Id('id1'),)))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_do_while_stmt2(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl, [
    #             Dowhile(
    #                   (
    #                       [
    #                           VarDecl(Id('id10'), [], None)
    #                       ],
    #                       [
    #                           Assign(Id('id10'), int_lit)
    #                       ]
    #                   ), Id('id1'),),
    #             Assign(Id('id10'), int_lit),

    #         ]))])
    #     expect = str(Undeclared(Identifier(), "id10"))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_invoke_before_declare(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                    [
    #                                        # Stmts
    #                                        CallStmt(Id('test'), [])
    #                                    ]
    #                                    )),
    #             FuncDecl(Id("test"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                       ]
    #                                       ))
    #          ])
    #     expect = ''
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_recursive(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                    [
    #                                        # Stmts
    #                                        CallStmt(Id('main'), [])
    #                                    ]
    #                                    )),
    #          ])
    #     expect = ''
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_stmt(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                      Assign(
    #                                                          Id('param3'), int_lit)
    #                                                  ]
    #                                                  )),
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           CallStmt(Id('test'), [
    #                                               int_lit, int_lit, int_lit])
    #                                       ]
    #                                       )),

    #         ])
    #     expect = ''
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_stmt1(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                      Assign(
    #                                                          Id('param3'), int_lit)
    #                                                  ]
    #                                                  )),
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           CallStmt(Id('test'), [
    #                                               int_lit, int_lit, float_lit])
    #                                       ]
    #                                       )),

    #         ])
    #     expect = str(TypeMismatchInStatement(CallStmt(Id('test'), [
    #         int_lit, int_lit, float_lit])))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_stmt2(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                  ]
    #                                                  )),
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           CallStmt(Id('test'), [
    #                                               int_lit, int_lit, float_lit])
    #                                       ]
    #                                       )),

    #         ])
    #     expect = str(TypeCannotBeInferred(
    #         CallStmt(Id('test'), [int_lit, int_lit, float_lit])))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_stmt3(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           CallStmt(Id('test'), [
    #                                               int_lit, int_lit, float_lit])
    #                                       ]
    #                                       )),
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                  ]
    #                                                  )),

    #         ])
    #     expect = str(TypeCannotBeInferred(
    #         CallStmt(Id('test'), [int_lit, int_lit, float_lit])))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_stmt4(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           CallStmt(Id('test'), [
    #                                               int_lit, int_lit])
    #                                       ]
    #                                       )),
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                  ]
    #                                                  )),

    #         ])
    #     expect = str(TypeMismatchInStatement(
    #         CallStmt(Id('test'), [int_lit, int_lit])))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_exp(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           Assign(Id('id1'), CallExpr(Id('test'), [
    #                                               int_lit, int_lit, int_lit]))
    #                                       ]
    #                                       )),
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                      Assign(
    #                                                          Id('param3'), int_lit),
    #                                                      Return(Id('param1'))
    #                                                  ]
    #                                                  )),

    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_exp1(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           Assign(Id('id1'), CallExpr(Id('test'), [
    #                                               int_lit, int_lit, int_lit]))
    #                                       ]
    #                                       )),
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                      Assign(
    #                                                          Id('param3'), int_lit),
    #                                                  ]
    #                                                  )),

    #         ])
    #     expect = str(TypeMismatchInStatement(
    #         Assign(Id('id1'), CallExpr(Id('test'), [
    #             int_lit, int_lit, int_lit]))))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_exp2(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           Assign(Id('id1'), CallExpr(Id('test'), [
    #                                               int_lit, int_lit, int_lit])),
    #                                           Assign(Id('id1'), int_lit)
    #                                       ]
    #                                       )),
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                      Assign(
    #                                                          Id('param3'), int_lit),
    #                                                      Return(Id('param1'))
    #                                                  ]
    #                                                  )),

    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_exp3(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           Assign(Id('id1'), CallExpr(Id('test'), [
    #                                               int_lit, int_lit, int_lit])),
    #                                           Assign(Id('id1'), BinaryOp(
    #                                               '-', int_lit, Id('id1')))
    #                                       ]
    #                                       )),
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                      Assign(
    #                                                          Id('param3'), int_lit),
    #                                                      Return(Id('param1'))
    #                                                  ]
    #                                                  )),

    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_exp4(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           Assign(Id('id1'), CallExpr(Id('test'), [
    #                                               int_lit, int_lit, int_lit])),
    #                                           Assign(Id('id4'), BinaryOp(
    #                                               '-', int_lit, Id('id1')))
    #                                       ]
    #                                       )),
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                      Assign(
    #                                                          Id('param3'), int_lit),
    #                                                      Return(Id('param1'))
    #                                                  ]
    #                                                  )),

    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_index(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           Assign(Id('id1'), array_lit1),
    #                                           Assign(Id('id2'), ArrayCell(
    #                                               Id('id1'), [int_lit])),
    #                                       ]
    #                                       )),
    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_index1(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           # [2][3]
    #                                           Assign(Id('id1'), array_lit3),
    #                                           Assign(Id('id2'), ArrayCell(
    #                                               Id('id1'), [int_lit, int_lit])),
    #                                       ]
    #                                       )),
    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_index2(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           # [2][3]
    #                                           Assign(Id('id1'), array_lit3),
    #                                           Assign(Id('id2'), ArrayCell(
    #                                               Id('id1'), [int_lit, int_lit])),

    #                                           Assign(Id('id2'), int_lit)
    #                                       ]
    #                                       )),
    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_index3(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           # [2][3]
    #                                           Assign(Id('id1'), array_lit3),
    #                                           Assign(Id('id2'), ArrayCell(
    #                                               Id('id1'), [int_lit])),

    #                                           Assign(Id('id2'), int_lit)
    #                                       ]
    #                                       )),
    #         ])
    #     expect = str(TypeMismatchInExpression(ArrayCell(
    #         Id('id1'), [int_lit])))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_index4(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           # [2][3]
    #                                           Assign(Id('id1'), array_lit3),
    #                                           Assign(Id('id2'), ArrayCell(
    #                                               Id('id1'), [int_lit, int_lit, int_lit])),

    #                                           Assign(Id('id2'), int_lit)
    #                                       ]
    #                                       )),
    #         ])
    #     expect = str(TypeMismatchInExpression(ArrayCell(
    #         Id('id1'), [int_lit, int_lit, int_lit])))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_index6(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           # [2][3]
    #                                           Assign(Id('id1'), array_lit3),
    #                                           Assign(Id('id3'), bool_lit),

    #                                           Assign(Id('id2'), ArrayCell(
    #                                               Id('id3'), [int_lit, int_lit])),

    #                                       ]
    #                                       )),
    #         ])
    #     expect = str(TypeMismatchInExpression(ArrayCell(
    #         Id('id3'), [int_lit, int_lit])))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_index6(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           # [2][3]
    #                                           Assign(Id('id1'), array_lit3),
    #                                           Assign(Id('id2'), ArrayCell(
    #                                               Id('id1'), [Id('id3'), Id('id4')])),

    #                                       ]
    #                                       )),
    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_index7(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           # [2][3]
    #                                           Assign(Id('id1'), array_lit3),
    #                                           Assign(Id('id2'), ArrayCell(
    #                                               Id('id1'), [Id('id3'), Id('id4')])),
    #                                           Assign(Id('id3'), int_lit)
    #                                       ]
    #                                       )),
    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_array_index8(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           # [2][3]
    #                                           Assign(Id('id1'), array_lit3),
    #                                           Assign(Id('id2'), ArrayCell(
    #                                               Id('id1'), [Id('id3'), Id('id4')])),
    #                                           Assign(Id('id3'), float_lit)
    #                                       ]
    #                                       )),
    #         ])
    #     expect = str(TypeMismatchInStatement(Assign(Id('id3'), float_lit)))
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_call_exp5(self):
    #     """Complex program"""
    #     input = Program(
    #         [
    #             FuncDecl(Id("main"), [], (list_of_var_decl,
    #                                       [
    #                                           # Stmts
    #                                           Assign(Id('id1'), CallExpr(Id('test'), [
    #                                               int_lit, int_lit, int_lit])),
    #                                           Assign(Id('id4'), BinaryOp(
    #                                               '-', int_lit, CallExpr(Id('test'), [
    #                                                   int_lit, int_lit, int_lit])))
    #                                       ]
    #                                       )),
    #             FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
    #                                                  [
    #                                                      # Stmts
    #                                                      Assign(
    #                                                          Id('param1'), int_lit),
    #                                                      Assign(
    #                                                          Id('param2'), int_lit),
    #                                                      Assign(
    #                                                          Id('param3'), int_lit),
    #                                                      Return(Id('param1'))
    #                                                  ]
    #                                                  )),

    #         ])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 499))

    # def test_list_of_var(self):
    #     """Complex program"""
    #     input = Program(
    #         [*list_of_var_decl, FuncDecl(Id("main"), [], ([], [])), *list_of_func_decl])
    #     expect = ""
    #     self.assertTrue(TestChecker.test(input, expect, 405))

    # def test_redeclared(self):
    #     """Complex program"""
    #     input = Program(
    #         [FuncDecl(Id("main"), [], ([*list_of_var_decl, *list_of_var_decl], [])), *list_of_func_decl])
    #     expect = str(Redeclared(Variable(), "id1"))
    #     self.assertTrue(TestChecker.test(input, expect, 405))

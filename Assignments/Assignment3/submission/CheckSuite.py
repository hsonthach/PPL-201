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

    def test_no_entry_point(self):
        """Complex program"""
        input = Program([
            FuncDecl(Id("test"), [], ([], [
                CallStmt(Id("printStrLn"), [])]))])
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_list_of_func(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], ([], [])), *list_of_func_decl])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_reclared(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("func1"), [], ([], [])), *list_of_func_decl])
        expect = str(Redeclared(Function(), "func1"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_reclared_1(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                For(Id('id1'), int_lit, BinaryOp('<', Id('id1'), int_lit), int_lit,
                    (
                    [
                        VarDecl(Id('id1'), [], None),
                        VarDecl(Id('main'), [], None),
                        VarDecl(Id('c'), [], None),
                        VarDecl(Id('c'), [], None),
                    ],
                    [

                    ]
                ))
            ]))])
        expect = str(Redeclared(Variable(), 'c'))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_reclared_param(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [VarDecl(Id("id1"), [], None), *list_of_var_decl], ([], []))])
        expect = str(Redeclared(Parameter(), "id1"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_reclared_var(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], ([VarDecl(Id("id1"), [], None), *list_of_var_decl], []))])
        expect = str(Redeclared(Variable(), "id1"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_array_lit(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], ([VarDecl(Id("id1"), [], ArrayLiteral([IntLiteral(1), IntLiteral(2)]))], []))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_array_lit1(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], ([VarDecl(Id("id1"), [], ArrayLiteral([array_lit1, array_lit1]))], []))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_array_lit2(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              Assign(
                                                  Id('id1'), array_lit1),
                                              Assign(
                                                  Id('id1'), array_lit2),
                                          ]
                                          )),
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                     ]
                                                     )),

            ])
        expect = str(TypeMismatchInStatement(
            Assign(Id('id1'), array_lit2)))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_lit3(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              Assign(
                                                  Id('id1'), array_lit1),
                                              Assign(
                                                  Id('id1'), array_lit3),
                                          ]
                                          )),
            ])
        expect = str(TypeMismatchInStatement(
            Assign(Id('id1'), array_lit3)))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_assign_stmt(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), IntLiteral(3))
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_stmt1(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), IntLiteral(3)),
                Assign(Id('id1'), FloatLiteral(3))
            ]))])
        expect = str(TypeMismatchInStatement(
            Assign(Id('id1'), FloatLiteral(3))))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_stmt2(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), array_lit1),
                Assign(Id('id1'), array_lit1),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_stmt3(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), IntLiteral(3)),
                Assign(Id('id2'), Id('id1')),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_stmt4(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), IntLiteral(3)),
                Assign(Id('id2'), Id('id2')),
            ]))])
        expect = str(TypeCannotBeInferred(Assign(Id('id2'), Id('id2'))))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_stmt5(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), IntLiteral(3)),
                Assign(Id('id1'), Id('id2')),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_stmt6(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), IntLiteral(3)),
                Assign(Id('id1'), Id('id2')),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_assign_stmt7(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), array_lit1),
                Assign(Id('id1'), int_lit),
            ]))])
        expect = str(TypeMismatchInStatement(Assign(Id('id1'), int_lit)))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op1(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), FloatLiteral(3)),
                Assign(Id('id1'), BinaryOp(
                    '+', IntLiteral(3), IntLiteral(4))),
            ]))])
        expect = str(TypeMismatchInStatement(
            Assign(Id('id1'), BinaryOp('+', IntLiteral(3), IntLiteral(4)))))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op2(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), FloatLiteral(3)),
                Assign(Id('id1'), BinaryOp(
                    '+', IntLiteral(3), FloatLiteral(4))),
            ]))])
        expect = str(TypeMismatchInExpression(
            BinaryOp(
                '+', IntLiteral(3), FloatLiteral(4))))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op3(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), int_lit),
                Assign(Id('id1'), BinaryOp(
                    '+', Id('id2'), Id('id3'))),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op4(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), int_lit),
                Assign(Id('id1'), BinaryOp(
                    '+', Id('id2'), float_lit)),
            ]))])
        expect = str(TypeMismatchInExpression(BinaryOp(
            '+', Id('id2'), float_lit)))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op5(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), int_lit),
                Assign(Id('id1'), BinaryOp(
                    '+', Id('id2'), int_lit)),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op6(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id1'), BinaryOp(
                    '+.', float_lit, float_lit)),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op7(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id1'), BinaryOp('+.', Id('id2'), Id('id3'))),
                Assign(Id('id2'), int_lit)
            ]))])
        expect = str(TypeMismatchInStatement(Assign(Id('id2'), int_lit)))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op8(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), BinaryOp('>=', Id('id2'), Id('id3'))),
                Assign(Id('id4'), float_lit),

            ]))])
        expect = str(TypeMismatchInStatement(Assign(Id('id4'), float_lit)))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op9(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), BinaryOp('>=', Id('id2'), float_lit)),

            ]))])
        expect = str(TypeMismatchInExpression(
            BinaryOp('>=', Id('id2'), float_lit)))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op10(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), BinaryOp('=/=', Id('id2'), float_lit)),

            ]))])
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op11(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), BinaryOp('=/=', Id('id2'), bool_lit)),

            ]))])
        expect = str(TypeMismatchInExpression(
            BinaryOp('=/=', Id('id2'), bool_lit)))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op12(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), BinaryOp('=/=', Id('id2'), Id('id3'))),
                Assign(Id('id4'), bool_lit)
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op13(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), BinaryOp('&&', Id('id2'), Id('id3'))),
                Assign(Id('id4'), bool_lit)
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op14(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), BinaryOp('&&', bool_lit, Id('id3'))),
                Assign(Id('id4'), bool_lit)
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_bin_op15(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), BinaryOp('&&', bool_lit, Id('id3'))),
                Assign(Id('id3'), float_lit)
            ]))])
        expect = str(TypeMismatchInStatement(Assign(Id('id3'), float_lit)))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_unary_op(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), UnaryOp('-', int_lit)),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_unary_op1(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), UnaryOp('-', int_lit)),
                Assign(Id('id4'), int_lit),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_unary_op2(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), UnaryOp('-.', float_lit)),
                Assign(Id('id4'), float_lit),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_unary_op3(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), float_lit),
                Assign(Id('id4'), UnaryOp('!', bool_lit)),
                Assign(Id('id4'), bool_lit),
            ]))])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_if_stmt(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                If(
                    # If
                    [
                        (
                            BinaryOp('==', Id('id1'), int_lit),
                            [
                                # Var declare
                            ],
                            [

                            ]
                        ),
                    ],
                    # Else
                    (
                        [

                        ],
                        [

                        ]
                    )
                ),
                Assign(Id('id1'), float_lit)
            ]))])
        expect = str(TypeMismatchInStatement(Assign(Id('id1'), float_lit)))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_if_stmt1(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                If(
                    # If
                    [
                        (
                            BinaryOp('==', Id('id1'), int_lit),
                            [
                                # Var declare
                                VarDecl(Id("id10"), [], None),
                            ],
                            [
                                Assign(Id('id10'), float_lit)
                            ]
                        ),
                    ],
                    # Else
                    (
                        [

                        ],
                        [
                            Assign(Id('id10'), float_lit)
                        ]
                    )
                ),
                Assign(Id('id1'), float_lit)
            ]))])
        expect = str(Undeclared(Identifier(), "id10"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_if_stmt3(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                If(
                    # If
                    [
                        (
                            Id('id1'),
                            [
                                # Var declare
                            ],
                            [

                            ]
                        ),
                    ],
                    # Else
                    (
                        [

                        ],
                        [

                        ]
                    )
                ),
                Assign(Id('id1'), float_lit)
            ]))])
        expect = str(TypeMismatchInStatement(Assign(Id('id1'), float_lit)))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_for_stmt(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                For(Id('id10'), int_lit, BinaryOp('<', Id('id1'), int_lit), int_lit,
                    (
                    [

                    ],
                    [

                    ]
                )),
                Assign(Id('id1'), float_lit)
            ]))])
        expect = str(Undeclared(Identifier(), "id10"))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_for_stmt1(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                For(Id('id1'), int_lit, BinaryOp('-', Id('id1'), int_lit), int_lit,
                    (
                    [

                    ],
                    [

                    ]
                )),
                Assign(Id('id1'), float_lit)
            ]))])
        expect = str(TypeMismatchInStatement(
            For(Id('id1'), int_lit, BinaryOp('-', Id('id1'), int_lit), int_lit, ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_for_stmt2(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                For(Id('id1'), int_lit, BinaryOp('<', Id('id1'), int_lit), float_lit,
                    (
                    [

                    ],
                    [

                    ]
                )),
                Assign(Id('id1'), float_lit)
            ]))])
        expect = str(TypeMismatchInStatement(
            For(Id('id1'), int_lit, BinaryOp('<', Id('id1'), int_lit), float_lit, ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_for_stmt3(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                For(Id('id1'), float_lit, BinaryOp('<', Id('id1'), int_lit), int_lit,
                    (
                    [

                    ],
                    [

                    ]
                )),
                Assign(Id('id1'), float_lit)
            ]))])
        expect = str(TypeMismatchInStatement(
            For(Id('id1'), float_lit, BinaryOp('<', Id('id1'), int_lit), int_lit, ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_for_stmt4(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                For(Id('id1'), int_lit, BinaryOp('<', Id('id1'), int_lit), int_lit,
                    (
                    [

                    ],
                    [

                    ]
                )),
                Assign(Id('id1'), float_lit)
            ]))])
        expect = str(TypeMismatchInStatement(
            Assign(Id('id1'), float_lit)))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_for_stmt5(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                For(Id('id1'), int_lit, BinaryOp('<', Id('id2'), int_lit), int_lit,
                    (
                    [

                    ],
                    [

                    ]
                )),
                Assign(Id('id2'), float_lit)
            ]))])
        expect = str(TypeMismatchInStatement(
            Assign(Id('id2'), float_lit)))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_for_stmt6(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                For(Id('id1'), int_lit, BinaryOp('<', Id('id2'), int_lit), int_lit,
                    (
                    [
                        VarDecl(Id("id10"), [], float_lit),
                    ],
                    [
                        Assign(Id('id10'), float_lit)
                    ]
                )),
                Assign(Id('id10'), int_lit)
            ]))])
        expect = str(Undeclared(Identifier(), "id10"))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_while_stmt(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                While(Id('id1'),
                      (
                    [

                    ],
                    [

                    ]
                )),
                Assign(Id('id1'), int_lit)
            ]))])
        expect = str(TypeMismatchInStatement(Assign(Id('id1'), int_lit)))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_while_stmt1(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), int_lit),
                While(Id('id1'),
                      (
                    [

                    ],
                    [

                    ]
                )),

            ]))])
        expect = str(TypeMismatchInStatement(While(Id('id1'), ([], []))))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_while_stmt2(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                While(Id('id1'),
                      (
                    [
                        VarDecl(Id('id10'), [], None)
                    ],
                    [
                        Assign(Id('id10'), int_lit)
                    ]
                )),
                Assign(Id('id10'), int_lit),

            ]))])
        expect = str(Undeclared(Identifier(), "id10"))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_do_while_stmt(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Dowhile(
                      (
                          [

                          ],
                          [

                          ]
                      ), Id('id1')),
                Assign(Id('id1'), int_lit)
            ]))])
        expect = str(TypeMismatchInStatement(Assign(Id('id1'), int_lit)))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_do_while_stmt1(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Assign(Id('id1'), int_lit),
                Dowhile(
                      (
                          [

                          ],
                          [

                          ]
                      ), Id('id1'),),

            ]))])
        expect = str(TypeMismatchInStatement(Dowhile(
            (
                [

                ],
                [

                ]
            ), Id('id1'),)))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_do_while_stmt2(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl, [
                Dowhile(
                      (
                          [
                              VarDecl(Id('id10'), [], None)
                          ],
                          [
                              Assign(Id('id10'), int_lit)
                          ]
                      ), Id('id1'),),
                Assign(Id('id10'), int_lit),

            ]))])
        expect = str(Undeclared(Identifier(), "id10"))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_invoke_before_declare(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl,
                                       [
                                           # Stmts
                                           CallStmt(Id('test'), [])
                                       ]
                                       )),
                FuncDecl(Id("test"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                          ]
                                          ))
             ])
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_recursive(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], (list_of_var_decl,
                                       [
                                           # Stmts
                                           CallStmt(Id('main'), [])
                                       ]
                                       )),
             ])
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_stmt(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                         Assign(
                                                             Id('param3'), int_lit)
                                                     ]
                                                     )),
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              CallStmt(Id('test'), [
                                                  int_lit, int_lit, int_lit])
                                          ]
                                          )),

            ])
        expect = ''
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_stmt1(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                         Assign(
                                                             Id('param3'), int_lit)
                                                     ]
                                                     )),
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              CallStmt(Id('test'), [
                                                  int_lit, int_lit, float_lit])
                                          ]
                                          )),

            ])
        expect = str(TypeMismatchInStatement(CallStmt(Id('test'), [
            int_lit, int_lit, float_lit])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_stmt2(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                     ]
                                                     )),
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              CallStmt(Id('test'), [
                                                  int_lit, int_lit, float_lit])
                                          ]
                                          )),

            ])
        expect = str(TypeCannotBeInferred(
            CallStmt(Id('test'), [int_lit, int_lit, float_lit])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_stmt3(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              CallStmt(Id('test'), [
                                                  int_lit, int_lit, float_lit])
                                          ]
                                          )),
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                     ]
                                                     )),

            ])
        expect = str(TypeCannotBeInferred(
            CallStmt(Id('test'), [int_lit, int_lit, float_lit])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_stmt4(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              CallStmt(Id('test'), [
                                                  int_lit, int_lit])
                                          ]
                                          )),
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                     ]
                                                     )),

            ])
        expect = str(TypeMismatchInStatement(
            CallStmt(Id('test'), [int_lit, int_lit])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_exp(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              Assign(Id('id1'), CallExpr(Id('test'), [
                                                  int_lit, int_lit, int_lit]))
                                          ]
                                          )),
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                         Assign(
                                                             Id('param3'), int_lit),
                                                         Return(
                                                             Id('param1'))
                                                     ]
                                                     )),

            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_exp1(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              Assign(Id('id1'), CallExpr(Id('test'), [
                                                  int_lit, int_lit, int_lit]))
                                          ]
                                          )),
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                         Assign(
                                                             Id('param3'), int_lit),
                                                     ]
                                                     )),

            ])
        expect = str(TypeMismatchInStatement(
            Assign(Id('id1'), CallExpr(Id('test'), [
                int_lit, int_lit, int_lit]))))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_exp2(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              Assign(Id('id1'), CallExpr(Id('test'), [
                                                  int_lit, int_lit, int_lit])),
                                              Assign(Id('id1'), int_lit)
                                          ]
                                          )),
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                         Assign(
                                                             Id('param3'), int_lit),
                                                         Return(
                                                             Id('param1'))
                                                     ]
                                                     )),

            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_exp3(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              Assign(Id('id1'), CallExpr(Id('test'), [
                                                  int_lit, int_lit, int_lit])),
                                              Assign(Id('id1'), BinaryOp(
                                                  '-', int_lit, Id('id1')))
                                          ]
                                          )),
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                         Assign(
                                                             Id('param3'), int_lit),
                                                         Return(
                                                             Id('param1'))
                                                     ]
                                                     )),

            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_exp4(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              Assign(Id('id1'), CallExpr(Id('test'), [
                                                  int_lit, int_lit, int_lit])),
                                              Assign(Id('id4'), BinaryOp(
                                                  '-', int_lit, Id('id1')))
                                          ]
                                          )),
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                         Assign(
                                                             Id('param3'), int_lit),
                                                         Return(
                                                             Id('param1'))
                                                     ]
                                                     )),

            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_index(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              Assign(
                                                  Id('id1'), array_lit1),
                                              Assign(Id('id2'), ArrayCell(
                                                  Id('id1'), [int_lit])),
                                          ]
                                          )),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_index1(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              # [2][3]
                                              Assign(
                                                  Id('id1'), array_lit3),
                                              Assign(Id('id2'), ArrayCell(
                                                  Id('id1'), [int_lit, int_lit])),
                                          ]
                                          )),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_index2(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              # [2][3]
                                              Assign(
                                                  Id('id1'), array_lit3),
                                              Assign(Id('id2'), ArrayCell(
                                                  Id('id1'), [int_lit, int_lit])),

                                              Assign(Id('id2'), int_lit)
                                          ]
                                          )),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_index3(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              # [2][3]
                                              Assign(
                                                  Id('id1'), array_lit3),
                                              Assign(Id('id2'), ArrayCell(
                                                  Id('id1'), [int_lit])),

                                              Assign(Id('id2'), int_lit)
                                          ]
                                          )),
            ])
        expect = str(TypeMismatchInExpression(ArrayCell(
            Id('id1'), [int_lit])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_index4(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              # [2][3]
                                              Assign(
                                                  Id('id1'), array_lit3),
                                              Assign(Id('id2'), ArrayCell(
                                                  Id('id1'), [int_lit, int_lit, int_lit])),

                                              Assign(Id('id2'), int_lit)
                                          ]
                                          )),
            ])
        expect = str(TypeMismatchInExpression(ArrayCell(
            Id('id1'), [int_lit, int_lit, int_lit])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_index6(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              # [2][3]
                                              Assign(
                                                  Id('id1'), array_lit3),
                                              Assign(Id('id3'), bool_lit),

                                              Assign(Id('id2'), ArrayCell(
                                                  Id('id3'), [int_lit, int_lit])),

                                          ]
                                          )),
            ])
        expect = str(TypeMismatchInExpression(ArrayCell(
            Id('id3'), [int_lit, int_lit])))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_index6(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              # [2][3]
                                              Assign(
                                                  Id('id1'), array_lit3),
                                              Assign(Id('id2'), ArrayCell(
                                                  Id('id1'), [Id('id3'), Id('id4')])),

                                          ]
                                          )),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_index7(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              # [2][3]
                                              Assign(
                                                  Id('id1'), array_lit3),
                                              Assign(Id('id2'), ArrayCell(
                                                  Id('id1'), [Id('id3'), Id('id4')])),
                                              Assign(Id('id3'), int_lit)
                                          ]
                                          )),
            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_array_index8(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              # [2][3]
                                              Assign(
                                                  Id('id1'), array_lit3),
                                              Assign(Id('id2'), ArrayCell(
                                                  Id('id1'), [Id('id3'), Id('id4')])),
                                              Assign(Id('id3'), float_lit)
                                          ]
                                          )),
            ])
        expect = str(TypeMismatchInStatement(Assign(Id('id3'), float_lit)))
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_call_exp5(self):
        """Complex program"""
        input = Program(
            [
                FuncDecl(Id("main"), [], (list_of_var_decl,
                                          [
                                              # Stmts
                                              Assign(Id('id1'), CallExpr(Id('test'), [
                                                  int_lit, int_lit, int_lit])),
                                              Assign(Id('id4'), BinaryOp(
                                                  '-', int_lit, CallExpr(Id('test'), [
                                                      int_lit, int_lit, int_lit])))
                                          ]
                                          )),
                FuncDecl(Id("test"), list_of_param, (list_of_var_decl,
                                                     [
                                                         # Stmts
                                                         Assign(
                                                             Id('param1'), int_lit),
                                                         Assign(
                                                             Id('param2'), int_lit),
                                                         Assign(
                                                             Id('param3'), int_lit),
                                                         Return(
                                                             Id('param1'))
                                                     ]
                                                     )),

            ])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_list_of_var(self):
        """Complex program"""
        input = Program(
            [*list_of_var_decl, FuncDecl(Id("main"), [], ([], [])), *list_of_func_decl])
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared(self):
        """Complex program"""
        input = Program(
            [FuncDecl(Id("main"), [], ([*list_of_var_decl, *list_of_var_decl], [])), *list_of_func_decl])
        expect = str(Redeclared(Variable(), "id1"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared1(self):
        input = """
                    Var: a,a;
                    Function: main
                    Body:
                    EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 400))

    def test_redeclared2(self):
        input = """
                    Var: a;
                    Var: a;
                    Function: main
                    Body:
                    EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 401))

    def test_redeclared3(self):
        input = """
                    Var: a[2][3];
                    Var: a;
                    Function: main
                    Body:
                    EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 402))

    def test_redeclared4(self):
        input = """
                    Var: a[2][3];
                    Function: a
                    Body:
                    EndBody.
                    Function: main
                    Body:
                    EndBody."""
        expect = str(Redeclared(Function(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 403))

    def test_redeclared5(self):
        input = """
                    Function: a
                    Parameter: a,a
                    Body:
                    EndBody.
                    Function: main
                    Body:
                    EndBody."""
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 404))

    def test_redeclared6(self):
        input = """
                    Function: a
                    Parameter: a
                    Body:
                    Var: a;
                    EndBody.
                    Function: main
                    Body:
                    EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 405))

    def test_redeclared6(self):
        input = """
                    Function: main
                    Body:
                    Var: a,a;
                    EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 406))

    def test_redeclared7(self):
        input = """
                    Function: main
                    Body:
                    Var: a;
                    Var: a;
                    EndBody."""
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 407))

    def test_redeclared8(self):
        input = """
                    Function: b
                    Body:
                    Var: a;
                    EndBody.
                     Function: main
                     Body:
                    Var: a;
                    EndBody.
                    Function: c
                    Body:
                    Var: a;
                    Var: a;
                    EndBody.
                    """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 408))

    def test_undeclared1(self):
        input = """
                    Function: main
                    Body:
                    a = 3;
                    EndBody."""
        expect = str(Undeclared(Identifier(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 409))

    def test_undeclared2(self):
        input = """
                    Function: main
                    Body:
                    Var: a;
                    a = 3;
                    a = b;
                    EndBody."""
        expect = str(Undeclared(Identifier(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 410))

    def test_undeclared3(self):
        input = """
                    Function: main
                    Body:
                    Var: a;
                    a = 3;
                    a = b;
                    EndBody.
                    Function: abc
                    Body:
                    Var:b;
                    b = a;
                    EndBody.
                    """
        expect = str(Undeclared(Identifier(), "b"))
        self.assertTrue(TestChecker.test(input, expect, 411))

    def test_undeclared4(self):
        input = """
                    Var: b;
                    Function: main
                    Body:
                    Var: a;
                    a = 3;
                    a = b;
                    b = c;
                    EndBody.
                    """
        expect = str(Undeclared(Identifier(), "c"))
        self.assertTrue(TestChecker.test(input, expect, 412))

    def test_undeclared5(self):
        input = """
                    Var: b;
                    Function: main
                    Body:
                    Var: a;
                    a = too();
                    a = b;
                    b = c;
                    EndBody.
                    """
        expect = str(Undeclared(Function(), "too"))
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_typemismatch1(self):
        input = """
                    Function: main
                    Parameter: x,y,z
                    Body:
                    x =2;
                    y =3.0;
                    x = x + y;
                    EndBody.
                    """
        expect = str(TypeMismatchInExpression(
            BinaryOp("+", Id("x"), Id("y"))))
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_typemismatch2(self):
        input = """
                    Function: main
                    Body:
                    Var : a;
                    Var : b;
                    a = 3;
                    b = 3.3;
                    a = b;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("a"), Id("b"))))
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_typemismatch3(self):
        input = """
                    Function: main
                    Body:
                    Var : a[2][2] ;
                    Var: b = 2;
                    Var: c = 2;
                    b = a[2][2] +. 2.2;
                    c = a[2][1] + 1;
                    EndBody."""
        expect = str(TypeMismatchInStatement(Assign(Id("b"), BinaryOp(
            "+.", ArrayCell(Id("a"), [IntLiteral(2), IntLiteral(2)]), FloatLiteral(2.2)))))
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_passbyref_val2(self):
        input = """
                    Var: a[1][2] = {{2,3}};
                    Function: main
                    Body:
                    a[0][0] = 1.1;
                    EndBody.
                    """
        expect = str(TypeMismatchInStatement(
            Assign(ArrayCell(Id("a"), [IntLiteral(0), IntLiteral(0)]), FloatLiteral(1.1))))
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_call_stmt5(self):
        input = r"""
    Function: foo
        Body:
            Return 1;
        EndBody.

    Function: main
        Body:
            foo();
        EndBody.
    """
        expect = str(TypeMismatchInStatement(CallStmt(Id("foo"), [])))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_call_stmt6(self):
        input = r"""
    Var: a  =5 ;
    Function: main
    Parameter: argc, argv
    Body:
        Var: foo = 5;
        a = 1;
        a = foo(a);
    EndBody.
    """
        expect = str(TypeMismatchInExpression(
            CallExpr(Id("foo"), [Id('a')])))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_reclared9(self):
        """Complex program"""
        input = Program(
            [*list_of_var_decl, FuncDecl(Id("id1"), [], ([], [])),  FuncDecl(Id("main"), [], ([], []))])
        expect = str(Redeclared(Function(), "id1"))
        self.assertTrue(TestChecker.test(input, expect, 500))

    def test_reclared10(self):
        input = r"""

        Var: a ;
        Function: main
            Body:
            EndBody.

        Function: foo
            Body:
                a = foo1();
                Return a ;
            EndBody.
        Function: foo
            Body:
                Return 1;
            EndBody.
        """
        expect = str(Redeclared(Function(), "foo"))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_reclared11(self):
        input = r"""

        Var: a ;
        Function: main
            Body:
            EndBody.

        Function: foo
            Parameter: a,b,c,a
            Body:
                a = foo1();
                Return a ;
            EndBody.
        """
        expect = str(Redeclared(Parameter(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_reclared12(self):
        input = r"""

        Var: a ;
        Function: main
            Body:
            EndBody.

        Function: foo
            Parameter: a,b,c
            Body:
                Var: a;
                a = foo1();
                Return a ;
            EndBody.
        """
        expect = str(Redeclared(Variable(), "a"))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_call_stmt7(self):
        input = r"""

        Var: a ;
        Function: main
            Body:
                foo();
            EndBody.

        Function: foo
            Body:
                Var: a = 3.3 ;
                Return a ;
            EndBody.
        """
        expect = str(TypeMismatchInStatement(
            CallStmt(Id('foo'), [])))
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_call_exp6(self):
        input = r"""

        Var: a,b ;
        Function: main
            Body:
                a = foo(2.1,True,"HEY");
            EndBody.

        Function: foo
            Parameter: a,b,c
            Body:
                a = 3.3 ;
                b = False ;
                c = "String";
                Return a ;
            EndBody.
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))


    def test_array_index5(self):
        input = r"""

        Var: a,b ; 
        Function: main
            Body:
                a = foo()[2];
            EndBody.

        Function: foo
            Body:
                Return {1,2,3} ;
            EndBody.
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_call_exp8(self):
        input = r"""

        Var: a,b ; 
        Function: main
            Body:
                a = foo(foo(1,True,"string"),False,"not string");
            EndBody.

        Function: foo
            Parameter: a,b,c
            Body:
                a= 1; 
                b= True ; 
                c = "string" ; 
                Return 1 ;
            EndBody.
        """
        expect = ""
        self.assertTrue(TestChecker.test(input, expect, 442))

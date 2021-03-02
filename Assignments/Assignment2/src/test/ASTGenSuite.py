import unittest
from TestUtils import TestAST
from main.bkit.utils.AST import *


class ASTGenSuite(unittest.TestCase):
    def test_vardec9(self):
        input = r"""
        Var : a ;
        Var : b ;
        Var : c ;
        """
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], None),
            VarDecl(Id("c"), [], None),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_vardec8(self):
        input = r"""
   Var : a[2] = {3.e2,2e-1} ;
"""
        expect = expect = Program([
            VarDecl(Id("a"), [2], ArrayLiteral(
                [FloatLiteral(300.0), FloatLiteral(0.2)]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_vardec7(self):
        input = r"""
   Var : a[2] = {False,True} ;
"""
        expect = expect = Program([
            VarDecl(Id("a"), [2], ArrayLiteral(
                [BooleanLiteral(False), BooleanLiteral(True)]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_vardec6(self):
        input = r"""
   Var : a[2] = {"string","test"} ;
"""
        expect = expect = Program([
            VarDecl(Id("a"), [2], ArrayLiteral(
                [StringLiteral('string'), StringLiteral('test')]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_vardec4(self):
        input = r"""
Var: a = 1;
Var: b[1] = {1};
Var: c[1][2] = {{1}, {2}};
"""
        expect = Program([
            VarDecl(Id("a"), [], IntLiteral(1)),
            VarDecl(Id("b"), [1], ArrayLiteral([IntLiteral(1)])),
            VarDecl(Id("c"), [1, 2],
                    ArrayLiteral([ArrayLiteral([IntLiteral(1)]),
                                  ArrayLiteral([IntLiteral(2)])]))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_vardec5(self):
        input = r"""
Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
"""
        expect = Program([
            VarDecl(Id("a"), [], IntLiteral(5)),
            VarDecl(Id("b"), [2, 3],
                    ArrayLiteral(
                [ArrayLiteral(
                    [IntLiteral(2),
                     IntLiteral(3),
                     IntLiteral(4), ]
                ),
                    ArrayLiteral(
                    [IntLiteral(4),
                     IntLiteral(5),
                     IntLiteral(6), ]
                ), ]
            ))
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_simple_program(self):
        input = """Var: x;"""
        expect = Program([
            VarDecl(Id("x"), [], None)
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_Var_decl(self):
        input = r"""
Var: x=10,y=9,z=8 ;
"""
        expect = Program([
            VarDecl(Id("x"), [], IntLiteral(10)),
            VarDecl(Id("y"), [], IntLiteral(9)),
            VarDecl(Id("z"), [], IntLiteral(8)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_8_Var_decl(self):
        """ Test Var Declare """
        input = r"""
Var :a = "String '"s String" ;
"""
        expect = Program([
            VarDecl(Id("a"), [], StringLiteral(r"""String '"s String""")),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_7_Var_decl(self):
        """ Test Var Declare """
        input = r"""
Var : a, b, c = 3;
 Var : z = False ;
 Var   :garray[1][3] ;
"""
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], None),
            VarDecl(Id("c"), [], IntLiteral(3)),
            VarDecl(Id("z"), [], BooleanLiteral(False)),
            VarDecl(Id("garray"), [1, 3], None),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_5_Var_decl(self):
        """ Test Var Declare """
        input = r"""
Var :a, b, c,array[1][3]  ;
"""
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], None),
            VarDecl(Id("c"), [], None),
            VarDecl(Id("array"), [1, 3], None),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_4_Var_decl(self):
        """ Test Var Declare array """
        input = r"""
Var :a ,  array[1][3] ;
"""
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("array"), [1, 3], None),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_3_var_decl(self):
        """ Test Var Declare n line """
        input = r"""
Var :a, b, c= 3;
Var :x, y= 3.e2;
Var :z= "string";
"""
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], None),
            VarDecl(Id("c"), [], IntLiteral(3)),
            VarDecl(Id("x"), [], None),
            VarDecl(Id("y"), [], FloatLiteral(3.e2)),
            VarDecl(Id("z"), [], StringLiteral(r"""string""")),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_2_var_decl(self):
        """ Test Var Declare 1 line n var """
        input = r"""
Var :a, b, c= 4;
"""
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], None),
            VarDecl(Id("c"), [], IntLiteral(4)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    def test_var_dec(self):
        input = """Var: a=5 ;"""
        expect = Program([
            VarDecl(Id("a"), [], IntLiteral(5)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_1_var_decl(self):
        """ Test Var Declare 1 line 1 var """
        input = r"""
Var : a= False;
"""
        expect = Program([
            VarDecl(Id("a"), [], BooleanLiteral(False)),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))

    def test_var_dec1(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}} ;"""
        expect = Program([
            VarDecl(Id("b"), [2, 3], ArrayLiteral(
                [ArrayLiteral(
                    [IntLiteral(2),
                     IntLiteral(3),
                     IntLiteral(4), ]
                ),
                    ArrayLiteral(
                    [IntLiteral(4),
                     IntLiteral(5),
                     IntLiteral(6), ]
                ), ]
            )),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    def test_var_dec2(self):
        input = """Var: c,d = 6,e,f ;"""
        expect = Program([
            VarDecl(Id("c"), [], None),
            VarDecl(Id("d"), [], IntLiteral(6)),
            VarDecl(Id("e"), [], None),
            VarDecl(Id("f"), [], None),

        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_var_dec3(self):
        input = """Var:m,n[10] ; """
        expect = Program([
            VarDecl(Id("m"), [], None),
            VarDecl(Id("n"), [10], None),
        ])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    # def test_variable_declare_func(self):
    #     input = r"""
    #     Var:m,n[10] ;
    #     Function : fact
    #     Parameter: n
    #     Body:
    #         Var: r = 10, v ;
    #         v = 3;
    #     EndBody.
    #     """
    #     expect = Program([
    #         VarDecl(Id('m'), [], None),
    #         VarDecl(Id('n'), [10], None),
    #         FuncDecl(
    #             Id('fact'),
    #             # Para
    #             [
    #                 VarDecl(Id("n"), [], None),
    #             ],
    #             (
    #                 [
    #                     VarDecl(Id("r"), [], IntLiteral(10)),
    #                     VarDecl(Id("v"), [], None),
    #                 ],
    #                 [
    #                     Assign(
    #                         Id('v'),
    #                         IntLiteral(3)
    #                     )
    #                 ]
    #             )
    #         )
    #     ])
    #     self.assertTrue(TestAST.checkASTGen(input, expect, 320))

#     def test_nested_statement4(self):
#         input = r"""
#         Function : main
#             Body:
#                 While expression Do While expression Do EndWhile. EndWhile.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         While(
#                             Id('expression'),
#                             (
#                                 [], [While(
#                                     Id('expression'),
#                                     (
#                                         [], []
#                                     )
#                                 )]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 321))

#     def test_nested_statement3(self):
#         input = r"""
#         Function : main
#             Body:
#                 For (i = 0, i < 10, 2) Do
#                 For (i = 0, i < 10, 2) Do  EndFor.  EndFor.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         For(
#                             Id('i'),
#                             IntLiteral(0),
#                             BinaryOp('<', Id('i'), IntLiteral(10)),
#                             IntLiteral(2),
#                             (
#                                 [

#                                 ],
#                                 [
#                                     For(
#                                         Id('i'),
#                                         IntLiteral(0),
#                                         BinaryOp('<', Id('i'), IntLiteral(10)),
#                                         IntLiteral(2),
#                                         (
#                                             [

#                                             ],
#                                             [
#                                             ]
#                                         )
#                                     )
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 322))

#     def test_nested_statement1(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If expression Then
#                 If expression Then
#                 If expression Then

#         EndIf.
#         EndIf.
#         EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             # If
#                             [
#                                 (
#                                     Id("expression"),
#                                     [

#                                     ],
#                                     [If(
#                                         # If
#                                         [
#                                             (
#                                                 Id("expression"),
#                                                 [

#                                                 ],
#                                                 [If(
#                                                     # If
#                                                     [
#                                                         (
#                                                             Id("expression"),
#                                                             [

#                                                             ],
#                                                             [
#                                                             ]
#                                                         ),
#                                                     ],
#                                                     # Else
#                                                     (
#                                                         [

#                                                         ],
#                                                         [

#                                                         ]
#                                                     )
#                                                 )
#                                                 ]
#                                             ),
#                                         ],
#                                         # Else
#                                         (
#                                             [

#                                             ],
#                                             [

#                                             ]
#                                         )
#                                     )
#                                     ]
#                                 ),
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [

#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 323))

#     def test_nested_statement(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If expression Then
#                 If expression Then
#             EndIf.
#             EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             # If
#                             [
#                                 (
#                                     Id("expression"),
#                                     [

#                                     ],
#                                     [
#                                         If(
#                                             # If
#                                             [
#                                                 (
#                                                     Id("expression"),
#                                                     [

#                                                     ],
#                                                     [
#                                                     ]
#                                                 ),
#                                             ],
#                                             # Else
#                                             (
#                                                 [

#                                                 ],
#                                                 [

#                                                 ]
#                                             )
#                                         )
#                                     ]
#                                 ),
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [

#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 324))

#     def test_if_stmt7(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If expression Then  a=3 ;
#         EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             # If
#                             [
#                                 (
#                                     Id("expression"),
#                                     [
#                                         # Var declare
#                                     ],
#                                     [
#                                         Assign(Id('a'), IntLiteral(3))
#                                     ]
#                                 ),
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [

#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 324))

#     def test_if_stmt6(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If expression Then
#                 ElseIf expression Then
#         EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             # If
#                             [
#                                 (
#                                     Id("expression"),
#                                     [

#                                     ],
#                                     [
#                                     ]
#                                 ),
#                                 (
#                                     Id("expression"),
#                                     [

#                                     ],
#                                     [
#                                     ]
#                                 ),
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [

#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 325))

#     def test_if_stmt5(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If expression Then
#                 ElseIf expression Then
#                 Else
#         EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             # If
#                             [
#                                 (
#                                     Id("expression"),
#                                     [

#                                     ],
#                                     [
#                                     ]
#                                 ),
#                                 (
#                                     Id("expression"),
#                                     [

#                                     ],
#                                     [
#                                     ]
#                                 ),
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [

#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 326))

#     def test_if_stmt4(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If expression Then
#                 Else
#         EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             # If
#                             [
#                                 (
#                                     Id("expression"),
#                                     [

#                                     ],
#                                     [
#                                     ]
#                                 ),
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [

#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 327))

#     def test_if_stmt3(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If expression Then
#         EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             # If
#                             [
#                                 (
#                                     Id("expression"),
#                                     [

#                                     ],
#                                     [
#                                     ]
#                                 ),
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [

#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 328))

#     def test_if_stmt2(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If expression Then Var: a=3 ;
#         EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             # If
#                             [
#                                 (
#                                     Id("expression"),
#                                     [
#                                         # Var declare
#                                         VarDecl(Id("a"), [], IntLiteral(3)),
#                                     ],
#                                     [
#                                     ]
#                                 ),
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [

#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 329))

#     def test_if_stmt1(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If n == 6 Then
#                 Return 1;
#                 Else
#                 Return n * fact (n - 1);
#                 EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             [
#                                 (
#                                     BinaryOp('==', Id('n'), IntLiteral(6)),
#                                     [
#                                         # Var declare
#                                     ],
#                                     [
#                                         Return(IntLiteral(1))
#                                     ]
#                                 )
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [
#                                     Return(
#                                         BinaryOp('*',
#                                                  Id('n'),
#                                                  CallExpr(Id('fact'), [
#                                                      BinaryOp('-', Id('n'),
#                                                               IntLiteral(1))
#                                                  ]
#                                                  )))
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 330))

#     def test_if_stmt(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : fact
#             Parameter: n
#             Body:
#                 If expression Then a=3 ;
#         ElseIf expression Then b=4 ;
#         ElseIf expression Then c =5 ;
#         EndIf.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                     VarDecl(Id("n"), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         If(
#                             # If
#                             [
#                                 (
#                                     Id("expression"),
#                                     [
#                                         # Var declare
#                                     ],
#                                     [
#                                         Assign(
#                                             Id('a'),
#                                             IntLiteral(3)
#                                         )
#                                     ]
#                                 ),
#                                 (
#                                     Id("expression"),
#                                     [
#                                         # Var declare
#                                     ],
#                                     [
#                                         Assign(
#                                             Id('b'),
#                                             IntLiteral(4)
#                                         )
#                                     ]
#                                 ),
#                                 (
#                                     Id("expression"),
#                                     [
#                                         # Var declare
#                                     ],
#                                     [
#                                         Assign(
#                                             Id('c'),
#                                             IntLiteral(5)
#                                         )
#                                     ]
#                                 )
#                             ],
#                             # Else
#                             (
#                                 [

#                                 ],
#                                 [

#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 331))

#     def test_for_stmt(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : main
#             Body:
#                 For (i = 0, i < 10, 2) Do a=3 ; EndFor.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         For(
#                             Id('i'),
#                             IntLiteral(0),
#                             BinaryOp('<', Id('i'), IntLiteral(10)),
#                             IntLiteral(2),
#                             (
#                                 [

#                                 ],
#                                 [
#                                     Assign(
#                                         Id('a'),
#                                         IntLiteral(3)
#                                     )
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 332))

#     def test_for_stmt1(self):
#         input = r"""
#         Function : main
#             Body:
#                 For (i = 0, i < 10, 2) Do  EndFor.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         For(
#                             Id('i'),
#                             IntLiteral(0),
#                             BinaryOp('<', Id('i'), IntLiteral(10)),
#                             IntLiteral(2),
#                             (
#                                 [

#                                 ],
#                                 [
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 333))

#     def test_for_stmt2(self):
#         input = r"""
#         Function : main
#             Body:
#                 For (i = 0, i < 10, 2) Do Var: a =3 ; EndFor.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         For(
#                             Id('i'),
#                             IntLiteral(0),
#                             BinaryOp('<', Id('i'), IntLiteral(10)),
#                             IntLiteral(2),
#                             (
#                                 [
#                                     VarDecl(Id('a'), [],  IntLiteral(3))
#                                 ],
#                                 [
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 334))

#     def test_for_stmt3(self):
#         input = r"""
#         Function : main
#             Body:
#                 For (i = 0, i < 10, 2) Do Var: a =3 ; a=3 ; EndFor.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         For(
#                             Id('i'),
#                             IntLiteral(0),
#                             BinaryOp('<', Id('i'), IntLiteral(10)),
#                             IntLiteral(2),
#                             (
#                                 [
#                                     VarDecl(Id('a'), [],  IntLiteral(3))
#                                 ],
#                                 [
#                                     Assign(
#                                         Id('a'),
#                                         IntLiteral(3)
#                                     )
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 335))

#     def test_while_stmt(self):
#         input = r"""
#         Var:m,n[10] ;
#         Function : main
#             Body:
#                 While expression Do a=3 ; EndWhile.
#             EndBody.
#         """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         While(
#                             Id('expression'),
#                             (
#                                 [

#                                 ],
#                                 [
#                                     Assign(
#                                         Id('a'),
#                                         IntLiteral(3)
#                                     )
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 336))

#     def test_while_stmt1(self):
#         input = r"""
#         Function : main
#             Body:
#                 While expression Do EndWhile.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         While(
#                             Id('expression'),
#                             (
#                                 [], []
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 337))

#     def test_while_stmt2(self):
#         input = r"""
#         Function : main
#             Body:
#                 While expression Do Var: a=3; EndWhile.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         While(
#                             Id('expression'),
#                             (
#                                 [
#                                     VarDecl(Id('a'), [],  IntLiteral(3))
#                                 ],
#                                 [
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 338))

#     def test_while_stmt3(self):
#         input = r"""
#         Function : main
#             Body:
#                 While expression Do Var: a=3; a=3; EndWhile.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         While(
#                             Id('expression'),
#                             (
#                                 [
#                                     VarDecl(Id('a'), [],  IntLiteral(3))
#                                 ],
#                                 [
#                                     Assign(
#                                         Id('a'),
#                                         IntLiteral(3)
#                                     )
#                                 ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 339))

#     def test_do_while_stmt(self):
#         input = r"""
# Var:m,n[10] ;
# Function : main
#     Body:
#         Do a=3; While expression EndDo.
#     EndBody.
# """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Dowhile(
#                             (
#                                 [

#                                 ],
#                                 [
#                                     Assign(
#                                         Id('a'),
#                                         IntLiteral(3)
#                                     )
#                                 ]
#                             ),
#                             Id('expression')
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 340))

#     def test_do_while_stmt1(self):
#         input = r"""
#         Function : main
#             Body:
#                 Do  While expression EndDo.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Dowhile(

#                             (
#                                 [], []
#                             ), Id('expression')
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 341))

#     def test_do_while_stmt2(self):
#         input = r"""
#         Function : main
#             Body:
#                 Do Var:a=3; While expression EndDo.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Dowhile(

#                             (
#                                 [
#                                     VarDecl(Id('a'), [],  IntLiteral(3))
#                                 ],
#                                 [
#                                 ]
#                             ), Id('expression'),
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 342))

#     def test_do_while_stmt3(self):
#         input = r"""
#         Function : main
#             Body:
#                Do Var: a=3 ; a=3; While expression EndDo.
#             EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Dowhile(

#                             (
#                                 [
#                                     VarDecl(Id('a'), [],  IntLiteral(3))
#                                 ],
#                                 [
#                                     Assign(
#                                         Id('a'),
#                                         IntLiteral(3)
#                                     )
#                                 ]
#                             ),
#                             Id('expression'),
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 343))

#     def test_break_stmt(self):
#         input = r"""
# Var:m,n[10] ;
# Function : main
#     Body:
#         Break;
#     EndBody.
# """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Break()
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 344))

#     def test_continue_stmt(self):
#         input = r"""
# Var:m,n[10] ;
# Function : main
#     Body:
#       Continue;
#     EndBody.
# """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Continue()
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 345))

#     def test_return_stmt(self):
#         input = r"""
# Var:m,n[10] ;
# Function : main
#     Body:
#       Return hello(n);
#     EndBody.
# """
#         expect = Program([
#             VarDecl(Id('m'), [], None),
#             VarDecl(Id('n'), [10], None),
#             FuncDecl(
#                 Id('main'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Return(
#                             CallExpr(Id('hello'),
#                                      [
#                                 Id('n')
#                             ]
#                             )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 346))

#     def test_return_return(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     Return ;
#     Return ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Return(
#                             None
#                         ),
#                         Return(
#                             None
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 347))

#     def test_return_null(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     Return ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Return(
#                             None
#                         ),
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 348))

#     def test_not_expression1(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = !!!!!a ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(
#                             Id('b'),
#                             UnaryOp('!',
#                                     UnaryOp('!',
#                                             UnaryOp('!',
#                                                     UnaryOp('!',
#                                                             UnaryOp(
#                                                                 '!', Id('a'))
#                                                             )))))
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 349))

#     def test_sign_expression(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = -----a;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(
#                             Id('b'),
#                             UnaryOp('-',
#                                     UnaryOp('-',
#                                             UnaryOp('-',
#                                                     UnaryOp('-',
#                                                             UnaryOp(
#                                                                 '-', Id('a'))
#                                                             )))))
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 350))

#     def test_sign_expression2(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = -.----a ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(
#                             Id('b'),
#                             UnaryOp('-.',
#                                     UnaryOp('-',
#                                             UnaryOp('-',
#                                                     UnaryOp('-',
#                                                             UnaryOp(
#                                                                 '-', Id('a'))
#                                                             )))))
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 351))

#     def test_sign_expression1(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = -.3.0 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(
#                             Id('b'),
#                             UnaryOp('-.', FloatLiteral(3.0)))

#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 352))

#     def test_sign_expression3(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = -3 + --3 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(
#                             Id('b'),
#                             BinaryOp('+', UnaryOp('-', IntLiteral(3)), UnaryOp('-', UnaryOp('-', IntLiteral(3)))))

#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 353))

#     def test_sign_expression4(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = -3 + -3 --3 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(
#                             Id('b'),
#                             BinaryOp('-',  BinaryOp('+', UnaryOp('-', IntLiteral(3)), UnaryOp('-', IntLiteral(3))), UnaryOp('-', IntLiteral(3))))

#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 354))

#     def test_index_exp(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = a[3][3];
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('b'), ArrayCell(
#                             Id('a'), [IntLiteral(3), IntLiteral(3)]))
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 355))

#     def test_index_exp1(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = a[a[3]];
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('b'), ArrayCell(
#                             Id('a'), [ArrayCell(
#                                 Id('a'), [IntLiteral(3)])])

#                                )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 356))

#     def test_index_exp2(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = a[3];
# EndBody.
# """
#         expect = expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('b'),
#                                ArrayCell(
#                                    Id('a'), [IntLiteral(3)]
#                         )
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 357))

#     def test_index_exp3(self):
#         input = r"""
# Function: foo
# Parameter: a[5], b
# Body:
#     b = foo(n)[2];
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [Assign(
#                         Id('b'),
#                         ArrayCell(
#                             CallExpr(Id('foo'), [
#                                 Id('n')
#                             ]), [IntLiteral(2)]))
#                      ]

#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 358))

#     def test_comment2(self):
#         input = r"""
# ** Empty program, more likes empty life
#  One mul zero is zero**
#  **sadasd**
# """
#         expect = Program([])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 359))

#     def test_comment1(self):
#         input = r"""
# ** Empty program, more likes empty life
#  One mul zero is zero**
# """
#         expect = Program([])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 360))

#     def test_comment(self):
#         input = r"""
# ** Empty program, more likes empty life **
# """
#         expect = Program([])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 361))

#     def test_func(self):
#         input = r"""
# Function: foo
# Parameter: a[5],b
# Body:
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                     ]

#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 362))

#     def test_func1(self):
#         input = r"""
# Function: foo
# Parameter: a[5],b
# Body:
# EndBody.
# Function: foo
# Parameter: a[5],b
# Body:
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                     ]

#                 )
#             ),
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('a'), [5], None),
#                     VarDecl(Id('b'), [], None),
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                     ]

#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 363))

#     def test_func2(self):
#         input = r"""
# Function: foo
# Body:
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 364))

#     def test_func3(self):
#         input = r"""
# Function: foo
# Body:
# Var : a=3 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [
#                         VarDecl(Id('a'), [], IntLiteral(3))
#                     ],
#                     [
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 365))

#     def test_func4(self):
#         input = r"""
# Function: foo
# Parameter: n
# Body:
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                     VarDecl(Id('n'), [], None),
#                 ],
#                 (
#                     [
#                     ],
#                     [
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 366))

#     def test_program(self):
#         input = r"""
# """
#         expect = Program([

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 367))

#     def test_program1(self):
#         input = r"""
#         Var: a ;
# """
#         expect = Program([
#             VarDecl(Id("a"), [], None),
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 368))

#     def test_program2(self):
#         input = r"""
#         Var: a ;
#         Function: foo
# Body:
#  a= b ;
# EndBody.
# """
#         expect = Program([
#             VarDecl(Id("a"), [], None),
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),  Id('b'))
#                     ]

#                 )
#             ),
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 369))

#     def test_program3(self):
#         input = r"""
#         Var: a ;
#         Function: foo
# Body:
#  a= b ;
# EndBody.
#         Function: foo
# Body:
#  a= b ;
# EndBody.
# """
#         expect = Program([
#             VarDecl(Id("a"), [], None),
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),  Id('b'))
#                     ]

#                 )
#             ),
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),  Id('b'))
#                     ]

#                 )
#             ),
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 370))

#     def test_program4(self):
#         input = r"""
#         Var: a ;
#         Var: b ;
#         Function: foo
# Body:
#  a= b ;
# EndBody.
#         Function: foo
# Body:
#  a= b ;
# EndBody.
# """
#         expect = Program([
#             VarDecl(Id("a"), [], None),
#             VarDecl(Id("b"), [], None),
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),  Id('b'))
#                     ]

#                 )
#             ),
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),  Id('b'))
#                     ]

#                 )
#             ),
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 371))

#     def test_program5(self):
#         input = r"""
#         Var: a ;
#         Var: b ;
#         Function: foo
# Body:
#  a= b ;
# EndBody.
#         Function: foo
# Body:
#  Var: c ;
# EndBody.
# """
#         expect = Program([
#             VarDecl(Id("a"), [], None),
#             VarDecl(Id("b"), [], None),
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),  Id('b'))
#                     ]

#                 )
#             ),
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [
#                         VarDecl(Id("c"), [], None),
#                     ],
#                     [

#                     ]

#                 )
#             ),
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 372))

#     def test_exp1(self):
#         input = r"""
# Function: foo
# Body:
#  a= b ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),  Id('b'))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 373))

#     def test_exp2(self):
#         input = r"""
# Function: foo
# Body:
#  a= (b) ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),  Id('b'))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 373))

#     def test_exp3(self):
#         input = r"""
# Function: foo
# Body:
#  a= fact(n-1) ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),
#                                CallExpr(Id('fact'), [BinaryOp('-', Id('n'), IntLiteral(1))]))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 375))

#     def test_exp4(self):
#         input = r"""
# Function: foo
# Body:
#  a= -b ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), UnaryOp('-', Id('b')))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 376))

#     def test_exp5(self):
#         input = r"""
# Function: foo
# Body:
#  a= -.b ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), UnaryOp('-.', Id('b')))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 377))

#     def test_exp6(self):
#         input = r"""
# Function: foo
# Body:
#  a= !b ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), UnaryOp('!', Id('b')))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 378))

#     def test_exp7(self):
#         input = r"""
# Function: foo
# Body:
#  a= 3.e2 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), FloatLiteral(300.0))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 379))

#     def test_exp8(self):
#         input = r"""
# Function: foo
# Body:
#  a= False ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BooleanLiteral(False))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 380))

#     def test_exp9(self):
#         input = r"""
# Function: foo
# Body:
#  a= {{1}, {2}} ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), ArrayLiteral([ArrayLiteral([IntLiteral(1)]),
#                                                       ArrayLiteral([IntLiteral(2)])]))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 381))

#     def test_exp10(self):
#         input = r"""
# Function: foo
# Body:
#  a= 6*6 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp(
#                             '*',  IntLiteral(6), IntLiteral(6)))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 382))

#     def test_exp11(self):
#         input = r"""
# Function: foo
# Body:
#  a= 6*.6 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp(
#                             '*.',  IntLiteral(6), IntLiteral(6)))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 383))

#     def test_exp12(self):
#         input = r"""
# Function: foo
# Body:
#  a= 6\6 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp(
#                             '\\',  IntLiteral(6), IntLiteral(6)))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 384))

#     def test_exp13(self):
#         input = r"""
# Function: foo
# Body:
#  a= 6\.6 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp(
#                             '\\.',  IntLiteral(6), IntLiteral(6)))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 385))

#     def test_exp14(self):
#         input = r"""
# Function: foo
# Body:
#  a= 6+6 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp(
#                             '+',  IntLiteral(6), IntLiteral(6)))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 386))

#     def test_exp15(self):
#         input = r"""
# Function: foo
# Body:
#  a= 6-6 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp(
#                             '-',  IntLiteral(6), IntLiteral(6)))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 387))

#     def test_exp16(self):
#         input = r"""
# Function: foo
# Body:
#  a= 6&&6 ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp(
#                             '&&',  IntLiteral(6), IntLiteral(6)))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 388))

#     def test_exp17(self):
#         input = r"""
# Function: foo
# Body:
#  a= 3*6+6  ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp(
#                             '+',  BinaryOp(
#                                 '*',  IntLiteral(3), IntLiteral(6)), IntLiteral(6)))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 389))

#     def test_exp18(self):
#         input = r"""
# Function: foo
# Body:
#  a= 3*(6+6)  ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp('*', IntLiteral(3),
#                                                  BinaryOp('+',  IntLiteral(6), IntLiteral(6))))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 390))

#     def test_exp20(self):
#         input = r"""
# Function: foo
# Body:
#  a= fact(n-1)+3*(6+6)  ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'),
#                                BinaryOp('+', CallExpr(Id('fact'), [BinaryOp('-', Id('n'), IntLiteral(1))]), BinaryOp('*', IntLiteral(3),
#                                                                                                                      BinaryOp('+',  IntLiteral(6), IntLiteral(6)))))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 391))

#     def test_exp21(self):
#         input = r"""
# Function: foo
# Body:
#  a= -(fact(n-1)+3*(6+6))  ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), UnaryOp('-', BinaryOp('+', CallExpr(Id('fact'), [BinaryOp('-', Id('n'), IntLiteral(1))]), BinaryOp('*', IntLiteral(3),
#                                                                                                                                            BinaryOp('+',  IntLiteral(6), IntLiteral(6))))))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 392))

#     def test_exp22(self):
#         input = r"""
# Function: foo
# Body:
#  a= (-(fact(n-1)+3*(6+6)))[3]  ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), ArrayCell(UnaryOp('-', BinaryOp('+', CallExpr(Id('fact'), [BinaryOp('-', Id('n'), IntLiteral(1))]), BinaryOp('*', IntLiteral(3),
#                                                                                                                                                      BinaryOp('+',  IntLiteral(6), IntLiteral(6))))), [IntLiteral(3)]))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 393))

#     def test_exp23(self):
#         input = r"""
# Function: foo
# Body:
#  a= a[-(fact(n-1)+3*(6+6))]  ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), ArrayCell(Id('a'), [UnaryOp('-', BinaryOp('+', CallExpr(Id('fact'), [BinaryOp('-', Id('n'), IntLiteral(1))]), BinaryOp('*', IntLiteral(3),
#                                                                                                                                                                BinaryOp('+',  IntLiteral(6), IntLiteral(6)))))]))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 394))

#     def test_exp24(self):
#         input = r"""
# Function: foo
# Body:
#  a= 3*(6\6)  ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), BinaryOp('*', IntLiteral(3),
#                                                  BinaryOp('\\',  IntLiteral(6), IntLiteral(6))))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 395))

#     def test_exp25(self):
#         input = r"""
# Function: foo
# Body:
#  a= -(3*(6\6))  ;
# EndBody.
# """
#         expect = Program([
#             FuncDecl(
#                 Id('foo'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [

#                     ],
#                     [
#                         Assign(Id('a'), UnaryOp('-', BinaryOp('*', IntLiteral(3),
#                                                               BinaryOp('\\',  IntLiteral(6), IntLiteral(6)))))
#                     ]

#                 )
#             ),

#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 396))

#     def test_assign(self):
#         input = r"""
#         Function : fact
#         Body:
#             v = 3;
#         EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [
#                     ],
#                     [
#                         Assign(
#                             Id('v'),
#                             IntLiteral(3)
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 397))

#     def test_assign1(self):
#         input = r"""
#         Function : fact
#         Body:
#             v[3] = 3;
#         EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [
#                     ],
#                     [
#                         Assign(
#                             ArrayCell(Id('v'), [IntLiteral(3)]),
#                             IntLiteral(3)
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 398))

#     def test_assign2(self):
#         input = r"""
#         Function : fact
#         Body:
#             v[fact(n-1)] = 3;
#         EndBody.
#         """
#         expect = Program([
#             FuncDecl(
#                 Id('fact'),
#                 # Para
#                 [
#                 ],
#                 (
#                     [
#                     ],
#                     [
#                         Assign(
#                             ArrayCell(Id('v'), [CallExpr(Id('fact'), [
#                                 BinaryOp('-', Id('n'),
#                                          IntLiteral(1))
#                             ])]),
#                             IntLiteral(3)
#                         )
#                     ]
#                 )
#             )
#         ])
#         self.assertTrue(TestAST.checkASTGen(input, expect, 399))

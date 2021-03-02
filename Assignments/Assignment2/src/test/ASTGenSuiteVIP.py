import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # Var Declare
    def test_301(self):
        input = r""" """
        expect = Program([])
        self.assertTrue(TestAST.checkASTGen(input, expect, 301))

    def test_302(self):
        input = r"""
        Var: a;
        """
        expect = Program([VarDecl(Id("a"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 302))

    def test_303(self):
        input = r"""
        Var: a;
        Var: a,b,c;
        """
        expect = Program([
            VarDecl(Id("a"), [], None),
            VarDecl(Id("a"), [], None),
            VarDecl(Id("b"), [], None),
            VarDecl(Id("c"), [], None)])
        self.assertTrue(TestAST.checkASTGen(input, expect, 303))

    def test_304(self):
        input = r"""
        Var: a_float = 1.25;
        """
        expect = Program([
            VarDecl(Id("a_float"), [], FloatLiteral(1.25))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 304))

    def test_305(self):
        input = r"""
        Var: a_hex = 0xFF;
"""
        expect = Program([VarDecl(Id("a_hex"), [], IntLiteral(255))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 305))

    def test_306(self):
        input = r"""
        Var: a_oct = 0o25;
"""
        expect = Program([VarDecl(Id("a_oct"), [], IntLiteral(21))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 306))

    def test_307(self):
        input = r"""
        Var: a = {2,3,4};
"""
        expect = Program([
            VarDecl(Id("a"), [], ArrayLiteral([
                IntLiteral(2),
                IntLiteral(3),
                IntLiteral(4)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 307))

    def test_308(self):
        input = r"""
        Var: a[2][3] = {{1,2,3},{3,4,5},{6,7,8}};
"""
        expect = Program([
            VarDecl(Id("a"), [2, 3],
                    ArrayLiteral([
                        ArrayLiteral([
                            IntLiteral(1),
                            IntLiteral(2),
                            IntLiteral(3)]),
                        ArrayLiteral([
                            IntLiteral(3),
                            IntLiteral(4),
                            IntLiteral(5)]),
                        ArrayLiteral([
                            IntLiteral(6),
                            IntLiteral(7),
                            IntLiteral(8)])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 308))

    def test_309(self):
        input = r"""
        Var: string = "string comment PPL Var: a = 6065;";
"""
        expect = Program([
            VarDecl(Id("string"), [], StringLiteral(r"""string comment PPL Var: a = 6065;"""))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 309))

    def test_310(self):
        input = r"""
        Var: float_Array[3] = {1.05, 2.07, 36, 24.000465, 1.00000};
"""
        expect = Program([
            VarDecl(Id("float_Array"), [3],
                    ArrayLiteral([
                        FloatLiteral(1.05),
                        FloatLiteral(2.07),
                        IntLiteral(36),
                        FloatLiteral(24.000465), FloatLiteral(1.0)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 310))

    def test_311(self):
        input = r"""
        Var: string_Array[3] = {"abcd", "array", "input"};
"""
        expect = Program([VarDecl(Id("string_Array"), [3], ArrayLiteral([StringLiteral(
            r"""abcd"""), StringLiteral(r"""array"""), StringLiteral(r"""input""")]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 311))

    def test_312(self):
        input = r"""
        Var: hex_Array[2] = {0xFF,0xAB};
"""
        expect = Program([VarDecl(Id("hex_Array"), [2], ArrayLiteral(
            [IntLiteral(255), IntLiteral(171)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 312))

    def test_313(self):
        input = r"""
        Var: boolean_var = True;
        Var: boolean_var1 = False;
"""
        expect = Program([VarDecl(Id("boolean_var"), [], BooleanLiteral(
            True)), VarDecl(Id("boolean_var1"), [], BooleanLiteral(False))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 313))

    def test_314(self):
        input = r"""
        Var: array[13] = {1, 2, 2.34, 34.000000000007, 0xFF, 0xFFFFF, 0XFFFFF, 0o12, 0O433, "string", "string **array** string2", True, False};
"""
        expect = Program([VarDecl(Id("array"), [13], ArrayLiteral([IntLiteral(1), IntLiteral(2), FloatLiteral(2.34), FloatLiteral(34.000000000007), IntLiteral(255), IntLiteral(1048575), IntLiteral(
            1048575), IntLiteral(10), IntLiteral(283), StringLiteral(r"""string"""), StringLiteral(r"""string **array** string2"""), BooleanLiteral(True), BooleanLiteral(False)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 314))

    # Function Declare
    def test_315(self):
        input = r"""
        Function: main
            Body:
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 315))

    def test_316(self):
        input = r"""
        Function: main 
            Body:
            EndBody.
        Function: main
            Body:
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [])),
                          FuncDecl(Id("main"), [], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 316))
    # Function and var Declare

    def test_317(self):
        input = r"""
        Function: main 
            Body:
                Var: a;
                Var: b,c;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(
            Id("b"), [], None), VarDecl(Id("c"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 317))

    # Function with parameter
    def test_318(self):
        input = r"""
        Function: main 
            Parameter: a
            Body:
            EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 318))

    def test_319(self):
        input = r"""
        Function: foo
            Parameter: b,c,d
            Body:
            EndBody.
"""
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("b"), [], None), VarDecl(
            Id("c"), [], None), VarDecl(Id("d"), [], None)], ([], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 319))

    def test_320(self):
        input = r"""
        Function: foo
            Parameter:a
            Body: 
                Var: b;
            EndBody.
        Function: foo1
            Parameter: x
            Body:
                Var: y;
                Var: z = 1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("foo"), [VarDecl(Id("a"), [], None)], ([VarDecl(Id("b"), [], None)], [])), FuncDecl(
            Id("foo1"), [VarDecl(Id("x"), [], None)], ([VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], IntLiteral(1))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 320))

    def test_321(self):
        input = r"""
        Function: main
            Parameter: a
            Body: 
                foo(a);
            EndBody.
        Function: foo
            Parameter: a
            Body:
                Return a + 1;
            EndBody. 
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], [CallStmt(Id("foo"), [Id("a")])])), FuncDecl(
            Id("foo"), [VarDecl(Id("a"), [], None)], ([], [Return(BinaryOp("+", Id("a"), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 321))

    def test_322(self):
        input = r"""
        Function: main 
            Parameter: a, a[1], a[1][1][1]
            Body:
                Var: b,c,d,e;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None), VarDecl(Id("a"), [1], None), VarDecl(Id("a"), [1, 1, 1], None)], ([
                         VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None), VarDecl(Id("e"), [], None)], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 322))

    def test_323(self):
        input = r"""
        Function: main 
            Parameter: a,b,c,d
            Body:
                Var: a = 1;
                Var: b,c[5], d = 1.05, e = 0xFFF, f = 0o32;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None)], ([VarDecl(Id("a"), [], IntLiteral(
            1)), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [5], None), VarDecl(Id("d"), [], FloatLiteral(1.05)), VarDecl(Id("e"), [], IntLiteral(4095)), VarDecl(Id("f"), [], IntLiteral(26))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 323))

    def test_324(self):
        input = r"""
        Function: main
            Parameter: x,y,z
            Body:
                Var: a = "String";
                Var: b[3] = {1,2,3};
                Var: c = True, d = False;
                Var: e[3][3] = {{1,2,3},{True, True, False},{"a","b","c"}};
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], ([VarDecl(Id("a"), [], StringLiteral(r"""String""")), VarDecl(Id("b"), [3], ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)])), VarDecl(Id("c"), [], BooleanLiteral(True)), VarDecl(
            Id("d"), [], BooleanLiteral(False)), VarDecl(Id("e"), [3, 3], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(True), BooleanLiteral(False)]), ArrayLiteral([StringLiteral(r"""a"""), StringLiteral(r"""b"""), StringLiteral(r"""c""")])]))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 324))
    # If STMT

    def test_325(self):
        input = r"""
        Function: main
            Body: 
                If a Then 
                EndIf.
            EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [If([(Id("a"), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 325))

    def test_326(self):
        input = r"""
        Function: main 
            Body:
                If a Then 
                ElseIf b Then 
                Else 
                EndIf.
            EndBody.
"""
        expect = Program([FuncDecl(
            Id("main"), [], ([], [If([(Id("a"), [], []), (Id("b"), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 326))

    def test_327(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
            EndBody.
        Function: foo
            Parameter: a, b, c
            Body:
                If a == True Then 
                ElseIf a != True Then 
                ElseIf b == 1 Then 
                Else
                    foo();
                EndIf.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], [])), FuncDecl(Id("foo"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None)], ([], [If(
            [(BinaryOp("==", Id("a"), BooleanLiteral(True)), [], []), (BinaryOp("!=", Id("a"), BooleanLiteral(True)), [], []), (BinaryOp("==", Id("b"), IntLiteral(1)), [], [])], ([], [CallStmt(Id("foo"), [])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 327))
    # nested If

    def test_328(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                If a == True Then
                    If b[1] == {2.085} Then 
                        If c == False Then 
                            foo(3);
                        EndIf.
                    EndIf.
                EndIf.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], [If([(BinaryOp("==", Id("a"), BooleanLiteral(True)), [], [If([(BinaryOp("==", ArrayCell(Id("b"), [IntLiteral(
            1)]), ArrayLiteral([FloatLiteral(2.085)])), [], [If([(BinaryOp("==", Id("c"), BooleanLiteral(False)), [], [CallStmt(Id("foo"), [IntLiteral(3)])])], ([], []))])], ([], []))])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 328))

    def test_329(self):
        input = r"""
        Function: foo
            Body:
                If var == True Then
                    Var: a,b,c;
                    foo();
                    If foo() == 2 Then 
                        a = 1;
                    ElseIf foo() == 3 Then 
                        a = 2;
                    ElseIf foo1() == 0 Then 
                        a = 0;
                    EndIf.
                EndIf.
            EndBody. 
        Function: foo1
            Parameter: a
            Body:
                Return a + 1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("foo"), [], ([], [If([(BinaryOp("==", Id("var"), BooleanLiteral(True)), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None)], [CallStmt(Id("foo"), []), If([(BinaryOp("==", CallExpr(Id("foo"), []), IntLiteral(2)), [], [Assign(Id("a"), IntLiteral(1))]), (BinaryOp(
            "==", CallExpr(Id("foo"), []), IntLiteral(3)), [], [Assign(Id("a"), IntLiteral(2))]), (BinaryOp("==", CallExpr(Id("foo1"), []), IntLiteral(0)), [], [Assign(Id("a"), IntLiteral(0))])], ([], []))])], ([], []))])), FuncDecl(Id("foo1"), [VarDecl(Id("a"), [], None)], ([], [Return(BinaryOp("+", Id("a"), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 329))
    # For STMT

    def test_330(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                For (a = 1, a < 100, True) Do
                    sum = sum + foo(a);
                EndFor. 
            EndBody.
        Function: foo
            Parameter: a
            Body:
                Return (a + 100) * 25;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], [For(Id("a"), IntLiteral(1), BinaryOp("<", Id("a"), IntLiteral(100)), BooleanLiteral(True), ([], [Assign(Id("sum"), BinaryOp(
            "+", Id("sum"), CallExpr(Id("foo"), [Id("a")])))]))])), FuncDecl(Id("foo"), [VarDecl(Id("a"), [], None)], ([], [Return(BinaryOp("*", BinaryOp("+", Id("a"), IntLiteral(100)), IntLiteral(25)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 330))
    # Nested For-loop

    def test_331(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                For (a = 100, a > 1, -1) Do
                    For (b = 0, b < 50, 2) Do
                        If (a - b) < 10 Then
                            foo(a);
                        Else
                            foo(b);
                        EndIf.
                    EndFor.
                EndFor.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], [For(Id("a"), IntLiteral(100), BinaryOp(">", Id("a"), IntLiteral(1)), UnaryOp("-", IntLiteral(1)), ([], [For(Id("b"), IntLiteral(0), BinaryOp(
            "<", Id("b"), IntLiteral(50)), IntLiteral(2), ([], [If([(BinaryOp("<", BinaryOp("-", Id("a"), Id("b")), IntLiteral(10)), [], [CallStmt(Id("foo"), [Id("a")])])], ([], [CallStmt(Id("foo"), [Id("b")])]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 331))
    # Break Loop

    def test_332(self):
        input = r"""
        Function: main
            Body:
                For (a = 100, a > -100, -2) Do
                    For (b = 0, b < 100, 1) Do
                        If (b > a) Then 
                            Break;
                        ElseIf (b == a) Then
                            Continue;
                        Else 
                            sum = sum + a + b;
                        EndIf.
                    EndFor.
            EndFor.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [For(Id("a"), IntLiteral(100), BinaryOp(">", Id("a"), UnaryOp("-", IntLiteral(100))), UnaryOp("-", IntLiteral(2)), ([], [For(Id("b"), IntLiteral(0), BinaryOp("<", Id("b"), IntLiteral(
            100)), IntLiteral(1), ([], [If([(BinaryOp(">", Id("b"), Id("a")), [], [Break()]), (BinaryOp("==", Id("b"), Id("a")), [], [Continue()])], ([], [Assign(Id("sum"), BinaryOp("+", BinaryOp("+", Id("sum"), Id("a")), Id("b")))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 332))
    # Continue stmt Loop

    def test_333(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                For (a = 0, a < 100, 1) Do
                    If (a + 2) * 0.3 == 0 Then 
                        foo();
                    Else
                        Continue;
                    EndIf.
                EndFor.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], [For(Id("a"), IntLiteral(0), BinaryOp("<", Id("a"), IntLiteral(100)), IntLiteral(1), ([], [If(
            [(BinaryOp("==", BinaryOp("*", BinaryOp("+", Id("a"), IntLiteral(2)), FloatLiteral(0.3)), IntLiteral(0)), [], [CallStmt(Id("foo"), [])])], ([], [Continue()]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 333))

    def test_334(self):
        input = r"""
        Function: main
            Body:
                For (a = 0, a < 5, 1) Do
                    If (a == 3) Then 
                        Return foo(1);
                    EndIf.
                EndFor.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [For(Id("a"), IntLiteral(0), BinaryOp("<", Id("a"), IntLiteral(5)), IntLiteral(
            1), ([], [If([(BinaryOp("==", Id("a"), IntLiteral(3)), [], [Return(CallExpr(Id("foo"), [IntLiteral(1)]))])], ([], []))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 334))
    # While-Do

    def test_335(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                Var: a = 0xFF;
                While (a < 100) Do
                    foo(a);
                a = a + 2;
                EndWhile.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([VarDecl(Id("a"), [], IntLiteral(255))], [While(BinaryOp(
            "<", Id("a"), IntLiteral(100)), ([], [CallStmt(Id("foo"), [Id("a")]), Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 335))

    def test_336(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                Var: a = 100;
                While (a > 0) Do
                    For (b = 1, b < 100, 1) Do 
                        If (a \ b) + 2 == 5 Then 
                            foo(a + b);
                        Else 
                            foo(foo(a));
                        EndIf.
                    EndFor.
                    a = a - 1;
                EndWhile.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([VarDecl(Id("a"), [], IntLiteral(100))], [While(BinaryOp(">", Id("a"), IntLiteral(0)), ([], [For(Id("b"), IntLiteral(1), BinaryOp("<", Id("b"), IntLiteral(100)), IntLiteral(1), ([], [If([(BinaryOp(
            "==", BinaryOp("+", BinaryOp("\\", Id("a"), Id("b")), IntLiteral(2)), IntLiteral(5)), [], [CallStmt(Id("foo"), [BinaryOp("+", Id("a"), Id("b"))])])], ([], [CallStmt(Id("foo"), [CallExpr(Id("foo"), [Id("a")])])]))])), Assign(Id("a"), BinaryOp("-", Id("a"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 336))

    def test_337(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                Var: a = True, sum = 0;
                While (a) Do
                    For(b = 0, b < 100, 1) Do
                        If (a) Then 
                            sum = sum + b;
                        Else 
                            sum = (sum +. 0.25) + 2*b;
                        EndIf.
                    EndFor.
                EndWhile.
            EndBody.

"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([VarDecl(Id("a"), [], BooleanLiteral(True)), VarDecl(Id("sum"), [], IntLiteral(0))], [While(Id("a"), ([], [For(Id("b"), IntLiteral(0), BinaryOp("<", Id("b"), IntLiteral(
            100)), IntLiteral(1), ([], [If([(Id("a"), [], [Assign(Id("sum"), BinaryOp("+", Id("sum"), Id("b")))])], ([], [Assign(Id("sum"), BinaryOp("+", BinaryOp("+.", Id("sum"), FloatLiteral(0.25)), BinaryOp("*", IntLiteral(2), Id("b"))))]))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 337))

    def test_338(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                Var: a[100];
                For (i = 0, i < 100, 1) Do
                    a[i] = 1;
                EndFor.
                While (a[i] > 0) Do
                    a[i] = a[i] \ 2;
                EndWhile.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([VarDecl(Id("a"), [100], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(100)), IntLiteral(1), ([], [Assign(ArrayCell(
            Id("a"), [Id("i")]), IntLiteral(1))])), While(BinaryOp(">", ArrayCell(Id("a"), [Id("i")]), IntLiteral(0)), ([], [Assign(ArrayCell(Id("a"), [Id("i")]), BinaryOp("\\", ArrayCell(Id("a"), [Id("i")]), IntLiteral(2)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 338))

    def test_339(self):
        input = r"""
        Function: main 
            Body:
                Var: a,b,c,d;
                Var: v;
                v = (4. \. 3.0209) *. (12.05 +. 24.23) *. a *. a *. a;
                If (v \. 2 == 0) Then 
                    foo(v);
                EndIf.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None), VarDecl(Id("v"), [], None)], [Assign(Id("v"), BinaryOp("*.", BinaryOp("*.", BinaryOp("*.", BinaryOp("*.", BinaryOp(
            "\\.", FloatLiteral(4.0), FloatLiteral(3.0209)), BinaryOp("+.", FloatLiteral(12.05), FloatLiteral(24.23))), Id("a")), Id("a")), Id("a"))), If([(BinaryOp("==", BinaryOp("\\.", Id("v"), IntLiteral(2)), IntLiteral(0)), [], [CallStmt(Id("foo"), [Id("v")])])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 339))

    def test_340(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                While (a == True) Do
                    b = foo();
                    If b < 0 Then 
                        Break;
                    ElseIf b == 0 Then
                        Return foo(1);
                    Else 
                        Continue;
                    EndIf.
                EndWhile.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], [While(BinaryOp("==", Id("a"), BooleanLiteral(True)), ([], [Assign(Id("b"), CallExpr(Id("foo"), [])), If(
            [(BinaryOp("<", Id("b"), IntLiteral(0)), [], [Break()]), (BinaryOp("==", Id("b"), IntLiteral(0)), [], [Return(CallExpr(Id("foo"), [IntLiteral(1)]))])], ([], [Continue()]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 340))
    # Do-While

    def test_341(self):
        input = r"""
        Function: main
            Parameter: a,b,c
            Body:
                Do
                    foo();
                While a == True
                EndDo.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(
            Id("c"), [], None)], ([], [Dowhile(([], [CallStmt(Id("foo"), [])]), BinaryOp("==", Id("a"), BooleanLiteral(True)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 341))

    def test_342(self):
        input = r"""
        Function: main
            Parameter: x,y,z
            Body:
                Do 
                    a = foo(x);
                    If (a == True) Then
                        Continue;
                    Else
                        Break;
                    EndIf.
                y = y - 1;
                While y > 0
                EndDo.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], ([], [Dowhile(([], [Assign(Id("a"), CallExpr(Id("foo"), [Id("x")])), If(
            [(BinaryOp("==", Id("a"), BooleanLiteral(True)), [], [Continue()])], ([], [Break()])), Assign(Id("y"), BinaryOp("-", Id("y"), IntLiteral(1)))]), BinaryOp(">", Id("y"), IntLiteral(0)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 342))

    def test_343(self):
        input = r"""
        Function: main
            Parameter: x
            Body:
                Var: a[100];
                For (i = 0, i < 100, 1) Do
                    a[i] = 1;
                EndFor.
                Do  
                    foo(a[i]);
                    y = y + 1;
                While y < 100 
                EndDo.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("x"), [], None)], ([VarDecl(Id("a"), [100], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(100)), IntLiteral(1), ([], [Assign(ArrayCell(
            Id("a"), [Id("i")]), IntLiteral(1))])), Dowhile(([], [CallStmt(Id("foo"), [ArrayCell(Id("a"), [Id("i")])]), Assign(Id("y"), BinaryOp("+", Id("y"), IntLiteral(1)))]), BinaryOp("<", Id("y"), IntLiteral(100)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 343))
    # Nested Loop

    def test_344(self):
        input = r"""
        Function: main
            Parameter: a,b,c,d
            Body:
                For (a = 0, a < 100, 1) Do
                    While (b < 100) Do
                        Do
                            foo(c);
                            If (foo(c) == 12.5) Then 
                                Break;
                            EndIf.
                            c = c + 1;
                        While c < 100 
                        EndDo.
                    EndWhile.
                EndFor.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None)], ([], [For(Id("a"), IntLiteral(0), BinaryOp("<", Id("a"), IntLiteral(100)), IntLiteral(1), ([], [While(BinaryOp("<", Id(
            "b"), IntLiteral(100)), ([], [Dowhile(([], [CallStmt(Id("foo"), [Id("c")]), If([(BinaryOp("==", CallExpr(Id("foo"), [Id("c")]), FloatLiteral(12.5)), [], [Break()])], ([], [])), Assign(Id("c"), BinaryOp("+", Id("c"), IntLiteral(1)))]), BinaryOp("<", Id("c"), IntLiteral(100)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 344))

    def test_345(self):
        input = r"""
        Function: main
            Body:
                Var: a,b,c;
                Var: a = {{1,2,3},{4,5,6}};
                For (i = 0, i < 100, 1) Do
                    While (x > 0) Do
                        foo(foo(foo(i)));
                        foo1(foo(foo1(x + i)));
                        x = x - 1;
                    EndWhile.
                EndFor.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("a"), [], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(4), IntLiteral(5), IntLiteral(6)])]))], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id(
            "i"), IntLiteral(100)), IntLiteral(1), ([], [While(BinaryOp(">", Id("x"), IntLiteral(0)), ([], [CallStmt(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [Id("i")])])]), CallStmt(Id("foo1"), [CallExpr(Id("foo"), [CallExpr(Id("foo1"), [BinaryOp("+", Id("x"), Id("i"))])])]), Assign(Id("x"), BinaryOp("-", Id("x"), IntLiteral(1)))]))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 345))

    def test_346(self):
        input = r"""
        Function: main
            Parameter: a,b,c,e,x,z, a[1][2][3][4]
            Body:
                Var: a[100], j = 0;
                For(i = 0, i < 100, 1) Do
                    If (i \ 2 == 0) Then
                        a[i] = 0xFF;
                    Else
                        a[i] = 0o32;
                    EndIf.
                EndFor.
                While (j < 100) Do
                    a[i] = a[i] + 100;
                EndWhile.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("e"), [], None), VarDecl(Id("x"), [], None), VarDecl(Id("z"), [], None), VarDecl(Id("a"), [1, 2, 3, 4], None)], ([VarDecl(Id("a"), [100], None), VarDecl(Id("j"), [], IntLiteral(0))], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(100)), IntLiteral(
            1), ([], [If([(BinaryOp("==", BinaryOp("\\", Id("i"), IntLiteral(2)), IntLiteral(0)), [], [Assign(ArrayCell(Id("a"), [Id("i")]), IntLiteral(255))])], ([], [Assign(ArrayCell(Id("a"), [Id("i")]), IntLiteral(26))]))])), While(BinaryOp("<", Id("j"), IntLiteral(100)), ([], [Assign(ArrayCell(Id("a"), [Id("i")]), BinaryOp("+", ArrayCell(Id("a"), [Id("i")]), IntLiteral(100)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 346))

    def test_347(self):
        input = r"""
        Function: main
            Body:
                foo(True, False, a, b, c, 0xFF, 0XAB, 0o325, 0o2142, True, !True);
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), [BooleanLiteral(True), BooleanLiteral(False), Id("a"), Id("b"), Id(
            "c"), IntLiteral(255), IntLiteral(171), IntLiteral(213), IntLiteral(1122), BooleanLiteral(True), UnaryOp("!", BooleanLiteral(True))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 347))

    def test_348(self):
        input = r"""
        Function: main
            Body: 
                foo(foo(foo(foo1(!True), False), True), !True);
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo1"), [
                         UnaryOp("!", BooleanLiteral(True))]), BooleanLiteral(False)]), BooleanLiteral(True)]), UnaryOp("!", BooleanLiteral(True))])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 348))

    def test_349(self):
        input = r"""
        Function: main
            Body:
                foo(1, True, foo(1, False), foo(1,!False), !False, 2.06 *. 3.05);
                foo(0xFF, 0xAAAEEEE);
                foo(0xFF, 0xFF, True, "String", 0xFF);
                foo("a", "b", "c", 1 + 2, foo(a[i]));
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), [IntLiteral(1), BooleanLiteral(True), CallExpr(Id("foo"), [IntLiteral(1), BooleanLiteral(False)]), CallExpr(Id("foo"), [IntLiteral(1), UnaryOp("!", BooleanLiteral(False))]), UnaryOp("!", BooleanLiteral(False)), BinaryOp("*.", FloatLiteral(2.06), FloatLiteral(3.05))]), CallStmt(Id("foo"), [
                         IntLiteral(255), IntLiteral(178974446)]), CallStmt(Id("foo"), [IntLiteral(255), IntLiteral(255), BooleanLiteral(True), StringLiteral(r"""String"""), IntLiteral(255)]), CallStmt(Id("foo"), [StringLiteral(r"""a"""), StringLiteral(r"""b"""), StringLiteral(r"""c"""), BinaryOp("+", IntLiteral(1), IntLiteral(2)), CallExpr(Id("foo"), [ArrayCell(Id("a"), [Id("i")])])])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 349))

    def test_350(self):
        input = r"""
        Function: main
            Body:
                Var: a = {{1,2,3},{0xFF, 0XFF, 0o32, 0O32},{"a", "b", "c"}, {True, False, True}, {1.05, 2.34, 45.5, 898777}, {True, False}};
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], ArrayLiteral([ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3)]), ArrayLiteral([IntLiteral(255), IntLiteral(255), IntLiteral(26), IntLiteral(26)]), ArrayLiteral([StringLiteral(r"""a"""), StringLiteral(
            r"""b"""), StringLiteral(r"""c""")]), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False), BooleanLiteral(True)]), ArrayLiteral([FloatLiteral(1.05), FloatLiteral(2.34), FloatLiteral(45.5), IntLiteral(898777)]), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])]))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 350))

    def test_351(self):
        input = r"""
        Function: main
            Body:
                Var: a, b, c, d;
                a = (b +. c +. d *. (a \. b)) % 2;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None)], [
                         Assign(Id("a"), BinaryOp("%", BinaryOp("+.", BinaryOp("+.", Id("b"), Id("c")), BinaryOp("*.", Id("d"), BinaryOp("\\.", Id("a"), Id("b")))), IntLiteral(2)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 351))

    def test_352(self):
        input = r"""
        Function: main
            Body:
                Break;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Break()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 352))

    def test_353(self):
        input = r"""
        Function: main
            Body:
                Continue;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Continue()]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 353))

    def test_354(self):
        input = r"""
        Function: main
            Body:
                Return;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Return(None)]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 354))

    def test_355(self):
        input = r"""
        Function: main
            Body:
                Return 1;
            EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Return(IntLiteral(1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 355))

    def test_356(self):
        input = r"""
        Function: main
            Body:
                Var: a = 0;
                Return a + 1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], IntLiteral(0))], [
                         Return(BinaryOp("+", Id("a"), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 356))

    def test_357(self):
        input = r"""
        Function: main
            Body:
                Return foo(a);
            EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Return(CallExpr(Id("foo"), [Id("a")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 357))

    def test_358(self):
        input = r"""
        Function: main
            Body:
                Return 1 + foo(a, True, False, 0.8)[1][2][3];
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Return(BinaryOp("+", IntLiteral(1), ArrayCell(CallExpr(Id("foo"), [Id(
            "a"), BooleanLiteral(True), BooleanLiteral(False), FloatLiteral(0.8)]), [IntLiteral(1), IntLiteral(2), IntLiteral(3)])))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 358))

    def test_359(self):
        input = r"""
        Function: main
            Body:
                Return foo(foo(foo(foo())));
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Return(CallExpr(Id("foo"), [
                         CallExpr(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 359))

    def test_360(self):
        input = r"""
        Function: main
            Parameter: a,b,c,d
            Body:
                a[3 + foo(0xFF, True, 0XFF)] = 0;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None)], ([], [
                         Assign(ArrayCell(Id("a"), [BinaryOp("+", IntLiteral(3), CallExpr(Id("foo"), [IntLiteral(255), BooleanLiteral(True), IntLiteral(255)]))]), IntLiteral(0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 360))

    def test_361(self):
        input = r"""
        Function: main
            Body:
                Var: a;
                a = 1e1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None)], [
                         Assign(Id("a"), FloatLiteral(10.0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 361))

    def test_362(self):
        input = r"""
        Function: main
            Body:
                a = 1e1;
                b = 1e10;
                c = 1E1;
                d = 1E10;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), FloatLiteral(10.0)), Assign(Id("b"), FloatLiteral(
            10000000000.0)), Assign(Id("c"), FloatLiteral(10.0)), Assign(Id("d"), FloatLiteral(10000000000.0))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 362))

    def test_363(self):
        input = r"""
        Function: main
            Body:
                a = 1e+1;
                b = 1E+1;
                c = 1e-1;
                d = 1E-1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), FloatLiteral(10.0)), Assign(
            Id("b"), FloatLiteral(10.0)), Assign(Id("c"), FloatLiteral(0.1)), Assign(Id("d"), FloatLiteral(0.1))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 363))

    def test_364(self):
        input = r"""
        Function: main
            Body:
                Var: a,b,c,d,e;
                a = True;
                b = a;
                c = False;
                d = !c;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None), VarDecl(
            Id("e"), [], None)], [Assign(Id("a"), BooleanLiteral(True)), Assign(Id("b"), Id("a")), Assign(Id("c"), BooleanLiteral(False)), Assign(Id("d"), UnaryOp("!", Id("c")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 364))

    def test_365(self):
        input = r"""
        Function: main
            Body:
                Var: a,b,c,d,string;
                string = "123456789";
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(
            Id("d"), [], None), VarDecl(Id("string"), [], None)], [Assign(Id("string"), StringLiteral(r"""123456789"""))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 365))

    def test_366(self):
        input = r"""
        Function: main
            Body:
                Var: a,b,c,d;
                a = {1, {1, {1, {1, {1, {1, {1, {1, {1, {1, {1, {1, {1, {{1}, 1}, 1}, 1}, 1}, 1}, 1}, 1}, 1}, 1}, 1}, 1}, 1}, 1}, 1};
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(Id("c"), [], None), VarDecl(Id("d"), [], None)], [Assign(Id("a"), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral(
            [IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([IntLiteral(1), ArrayLiteral([ArrayLiteral([IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]), IntLiteral(1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 366))

    def test_367(self):
        input = r"""
        Function: main
            Body:
                a = {{{{{{{{{{{{{{{{True}}}}}}}}}}}}}}}};
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral(
            [ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([BooleanLiteral(True)])])])])])])])])])])])])])])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 367))

    def test_368(self):
        input = r"""
        Function: main
            Body:
                a = foo(a);
            EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Assign(Id("a"), CallExpr(Id("foo"), [Id("a")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 368))

    def test_369(self):
        input = r"""
        Function: main
            Body:
                a = foo(a)[2];
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(
            Id("a"), ArrayCell(CallExpr(Id("foo"), [Id("a")]), [IntLiteral(2)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 369))

    def test_370(self):
        input = r"""
        Function: main
            Body:
                a = (((((a)))));
            EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [Assign(Id("a"), Id("a"))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 370))

    def test_371(self):
        input = r"""
        Function: main
            Body:
                a = 1*1;
                b = 1*.1;
                c = 1 \ 1;
                d = 1 \. 1; 
                e = 1 % 1;
                f = 1 %. 1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), BinaryOp("*", IntLiteral(1), IntLiteral(1))), Assign(Id("b"), BinaryOp("*.", IntLiteral(1), IntLiteral(1))), Assign(Id("c"), BinaryOp("\\", IntLiteral(
            1), IntLiteral(1))), Assign(Id("d"), BinaryOp("\\.", IntLiteral(1), IntLiteral(1))), Assign(Id("e"), BinaryOp("%", IntLiteral(1), IntLiteral(1))), Assign(Id("f"), BinaryOp("%.", IntLiteral(1), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 371))

    def test_372(self):
        input = r"""
        Function: main
            Body:
                a = 1 + 1;
                b = 1 +. 0.25;
                c = 1 - 1;
                d = 1 -. -1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), BinaryOp("+", IntLiteral(1), IntLiteral(1))), Assign(Id("b"), BinaryOp("+.", IntLiteral(1),
                                                                                                                                                FloatLiteral(0.25))), Assign(Id("c"), BinaryOp("-", IntLiteral(1), IntLiteral(1))), Assign(Id("d"), BinaryOp("-.", IntLiteral(1), UnaryOp("-", IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 372))

    def test_373(self):
        input = r"""
        Function: main
            Body:
                a = 1--1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(
            Id("a"), BinaryOp("-", IntLiteral(1), UnaryOp("-", IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 373))

    def test_374(self):
        input = r"""
        Function: main
            Body:
                a = 1+-1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(
            Id("a"), BinaryOp("+", IntLiteral(1), UnaryOp("-", IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 374))

    def test_375(self):
        input = r"""
        Function: main
            Body:
                a = 1*.-1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(
            Id("a"), BinaryOp("*.", IntLiteral(1), UnaryOp("-", IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 375))

    def test_376(self):
        input = r"""
        Function: main
            Body:
                a = 1 <= a;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(
            Id("a"), BinaryOp("<=", IntLiteral(1), Id("a")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 376))

    def test_377(self):
        input = r"""
        Function: main
            Body:
                a = 1 <=. a;
                b = 1 >=. a;
                b = 1 || a;
                c = a && c;
            EndBody.

"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), BinaryOp("<=.", IntLiteral(1), Id("a"))), Assign(Id("b"), BinaryOp(
            ">=.", IntLiteral(1), Id("a"))), Assign(Id("b"), BinaryOp("||", IntLiteral(1), Id("a"))), Assign(Id("c"), BinaryOp("&&", Id("a"), Id("c")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 377))

    def test_378(self):
        input = r"""
        Function: main
            Body:
                a = !!1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(
            Id("a"), UnaryOp("!", UnaryOp("!", IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 378))

    def test_379(self):
        input = r"""
        Function: main
            Body:
                a = --1;
                b = -.-.1;
                c = !!1;
                d = 1 % 5 % 3;
                e = 1 + 2 * (a + b) -. d;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), UnaryOp("-", UnaryOp("-", IntLiteral(1)))), Assign(Id("b"), UnaryOp("-.", UnaryOp("-.", IntLiteral(1)))), Assign(Id("c"), UnaryOp("!", UnaryOp("!", IntLiteral(1)))),
                                                         Assign(Id("d"), BinaryOp("%", BinaryOp("%", IntLiteral(1), IntLiteral(5)), IntLiteral(3))), Assign(Id("e"), BinaryOp("-.", BinaryOp("+", IntLiteral(1), BinaryOp("*", IntLiteral(2), BinaryOp("+", Id("a"), Id("b")))), Id("d")))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 379))

    def test_380(self):
        input = r"""
        Function: main
            Parameter: a
            Body:
                a = !-1;
                b = !-.1;
                c = --.1;
                d = -.-1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None)], ([], [Assign(Id("a"), UnaryOp("!", UnaryOp("-", IntLiteral(1)))), Assign(Id("b"), UnaryOp(
            "!", UnaryOp("-.", IntLiteral(1)))), Assign(Id("c"), UnaryOp("-", UnaryOp("-.", IntLiteral(1)))), Assign(Id("d"), UnaryOp("-.", UnaryOp("-", IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 380))

    def test_381(self):
        input = r"""
        Function: main
            Body:
                Var: a[1000];
                For(i = 0, i < 1000, 1) Do
                    a[i] = True;
                EndFor.
            EndBody.

"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [1000], None)], [For(Id("i"), IntLiteral(0), BinaryOp(
            "<", Id("i"), IntLiteral(1000)), IntLiteral(1), ([], [Assign(ArrayCell(Id("a"), [Id("i")]), BooleanLiteral(True))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 381))

    def test_382(self):
        input = r"""
        Function: main
            Body:
                Var: a[1000];
                For(i = 0, i < 1000, 1) Do
                    a[i] = True;
                EndFor.
                Do
                    If (a[i] != True) Then 
                        a[i] = True;
                    EndIf.
                i = i + 1;
                While (i < 1000)
                EndDo.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [1000], None)], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(1000)), IntLiteral(1), ([], [Assign(ArrayCell(Id("a"), [Id("i")]), BooleanLiteral(True))])), Dowhile(
            ([], [If([(BinaryOp("!=", ArrayCell(Id("a"), [Id("i")]), BooleanLiteral(True)), [], [Assign(ArrayCell(Id("a"), [Id("i")]), BooleanLiteral(True))])], ([], [])), Assign(Id("i"), BinaryOp("+", Id("i"), IntLiteral(1)))]), BinaryOp("<", Id("i"), IntLiteral(1000)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 382))

    def test_383(self):
        input = r"""
        Function: main
            Body:
                a = (a < b) && (d >= d);
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), BinaryOp(
            "&&", BinaryOp("<", Id("a"), Id("b")), BinaryOp(">=", Id("d"), Id("d"))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 383))

    def test_384(self):
        input = r"""
        Function: main
            Body:
                a = 1+-1;
            EndBody.        
        

"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(
            Id("a"), BinaryOp("+", IntLiteral(1), UnaryOp("-", IntLiteral(1))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 384))

    def test_385(self):
        input = r"""
        Function: main
            Body:
                a = a + b || c - d;
            EndBody.    
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), BinaryOp(
            "||", BinaryOp("+", Id("a"), Id("b")), BinaryOp("-", Id("c"), Id("d"))))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 385))

    def test_386(self):
        input = r"""
        Function: main
            Parameter: a,b,c,d
            Body:
                Var: a = 1;

            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("a"), [], None), VarDecl(Id("b"), [], None), VarDecl(
            Id("c"), [], None), VarDecl(Id("d"), [], None)], ([VarDecl(Id("a"), [], IntLiteral(1))], []))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 386))

    def test_387(self):
        input = r"""
        Function: main
            Body:
                Var: a = 0;
                For (i = 0, i < 100, 1) Do
                    a = !-1;
                    a = !-.1;
                    a = --.1;
                    a = -.-1;
                EndFor.
                While (a < 100) Do
                    a = !-1;
                    a = !-.1;
                    a = --.1;
                    a = -.-1;                    
                a = a + 1;
                EndWhile.   
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], IntLiteral(0))], [For(Id("i"), IntLiteral(0), BinaryOp("<", Id("i"), IntLiteral(100)), IntLiteral(1), ([], [Assign(Id("a"), UnaryOp("!", UnaryOp("-", IntLiteral(1)))), Assign(Id("a"), UnaryOp("!", UnaryOp("-.", IntLiteral(1)))), Assign(Id("a"), UnaryOp("-", UnaryOp("-.", IntLiteral(1)))), Assign(Id("a"), UnaryOp("-.", UnaryOp(
            "-", IntLiteral(1))))])), While(BinaryOp("<", Id("a"), IntLiteral(100)), ([], [Assign(Id("a"), UnaryOp("!", UnaryOp("-", IntLiteral(1)))), Assign(Id("a"), UnaryOp("!", UnaryOp("-.", IntLiteral(1)))), Assign(Id("a"), UnaryOp("-", UnaryOp("-.", IntLiteral(1)))), Assign(Id("a"), UnaryOp("-.", UnaryOp("-", IntLiteral(1)))), Assign(Id("a"), BinaryOp("+", Id("a"), IntLiteral(1)))]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 387))

    def test_388(self):
        input = r"""
        Function: main
            Body:
                foo();
            EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [CallStmt(Id("foo"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 388))

    def test_389(self):
        input = r"""
        Function: main
            Body:
                Var: a, b;
                foo1();
                foo2();
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([VarDecl(Id("a"), [], None), VarDecl(
            Id("b"), [], None)], [CallStmt(Id("foo1"), []), CallStmt(Id("foo2"), [])]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 389))

    def test_390(self):
        input = r"""
        Function: main
            Body:
                If True Then
                EndIf.
            EndBody.
"""
        expect = Program(
            [FuncDecl(Id("main"), [], ([], [If([(BooleanLiteral(True), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 390))

    def test_391(self):
        input = r"""
        Function: main
            Body:
                If True Then
                    Var: a;
                EndIf.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [
                         If([(BooleanLiteral(True), [VarDecl(Id("a"), [], None)], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 391))

    def test_392(self):
        input = r"""
        Function: main
            Body:
                If True Then
                ElseIf True Then
                ElseIf True Then
                EndIf.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [If([(BooleanLiteral(True), [], [
        ]), (BooleanLiteral(True), [], []), (BooleanLiteral(True), [], [])], ([], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 392))

    def test_393(self):
        input = r"""
        Function: main
            Body:
                If True Then
                Else
                    Var: a;
                EndIf.
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [
                         If([(BooleanLiteral(True), [], [])], ([VarDecl(Id("a"), [], None)], []))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 393))

    def test_394(self):
        input = r"""
        Function: main
            Body:
                a = { 1, 2, 3, 4 };
                a = { 1.0, 2.0, 3.0, 4.0 };
                a = { True, False };
                a = { {1,2}, {3,4} };
                a = {{{{{1}}}}};
                a = {{{{{1}}}}, {1}, 1};
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), ArrayLiteral([IntLiteral(1), IntLiteral(2), IntLiteral(3), IntLiteral(4)])), Assign(Id("a"), ArrayLiteral([FloatLiteral(1.0), FloatLiteral(2.0), FloatLiteral(3.0), FloatLiteral(4.0)])), Assign(Id("a"), ArrayLiteral([BooleanLiteral(True), BooleanLiteral(False)])), Assign(Id("a"), ArrayLiteral(
            [ArrayLiteral([IntLiteral(1), IntLiteral(2)]), ArrayLiteral([IntLiteral(3), IntLiteral(4)])])), Assign(Id("a"), ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])])])), Assign(Id("a"), ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([ArrayLiteral([IntLiteral(1)])])])]), ArrayLiteral([IntLiteral(1)]), IntLiteral(1)]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 394))

    def test_395(self):
        input = r"""
        Function: main
            Body:
                a = foo();
                a = foo(1, True, "", 1.);
                a = foo(foo(foo()));
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [], ([], [Assign(Id("a"), CallExpr(Id("foo"), [])), Assign(Id("a"), CallExpr(Id("foo"), [IntLiteral(1), BooleanLiteral(
            True), StringLiteral(""), FloatLiteral(1.0)])), Assign(Id("a"), CallExpr(Id("foo"), [CallExpr(Id("foo"), [CallExpr(Id("foo"), [])])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 395))

    def test_396(self):
        input = r"""
        Function: assign
            Parameter: x,y,z
            Body:
                x = 1;
                y = 2.05e-3;
                z = "apple";
            EndBody.
"""
        expect = Program([FuncDecl(Id("assign"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], ([], [
                         Assign(Id("x"), IntLiteral(1)), Assign(Id("y"), FloatLiteral(0.00205)), Assign(Id("z"), StringLiteral(r"""apple"""))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 396))

    def test_397(self):
        input = r"""
        Function: sthg
            Parameter: x,y,z
            Body:
                x = -1 - 1 -1;
            EndBody.
"""
        expect = Program([FuncDecl(Id("sthg"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], ([], [
                         Assign(Id("x"), BinaryOp("-", BinaryOp("-", UnaryOp("-", IntLiteral(1)), IntLiteral(1)), IntLiteral(1)))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 397))

    def test_398(self):
        input = r"""
        Function: sthg
            Parameter: x,y,z
            Body:
                a = foo(a);
            EndBody.
"""
        expect = Program([FuncDecl(Id("sthg"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(
            Id("z"), [], None)], ([], [Assign(Id("a"), CallExpr(Id("foo"), [Id("a")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 398))

    def test_399(self):
        input = r"""
        Function: sthg
            Parameter: x,y,z
                Body:
                    x = x(x);
                EndBody.
"""
        expect = Program([FuncDecl(Id("sthg"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(
            Id("z"), [], None)], ([], [Assign(Id("x"), CallExpr(Id("x"), [Id("x")]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 399))

    def test_400(self):
        input = r"""
        Function: main
            Parameter: x,y,z
            Body:
                x = foo(foo(y+foo(y)));
            EndBody.
"""
        expect = Program([FuncDecl(Id("main"), [VarDecl(Id("x"), [], None), VarDecl(Id("y"), [], None), VarDecl(Id("z"), [], None)], ([], [
                         Assign(Id("x"), CallExpr(Id("foo"), [CallExpr(Id("foo"), [BinaryOp("+", Id("y"), CallExpr(Id("foo"), [Id("y")]))])]))]))])
        self.assertTrue(TestAST.checkASTGen(input, expect, 400))

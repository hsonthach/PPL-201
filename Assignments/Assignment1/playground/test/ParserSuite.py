import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_func_call(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   foo (2 + x, a[3]);
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_return(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    Return 3 + foo (2 + x, 4. \. y);
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 202))

    def test_call1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    foo (2 + x, 4. \. y);
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_continue(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    deadline = is = coming =Continue ; 
EndBody.
"""
        expect = r"Error on line 5 col 18: ="
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_break(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    Do Break;   While a==3 EndDo.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 205))

    def test_do_while_nest_while_do(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    Do While a==2 Do a=3; EndWhile.  While a==3 EndDo.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 206))

    def test_do_while(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Do get[i][some][help] = "NO" ; While expression EndDo.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 207))

    def test_error_func_delare3(self):
        input = r"""
Function: 
Parameter: a[3]
Body:
   var: a =3 ; 
EndBody.
"""
        expect = r"Error on line 3 col 0: Parameter"
        self.assertTrue(TestParser.checkParser(input, expect, 208))

    def test_error_func_delare1(self):
        input = r"""
Function: foo
Parameter: a[3]
Body:
   var: a =3 ; 
EndBody.
"""
        expect = r"Error on line 5 col 6: :"
        self.assertTrue(TestParser.checkParser(input, expect, 209))

    def test_error_func_delare(self):
        input = r"""
Function: foo
Parameter: 
Body:
   Var: a =3 ; 
EndBody.
"""
        expect = r"Error on line 4 col 0: Body"
        self.assertTrue(TestParser.checkParser(input, expect, 210))

    def test_error_declare3(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Var: a = a{1,2,3};
EndBody.
"""
        expect = r"Error on line 5 col 13: {"
        self.assertTrue(TestParser.checkParser(input, expect, 211))

    def test_error_declare2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Var: a = ((a) ; 
EndBody.
"""
        expect = r"Error on line 5 col 17: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_error_declare1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Var: a =a3] ; 
EndBody.
"""
        expect = r"Error on line 5 col 13: ]"
        self.assertTrue(TestParser.checkParser(input, expect, 213))

    def test_error_declare(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Var =3 ; 
EndBody.
"""
        expect = r"Error on line 5 col 7: ="
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_error3(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Var  a =3 ; 
EndBody.
"""
        expect = r"Error on line 5 col 8: a"
        self.assertTrue(TestParser.checkParser(input, expect, 215))

    def test_error4(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
  True;
EndBody.
"""
        expect = r"Error on line 5 col 6: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 216))

    def test_error2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   hey = jude[i;]
EndBody.
"""
        expect = r"Error on line 5 col 15: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 217))

    def test_error1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   hey = jude[i ;
EndBody.
"""
        expect = r"Error on line 5 col 16: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 218))

    def test_error_semi(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   foo((let(it(be()))))
EndBody.
"""
        expect = r"Error on line 6 col 0: EndBody"
        self.assertTrue(TestParser.checkParser(input, expect, 219))

    def test_call(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   foo((let(it(be()))));
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_while3(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    For (i = 0, i < 10, 2) Do
    While (foo()) Do a = a+1 ;
      If ((3==2) && (3==3)) && (3 == 3) Then foo(0);  
      ElseIf (3==3) Then Return hello();
      EndIf.
        EndWhile. EndFor.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 221))

    def test_while2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    For (i = 0, i < 10, 2) Do writeln(i); EndFor.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_while1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      While (foo()) Do a = a+1 ;
      If ((3==2) && (3==3)) && (3 == 3) Then foo(0);  
      ElseIf (3==3) Then Return hello();
      EndIf.
        EndWhile.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 223))

    def test_while(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      While (True) Do a = a+1 ;  EndWhile.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 224))

    def test_complex(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      While (True) Do   While (foo()) Do a = a+1 ;
      If ((3==2) && (3==3)) && (3 == 3) Then foo(0);  
      ElseIf (3==3) Then Return hello();
      EndIf.
        EndWhile. EndWhile.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 225))

    def test_complex1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      While (True) Do  While (True) Do   While (foo()) Do a = a+1 ;
      If ((3==2) && (3==3)) && (3 == 3) Then foo(0);  
      ElseIf (3==3) Then Return hello();
      EndIf.
        EndWhile. EndWhile.  While (foo()) Do a = a+1 ;
      If ((3==2) && (3==3)) && (3 == 3) Then foo(0);  
      ElseIf (3==3) Then Return hello();
      EndIf.
        EndWhile. EndWhile.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_if5(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      If ((3==2) && (3==3)) && (3 == 3) Then foo(0);  
      ElseIf (3==3) Then Return hello();
      EndIf.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_if4(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      If ((3==2) && (3==3)) && (3 == 3) Then foo(0);  EndIf.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 228))

    def test_if3(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      If False && 3 == 3 Then foo(0);  EndIf.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 229))

    def test_if2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      If False Then foo(0);  EndIf.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_if1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      If (a==5) && b==2 Then foo(0);  EndIf.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 231))

    def test_if(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      If (a==5) || b==2 Then foo(0);  EndIf.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_bool(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      a = (3<5) == True ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_bool1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      a = (3<5) == True && (2>5); 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_bool2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      a = (3<5) == True && (2>5) || (5>2); 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 235))

    def test_precedence(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      a = 2 * foo(3,5,a[3]) ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 236))

    def test_precedence1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      a = 2 * (foo(3,5,!a[3]) =/= 3)  ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 237))

    def test_precedence2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      a = 2 * ((foo(3,5,!a[3]) =/= 3) && False) ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 238))

    def test_assign5(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
      foo(2)[3+x] = a[b[f+y[2]-h[t[5+j]] * 4]] + 3;
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 239))

    def test_assign4(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    foo(2)[3+x] = a[b[f+y[2]]] + 3;
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 240))

    def test_assign3(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    a = {12,3,{1,2}} = foo() ;
EndBody.
"""
        expect = r"Error on line 5 col 21: ="
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_exp(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    a = getArray(getID())[3] ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_assign2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    a = {12,3,{1,2}};
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_assign1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    a = {12,3,{1,2}};
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_assign(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    a = b = c ; 
EndBody.
"""
        expect = r"Error on line 5 col 10: ="
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_stmt8(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    a = getPointer()[2] ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_stmt7(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
Var: r = 10., v;
v = (4. \. 3.) *. 3.14 *. r *. r *. r;
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_func1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
If bool_of_string ("True") Then
a = int_of_string (read ());
b = float_of_int (a) +. 2.0;
EndIf.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_index_op(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
a[3 + foo(2)] = a[b[2][3]] + 4;
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_func_declare2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
Var: i = 0;
While (i < 5)
Do
a[i] = b +. 1.0;
i = i + 1;
EndWhile.
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_arr_declare(self):
        input = r"""
Var: a[5] = {1,4,3,2,0};
Var: b[2][3]={{1,2,3},{4,5,6}};
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_func_declare1(self):
        input = r"""
Var: x;
Function: fact
Parameter: n
Body:
If n == 0 Then
Return 1;
Else
Return n * fact (n - 1);
EndIf.
EndBody.
Function: main
Body:
x = 10;
fact (x);
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_arr_declare3(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Var : a = {1,    3 ,   4} ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_arr_declare4(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Var : a = {True ,   False, "String"} ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_arr_declare5(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Var : a = {3,  {True ,   False, "String"}} ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_arr_declare6(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
   Var : a = {{1},{3,  {True ,   False, "String"}} } ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_null_func(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_index_exp(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    b = a[a[a[a[a[a[a[a]]]]]]] ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_index_exp1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    b = a[foo(a[a[a[a[a[a[a[a]]]]]]])] ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_index_exp2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    b = a[((2%3 *. 3.0)==3) && (3==3)];
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_index_exp3(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    b = a[((2%3 *. 3.0)==3) && (3==3) -2.e3 +0x11];
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_comment(self):
        input = r"""
** Empty program, more likes empty life **
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_comment1(self):
        input = r"""
** Empty program, more likes empty life 
 One mul zero is zero**
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_var1(self):
        input = r"""
Var: a = 5;
Var: b[2][3] = {{2,3,4},{4,5,6}};
Var: c, d = 6, e, f;
Var: m, n[10];
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_sign_expression(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    b = -3 + -3 --3 ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_sign_expression1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    b = -.3.0 ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_sign_expression2(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    b = -.----.3.0 ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_not_expression(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    b = !((-3 + -3 --3) == -3) ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_not_expression1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    b = !!!!!((-3 + -3 --3) == -3) ; 
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_return_break(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    Return Break;
EndBody.
"""
        expect = r"Error on line 5 col 11: Break"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_return_continue(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    Return Continue;
EndBody.
"""
        expect = r"Error on line 5 col 11: Continue"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_return_null(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    Return ;
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_return_return(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    Return Return ; ;
EndBody.
"""
        expect = r"Error on line 5 col 11: Return"
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_return_return1(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    Return ;
    Return ;
EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_return_func(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    Return() ;
EndBody.
"""
        expect = r"Error on line 5 col 11: )"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_index_exp_assign(self):
        input = r"""
Function: foo
Parameter: a[5], b
Body:
    a = a[5][5] = b[3][3] = c [3<4] ; 
EndBody.
"""
        expect = r"Error on line 5 col 16: ="
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_stmt6(self):
        input = r"""
Var:m,n[10] ;
Function : main
    Body:
      Return hello(n);
    EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_stmt5(self):
        input = r"""
Var:m,n[10] ;
Function : main
    Body:
      Continue;
    EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_stmt4(self):
        input = r"""
Var:m,n[10] ;
Function : main
    Body:
        Break;
    EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_stmt3(self):
        input = r"""
Var:m,n[10] ;
Function : main
    Body:
        Do a=3; While expression EndDo.
    EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_stmt2(self):
        input = r"""
Var:m,n[10] ;
Function : main
    Body:
        While expression Do a=3 ; EndWhile.
    EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_stmt1(self):
        input = r"""
Var:m,n[10] ;
Function : main
    Body:
        For (i = 0, i < 10, 2) Do a=3 ; EndFor.
    EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_stmt(self):
        input = r"""
Var:m,n[10] ;
Function : fact
    Parameter: n
    Body:
        If expression Then a=3 ;
ElseIf expression Then b=4 ; 
ElseIf expression Then c =5 ; 
EndIf.
    EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_variable_declare_func(self):
        input = r"""
Var:m,n[10] ;
Function : fact
    Parameter: n
    Body:
        Var: r = 10, v ; 
        v = 3; 
    EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_func(self):
        input = r"""
Var:m,n[10] ;
Function : fact
    Parameter: n
    Body:
        If n == 6 Then
        Return 1;
        Else
        Return n * fact (n - 1);
        EndIf.
    EndBody.
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_var_dec3(self):
        input = """Var:m,n[10] ; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_var_dec2(self):
        input = """Var: c,d = 6,e,f ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_var_dec1(self):
        input = """Var: b[2][3] = {{2,3,4},{4,5,6}} ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_var_dec(self):
        input = """Var: a=5 ;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_1_var_decl(self):
        """ Test Var Declare 1 line 1 var """
        input = r"""
Var : a= 3;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_2_var_decl(self):
        """ Test Var Declare 1 line n var """
        input = r"""
Var :a, b, c= 4;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_3_var_decl(self):
        """ Test Var Declare n line """
        input = r"""
Var :a, b, c= 3;
Var :x, y= 3.e2;
Var :z= "string";
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_4_Var_decl(self):
        """ Test Var Declare array """
        input = r"""
Var :a ,  array[1][3] ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_5_Var_decl(self):
        """ Test Var Declare """
        input = r"""
Var :a, b, c,array[1][3]  ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_6_Var_decl(self):
        """ Test Var Declare """
        input = r"""
Var : a, b, c = 3;
 Var : z = False ;
 Var   :garray[1][3] ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_7_Var_decl(self):
        """ Test Var Declare """
        input = r"""
Var : a, b, c = 3;
 Var : z = False ;
 Var   :garray[1][3] ;
 Var   : d = foo(False[1][3]) ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_8_Var_decl(self):
        """ Test Var Declare """
        input = r"""
Var :a = "String '"s String" ; 
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_Var_decl(self):
        input = r"""
Var: x=10,y=9,z=8 ;
"""
        expect = r"successful"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_simple_program(self):
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 300))

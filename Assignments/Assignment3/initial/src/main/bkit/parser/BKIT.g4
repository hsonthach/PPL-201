grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    elif tk == self.UNTERMINATED_COMMENT:
        raise UnterminatedComment()
    else:
        return result;
}

options {
	language = Python3;
}

/** Parser Declaration */
program: (var_declare)* (func_declare)* EOF;

//********* 2.1 Variable declaration
var_declare: VAR COLON (variable_assign_list) SEMI;

// Ex : a,b=5,c = 6,d[3]
variable_assign_list: variable_assign (COMMA variable_assign)*;

// Ex: a = 5  | a | a[5] = {1,2,3} 
variable_assign: variable (ASSIGN literal)?;

//********* 2.2 Function declarations

// Ex : Function : hello 
func_declare: FUNC COLON ID param_declare? body;

// Ex: Parameter: n
param_declare: PARAMETER COLON param_list;
param_list: variable (COMMA variable)*;

body: BODY COLON list_statement END_BODY DOT;

//********* 3. Statement
list_statement: var_declare* statement*;
statement: (
		assignment_stmt
		| if_stmt
		| for_stmt
		| while_stmt
		| do_while_stmt
		| break_stmt
		| continue_stmt
		| call_stmt
		| return_stmt
	);

//********* 3.1 Assignment statement 

// Ex: a= b =3  ;
assignment_stmt: assign_body SEMI;
assign_body: assign_head ASSIGN exp;
assign_head: ID | index_exp;
//assign_tail: assign_head ASSIGN assign_tail | exp;

//********* 3.2 If statement

/*
 Ex: If a==3 Then a=5 ; ElseIf expression Then statement-list ElseIf expression Then statement-list
 Else statement-list EndIf.
 */
if_stmt:
	IF exp THEN list_statement (else_if_stmt)* (else_stmt)? END_IF DOT;

/*
 Ex:ElseIf expression Then statement-list
 */
else_if_stmt: ELSE_IF exp THEN list_statement;

/*
 Ex: Else statement-list
 */
else_stmt: ELSE list_statement;

//********* 3.3 For statement

/*
 Ex: For (i = 0, i < 10, 2) Do writeln(i); EndFor.
 */
for_stmt:
	FOR LP ID ASSIGN exp COMMA exp COMMA exp RP DO list_statement END_FOR DOT;

//********* 3.4 While Statement
/*
 Ex:While expression Do statement-list EndWhile.
 */
while_stmt: WHILE exp DO list_statement END_WHILE DOT;

//********* 3.5 Do-while Statement

/*
 Ex: Do statement-list While expression EndDo.
 */
do_while_stmt: DO list_statement WHILE exp END_DO DOT;

//********* 3.6 Break Statement
/*
 Ex:Break ;
 */
break_stmt: BREAK SEMI;

//********* 3.7 Continue Statement Ex:Continue ; */
continue_stmt: CONTINUE SEMI;

//********* 3.8 Call Statement
/*
 Ex:foo (2 + x, 4. \. y);
 */
call_stmt: ID LP exps_list RP SEMI;

//********* 3.9 Return statement
/*
 Ex:Return 3 + foo (2 + x, 4. \. y);
 */
return_stmt: RETURN exp? SEMI;

/*  Utils */
/*
 Ex:foo (2 + x, 4. \. y);
 */
func_call: ID LP exps_list RP;
exps_list: (exp (COMMA exp)*)?;

bool_literal: 'True' | 'False';

// Ex: a[3][4] | a
variable: ID | array_type;

array_type: ID (LSB INTEGER_LITERAL RSB)+;

literal: (
		INTEGER_LITERAL
		| FLOAT_LITERAL
		| array_literal
		| bool_literal
		| STRING_LITERAL
	);
// { "abc", 3 }
array_literal: LCP (literal (COMMA literal)*) RCP;

/*
 ==, ! =, <, >, <=, >=, = / =, < ., > ., <= ., >= .
 */
// 4.Expression Relation
exp:
	exp1 (
		INT_EQ
		| INT_NEQ
		| INT_LT
		| INT_GT
		| INT_LTE
		| INT_GTE
		| FLOAT_NEQ
		| FLOAT_LT
		| FLOAT_GT
		| FLOAT_LTE
		| FLOAT_GTE
	) exp1
	| exp1;
// Logical
exp1: exp1 (AND | OR) exp2 | exp2;
// Adding
exp2:
	exp2 (INT_ADD | FLOAT_ADD | FLOAT_SUB | INT_SUB) exp3
	| exp3;
// Multiplying
exp3:
	exp3 (INT_MUL | FLOAT_MUL | FLOAT_DIV | INT_DIV | INT_MOD) exp4
	| exp4;
// Logical
exp4: (NOT) exp4 | exp5;
// Sign
exp5: (FLOAT_SUB | INT_SUB) exp5 | index_exp;

// Index ID (LSB exp RSB)+; foo()[3]
index_exp: exp7 (LSB exp RSB)*;

// Function call
exp7: ID LP exps_list RP | exp8;
// Parentheses
exp8: LP exp RP | ID | literal;

/** Lexers Declaration */

/* ----------------------------------------------------------------------------------- SEPARATOR
 * -----------------------------------------------------------------------------------
 */

SEMI: ';';

COLON: ':';

COMMA: ',';

LSB: '[';
// Square bracket left 

RSB: ']';
// Square bracket right 

LCP: '{';

RCP: '}';

LP: '(';

RP: ')';

DOT: '.';

/* ----------------------------------------------------------------------------------- KeyWords
 * -----------------------------------------------------------------------------------
 */
BODY: 'Body';

BREAK: 'Break';

CONTINUE: 'Continue';

DO: 'Do';

ELSE: 'Else';

ELSE_IF: 'ElseIf';

END_BODY: 'EndBody';

END_IF: 'EndIf';

END_FOR: 'EndFor';

END_WHILE: 'EndWhile';

FOR: 'For';

FUNC: 'Function';

IF: 'If';

PARAMETER: 'Parameter';

RETURN: 'Return';

VAR: 'Var';

THEN: 'Then';

WHILE: 'While';

TRUE: 'True';

FALSE: 'False';

END_DO: 'EndDo';

/* ----------------------------------------------------------------------------------- Operators
 * -----------------------------------------------------------------------------------
 */

INT_ADD: '+';
INT_SUB: '-';
INT_MUL: '*';
INT_DIV: '\\';
INT_MOD: '%';

INT_EQ: '==';
INT_NEQ: '!=';
INT_LT: '<';
INT_GT: '>';
INT_LTE: '<=';
INT_GTE: '>=';

FLOAT_ADD: '+.';
FLOAT_SUB: '-.';
FLOAT_MUL: '*.';
FLOAT_DIV: '\\.';

FLOAT_NEQ: '=/=';
FLOAT_LT: '<.';
FLOAT_GT: '>.';
FLOAT_LTE: '<=.';
FLOAT_GTE: '>=.';

AND: '&&';
NOT: '!';
OR: '||';
ASSIGN: '=';

/* ----------------------------------------------------------------------------------- literal
 * -----------------------------------------------------------------------------------
 */

INTEGER_LITERAL: OCT | DECIMAL | HEXA;

fragment DECIMAL: '0' | [1-9][0-9]*;

fragment DIGIT: [0-9];

fragment SIGN: [+-];
// 0o03 is valid but doesn't match with OCT
fragment OCT: [0][oO][1-7][0-7]*;

fragment HEXA: [0][xX][1-9A-F][0-9A-F]*;

FLOAT_LITERAL:
	DIGIT+ (
		DECIMAL_PART
		| EXPONENT_PART
		| DECIMAL_PART EXPONENT_PART
	);
fragment DECIMAL_PART: '.' DIGIT*;
fragment EXPONENT_PART: [Ee] [+-]? DIGIT+;

BOOLEAN_LITERAL: TRUE | FALSE;

// Every char that isn't ESC_ILLEGAL or is ESC_SEQ fragment 
STRING_LITERAL:
	["] STR_CHAR* ["] {
		y = str(self.text)
		self.text = y[1:-1]
	};

fragment STR_CHAR: ~([\b\t\n\f\r"'\\]) | ESC_SEQ;

fragment ESC_SEQ: ('\\' [btnfr'\\]) | ('\'"');

//fragment EXPONENT: [eE] SUB? DIGIT+;

//if , then , else endif, function call

WS: [ \t\r\n]+ -> skip;
// skip spaces, tabs, newlines ;

UNCLOSE_STRING:
	'"' STR_CHAR* ([\b\t\n\f\r] | EOF) {
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '\"', "\'", '\\']
		if y[-1] in possible:
			raise UncloseString(y[1:-1])
		else:
			raise UncloseString(y[1:])
	};
ILLEGAL_ESCAPE:
	'"' STR_CHAR* ESC_ILLEGAL {
		y = str(self.text)
		raise IllegalEscape(y[1:])
	};
fragment ESC_ILLEGAL: ('\\' ~[btnfr'\\]) | (['] ~["]);

ID: [a-z][_a-zA-Z0-9]*;
// ID have to be after key words to avoiding misunderstanding for antlr

// UNTERMINATED_COMMENT: '**' STR_CHAR* ([\b\t\n\f\r] | EOF) { raise UnterminatedComment() };
COMMENT_LITERAL: ('**' .*? '**') -> skip;

UNTERMINATED_COMMENT:
	'**' (~'*' | '*' ~'*') {
		raise UnterminatedComment()
	};
ERROR_CHAR: .;

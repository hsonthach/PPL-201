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

fragment DIGIT: [0-9];
fragment EXPONENT: [eE] [+-]? DIGIT+;

//-------------------Grammar---------------------------------

program: ( global_vardecl)* (func_decl)* EOF;
global_vardecl: VAR COLON vardecl_list SEMI;
vardecl_list: var_decl (COMMA var_decl)*;
var_decl: ID (LSB INTEGER_LITERAL RSB)* (ASSIGN literal)?;
para_decllist: para_decl (COMMA para_decl)*;
para_decl: ID (LSB INTEGER_LITERAL RSB)*;

func_decl:
	FUNCTION COLON ID (PARAMETER COLON para_decllist)? BODY COLON stmtList ENDBODY DOT;

stmtList: global_vardecl* stmt*;

stmt:
	ifStmt
	| assignStmt
	| whileStmt
	| forStmt
	| breakStmt
	| continueStmt
	| returnStmt
	| callStmt
	| doWhileStmt;

ifStmt: IF exp1 THEN stmtList (elifStmt)* (elseStmt)? ENDIF DOT;
elifStmt: ELSEIF exp1 THEN stmtList;
elseStmt: ELSE stmtList;

whileStmt: WHILE exp1 DO stmtList ENDWHILE DOT;

doWhileStmt: DO stmtList WHILE exp1 ENDDO DOT;

forStmt:
	FOR LP ID ASSIGN exp1 COMMA exp1 COMMA exp1 RP DO stmtList ENDFOR DOT;

callStmt: ID LP (exp1 (COMMA exp1)*)? RP SEMI;
breakStmt: BREAK SEMI;
continueStmt: CONTINUE SEMI;
returnStmt: RETURN exp1? SEMI;
argulist: (exp1 (COMMA exp1)*)?;
funcCall: ID LP (exp1 (COMMA exp1)*)? RP;
assignStmt: lhs ASSIGN exp1 SEMI;

lhs: ID | index_exp;

exp1:
	exp2 (
		LT
		| LTE
		| EQ
		| GT
		| GTE
		| NEQ
		| FNEQ
		| FLTE
		| FLT
		| FGTE
		| FGT
		| FEQ
	) exp2
	| exp2;
exp2: exp2 (AND | OR) exp3 | exp3;
exp3: exp3 (ADD | SUB | FADD | FSUB) exp4 | exp4;
exp4: exp4 ( DIV | MUL | MOD | FMUL | FDIV) exp5 | exp5;
exp5: NOT exp5 | exp6;
exp6: (SUB | FSUB) exp6 | index_exp;
index_exp: exp7 (LSB exp1 RSB)*;
exp7: operands;

literal:
	INTEGER_LITERAL
	| BOOLEAN_LITERAL
	| array_literal
	| FLOAT_LITERAL
	| STRING_LITERAL;

operands: literal | ID | funcCall | LP exp1 RP;

array_literal: LCB ( literal ( COMMA literal)*) RCB;

// Literal

INTEGER_LITERAL:
	[1-9][0-9]*
	| '0'
	| '0x' [_a-fA-F]* [0-9]*
	| '0X' [_a-fA-F]* [0-9]*
	| '0o' [0-7]*
	| '0O' [0-7]*;
FLOAT_LITERAL: (DIGIT)+ DOT (DIGIT | EXPONENT)*
	| DIGIT* DOT (DIGIT)+ EXPONENT?
	| DIGIT+ EXPONENT;
BOOLEAN_LITERAL: TRUE | FALSE;
STRING_LITERAL:
	["] STR_CHAR* ["] {
		y = str(self.text)
		self.text = y[1:-1]
	};

// ----------------------------------------------------------------------------------------
DOT: '.';
//Comment

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '\\';
MOD: '%';
NOT: '!';
AND: '&&';
OR: '||';

ASSIGN: '=';
LTE: '<=';
GTE: '>=';
NEQ: '!=';
EQ: '==';
LT: '<';
GT: '>';

FADD: '+.';
FSUB: '-.';
FMUL: '*.';
FDIV: '\\.';

FLTE: '<=.';
FGTE: '>=.';
FNEQ: '=\\=';
FEQ: '=.';
FLT: '<.';
FGT: '>.';
//------------------------------------------------------------------

//----------Lexer----------//

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

LP: '(';
RP: ')';
LCB: '{';
RCB: '}';
LSB: '[';
RSB: ']';

SEMI: ';';
COMMA: ',';
COLON: ':';
number: SUB? INTEGER_LITERAL;

FUNCTION: 'Function';

BODY: 'Body';
END: 'End';
PARAMETER: 'Parameter';

TRUE: 'True';
FALSE: 'False';

IF: 'If';
THEN: 'Then';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDIF: 'EndIf';
ENDDO: 'EndDo';
ENDBODY: 'EndBody';

FOR: 'For';
WHILE: 'While';
DO: 'Do';
TO: 'To';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';

RETURN: 'Return';
BREAK: 'Break';
CONTINUE: 'Continue';

primitive_types: INTEGER | FLOAT | STRING | BOOLEAN;
INTEGER: 'int';
STRING: 'string';
FLOAT: 'float';
BOOLEAN: 'boolean';
VAR: 'Var';
OF: 'of';

COMMENT_LITERAL: ('**' .*? '**') -> skip;

ID: [a-z][_a-zA-Z0-9]*;

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

UNTERMINATED_COMMENT:
	'**' (~'*' | '*' ~'*') {
		raise UnterminatedComment()
	};

fragment STR_CHAR: ~([\b\t\n\f\r"'\\]) | ESC_SEQ;

fragment ESC_SEQ: ('\\' [btnfr'\\]) | ('\'"');

ERROR_CHAR: .;
//fragment EXPONENT: [eE] SUB? DIGIT+;
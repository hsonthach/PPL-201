grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options {
	language = Python3;
}

fragment DIGIT: [0-9];
fragment EXPONENT: [eE] '-'? DIGIT+;

//-------------------Grammar---------------------------------

program: ( global_decl | func_decl) | EOF;
// Var : a[5],b,c=3 ;
global_decl: VAR COLON varlist SEMI;
varlist: var (COMMA varlist)*;
var: ID (LSB INTEGER_LITERAL RSB)? | ID ASSIGN operands;
para_decl: VAR COLON paralist SEMI;
paralist: para (COMMA paralist)*;
para: ID (LSB INTEGER_LITERAL RSB)?;
idsList: ID (COMMA ID)*;
func_decl:
	FUNCTION COLON ID PARAMETER COLON idsList? BODY COLON blockstmt? ENDBODY DOT;

stmt:
	| blockstmt
	| if_stmt
	| while_stmt
	| for_stmt
	| do_stmt
	| break_stmt
	| continue_stmt
	| return_stmt
	| call_stmt
	| exp_stmt
	| assign_stmt;

blockstmt: LP (para_decl | stmt) RP;

if_stmt:
	IF exp0 THEN stmt (ELSEIF exp0 THEN stmt)? (
		ELSE exp0 THEN stmt ENDIF DOT
	)?;

for_stmt:
	FOR ID ASSIGN exp0 SEMI exp0 SEMI exp0 DO stmt ENDFOR DOT;

while_stmt: WHILE exp0 DO stmt ENDWHILE DOT;

do_stmt: DO stmt WHILE exp0 ENDDO DOT;

break_stmt: BREAK SEMI;

assign_stmt: ID EQ exp0 SEMI;

continue_stmt: CONTINUE SEMI;

call_stmt: ID LP arglist RP;

return_stmt: RETURN (exp0)? SEMI;

arglist: (exp0 (COMMA exp0)*)?;

exp_stmt: exp0 SEMI;

exp0: exp1 ASSIGN exp0 | exp1;
exp1: exp1 OR exp2 | exp2;
exp2: exp2 AND exp3 | exp3;
exp3: exp4 (EQ | NEQ) exp4 | exp4;
exp4: exp5 (LT | LTE | GT | GTE) exp5 | exp5;
exp5: exp5 (ADD | SUB) exp6 | exp6;
exp6: exp6 (MUL | DIV | MOD) exp7 | exp7;
exp7: (NOT | SUB) exp7 | exp8;
exp8: exp9 LSB exp0 RSB | exp9;
exp9: LP exp0 RP | operands;

operands:
	INTEGER_LITERAL
	| BOOLEAN_LITERAL
	| ID
	| FLOAT_LITERAL
	| STRING_LITERAL
	| call_stmt
	| array;

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
	'"' STR_CHAR* '"' {
		y = str(self.text)
		self.text = y[1:-1]
	};

array: LCB ( exp0 ( COMMA exp0)*)? RCB;

// ----------------------------------------------------------------------------------------

//Comment
CMTLINE: '*' ~[\n\r\f]* -> skip;
CMTBLOCK: '*' '*' .*? '*' '*' -> skip;

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';
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
FDIV: '/.';

FLTE: '<=.';
FGTE: '>=.';
FNEQ: '=/=';
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
DOT: '.';
SEMI: ';';
COMMA: ',';
COLON: ':';
number: SUB? INTEGER_LITERAL;

// Methods
FUNCTION: 'Function';

// Scope
BEGIN: 'Begin';
BODY: 'Body';
END: 'End';
PARAMETER: 'Parameter';

// Value
TRUE: 'True';
FALSE: 'False';

// Flow Statement
IF: 'If';
THEN: 'Then';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDIF: 'Endif';
ENDDO: 'EndDo';
ENDBODY: 'EndBody';

// Loop Statement
FOR: 'For';
WHILE: 'While';
DO: 'Do';
TO: 'To';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';

// Stop Statement
RETURN: 'return';
BREAK: 'break';
CONTINUE: 'continue';

// Primitive Types
primitive_types: INTEGER | FLOAT | STRING | BOOLEAN;
INTEGER: 'int';
STRING: 'string';
FLOAT: 'float';
BOOLEAN: 'boolean';
VAR: 'Var';
OF: 'of';

// Compound Types
ARRAY: 'array';
array_lhs: ID LSB number RSB;
array_rhs: LCB operands? (COMMA operands)* RCB;
ID: [_a-zA-Z][_a-zA-Z0-9]*;

UNCLOSE_STRING:
	'"' STR_CHAR* ([\b\t\n\f\r"'\\] | EOF) {
		y = str(self.text)
		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
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
fragment STR_CHAR: ~[\b\t\n\f\r"'\\] | ESC_SEQ;

fragment ESC_SEQ: '\\' [btnfr"'\\];
fragment ESC_ILLEGAL: '\\' ~[btnfr"'\\] | ~'\\';
ERROR_CHAR:
	. {
		raise ErrorToken(self.text)
	};
UNTERMINATED_COMMENT: .;
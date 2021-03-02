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

program: ( var_declaration | func_declaration)+;

var_declaration: var_type id_list SM;
var_type: INT | FLOAT;
id_list: ID CM id_list | ID;

func_declaration: var_type ID param_declaration body;

param_declaration: LP list_of_params RP;
list_of_params: list_of_non_null_params |;
list_of_non_null_params:
	param SM list_of_non_null_params
	| param;
param: var_type id_list;

body: LB (var_declaration | stament)* RB;
stament: (assignment_stament | call_stament | return_stament) SM;

assignment_stament: ID EQ expression;
expression: exp1 ADD expression | exp1;
exp1: exp2 SUB exp2 | exp2;
exp2: exp2 DIV exp3 | exp2 MUL exp3 | exp3;
exp3: operands;
operands:
	INTLIT
	| FLOATLIT
	| ID
	| call_stament
	| sub_expression;
sub_expression: LP expression RP;

call_stament: ID LP expression_list RP;
expression_list: non_null_expression_list?;
non_null_expression_list:
	expression CM non_null_expression_list
	| expression;

return_stament: RETURN expression;

/** Lexer */

// Keywords
RETURN: 'return';
FLOAT: 'float';
INT: 'int';

// Specific characters
LB: '{';
RB: '}';
LP: '(';
RP: ')';

SM: ';';
CM: ',';

EQ: '=';

ADD: '+';
SUB: '-';
MUL: '*';
DIV: '/';

FLOATLIT: INTLIT ([.][0-9]+)? ([eE][+-]? [0-9]+)?;

INTLIT: [1-9] [0-9]* | '0';

ID: [_a-zA-Z] [_a-zA-Z0-9]*;

WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;
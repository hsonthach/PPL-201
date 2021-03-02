grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
   	return result;
}

options {
	language = Python3;
}

/** Parser Declaration */
program: EOF;

WS: [ \t\n\r] -> skip;
// a1122 a*2 sad?33
STRING_LITERAL: [a-zA-Z] (~[ 0-9] | DOUBLE_NUM)*;
fragment DOUBLE_NUM:
	[0][0]
	| [1][1]
	| [2][2]
	| [3][3]
	| [4][4]
	| [5][5]
	| [6][6]
	| [7][7]
	| [8][8];

// \ with btnrf or no \
fragment STR_CHAR: ~([\b\t\n\f\r"'\\]) | ESC_SEQ;

fragment ESC_SEQ: ('\\' [btnfr'\\]) | ('\'"');

ERROR_CHAR:
	. {
	raise UnterminatedComment()
};

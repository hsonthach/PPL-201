// 1813854
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

options{
	language=Python3;
}

program  : VAR COLON ID SEMI EOF ;


SEMI: ';' ;

COLON: ':' ;

VAR: 'Var' ;

WS : [ \t\r\n]+ -> skip ; // skip spaces, tabs, newlines
// Start of Tutorial 1

fragment LOWERCASE_LETTER: [a-z];
fragment DIGIT: [0-9];
fragment SIGN: [+-]?;
fragment SCIENTIFIC: [e](SIGN)(DIGIT)+;
fragment DECIMAL_POINT: [.](DIGIT)+;

REAL: SIGN(DIGIT)+(DECIMAL_POINT(SCIENTIFIC)? | SCIENTIFIC);
ID: LOWERCASE_LETTER (LOWERCASE_LETTER | DIGIT)*;
STRING : ['] ((~[']) | (['][']))* ['];

//ID: [a-z]+;

ERROR_CHAR: .;
UNCLOSE_STRING: .;
ILLEGAL_ESCAPE: .;
UNTERMINATED_COMMENT: .;

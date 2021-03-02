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
program: vardecls EOF;

vardecls: vardecl vardecltail;

vardecltail: vardecl vardecltail |;

vardecl: mptype ids ';';

mptype: INTTYPE | FLOATTYPE;

ids: ID ',' ids | ID;

INTTYPE: 'int';

FLOATTYPE: 'float';

ID: [a-z]+;
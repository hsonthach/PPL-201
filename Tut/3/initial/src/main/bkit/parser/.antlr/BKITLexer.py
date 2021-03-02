# Generated from c:\Users\ASUS\Desktop\201\PPL\Tut\3\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\30")
        buf.write("\u008a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\20\6\20Z\n\20\r\20\16\20[\5\20^\n\20\3\20\3\20\5")
        buf.write("\20b\n\20\3\20\6\20e\n\20\r\20\16\20f\5\20i\n\20\3\21")
        buf.write("\3\21\7\21m\n\21\f\21\16\21p\13\21\3\21\5\21s\n\21\3\22")
        buf.write("\3\22\7\22w\n\22\f\22\16\22z\13\22\3\23\6\23}\n\23\r\23")
        buf.write("\16\23~\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\27\3")
        buf.write("\27\2\2\30\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30\3\2\n\3\2\60\60\3\2\62;\4\2GGgg\4\2--//\3\2\63")
        buf.write(";\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\17\17\"\"\2\u0092")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\3/\3\2\2\2\5\66\3\2\2\2\7<\3\2\2\2\t@\3\2\2\2\13B\3\2")
        buf.write("\2\2\rD\3\2\2\2\17F\3\2\2\2\21H\3\2\2\2\23J\3\2\2\2\25")
        buf.write("L\3\2\2\2\27N\3\2\2\2\31P\3\2\2\2\33R\3\2\2\2\35T\3\2")
        buf.write("\2\2\37V\3\2\2\2!r\3\2\2\2#t\3\2\2\2%|\3\2\2\2\'\u0082")
        buf.write("\3\2\2\2)\u0084\3\2\2\2+\u0086\3\2\2\2-\u0088\3\2\2\2")
        buf.write("/\60\7t\2\2\60\61\7g\2\2\61\62\7v\2\2\62\63\7w\2\2\63")
        buf.write("\64\7t\2\2\64\65\7p\2\2\65\4\3\2\2\2\66\67\7h\2\2\678")
        buf.write("\7n\2\289\7q\2\29:\7c\2\2:;\7v\2\2;\6\3\2\2\2<=\7k\2\2")
        buf.write("=>\7p\2\2>?\7v\2\2?\b\3\2\2\2@A\7}\2\2A\n\3\2\2\2BC\7")
        buf.write("\177\2\2C\f\3\2\2\2DE\7*\2\2E\16\3\2\2\2FG\7+\2\2G\20")
        buf.write("\3\2\2\2HI\7=\2\2I\22\3\2\2\2JK\7.\2\2K\24\3\2\2\2LM\7")
        buf.write("?\2\2M\26\3\2\2\2NO\7-\2\2O\30\3\2\2\2PQ\7/\2\2Q\32\3")
        buf.write("\2\2\2RS\7,\2\2S\34\3\2\2\2TU\7\61\2\2U\36\3\2\2\2V]\5")
        buf.write("!\21\2WY\t\2\2\2XZ\t\3\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2")
        buf.write("\2[\\\3\2\2\2\\^\3\2\2\2]W\3\2\2\2]^\3\2\2\2^h\3\2\2\2")
        buf.write("_a\t\4\2\2`b\t\5\2\2a`\3\2\2\2ab\3\2\2\2bd\3\2\2\2ce\t")
        buf.write("\3\2\2dc\3\2\2\2ef\3\2\2\2fd\3\2\2\2fg\3\2\2\2gi\3\2\2")
        buf.write("\2h_\3\2\2\2hi\3\2\2\2i \3\2\2\2jn\t\6\2\2km\t\3\2\2l")
        buf.write("k\3\2\2\2mp\3\2\2\2nl\3\2\2\2no\3\2\2\2os\3\2\2\2pn\3")
        buf.write("\2\2\2qs\7\62\2\2rj\3\2\2\2rq\3\2\2\2s\"\3\2\2\2tx\t\7")
        buf.write("\2\2uw\t\b\2\2vu\3\2\2\2wz\3\2\2\2xv\3\2\2\2xy\3\2\2\2")
        buf.write("y$\3\2\2\2zx\3\2\2\2{}\t\t\2\2|{\3\2\2\2}~\3\2\2\2~|\3")
        buf.write("\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081\b\23")
        buf.write("\2\2\u0081&\3\2\2\2\u0082\u0083\13\2\2\2\u0083(\3\2\2")
        buf.write("\2\u0084\u0085\13\2\2\2\u0085*\3\2\2\2\u0086\u0087\13")
        buf.write("\2\2\2\u0087,\3\2\2\2\u0088\u0089\13\2\2\2\u0089.\3\2")
        buf.write("\2\2\f\2[]afhnrx~\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    RETURN = 1
    FLOAT = 2
    INT = 3
    LB = 4
    RB = 5
    LP = 6
    RP = 7
    SM = 8
    CM = 9
    EQ = 10
    ADD = 11
    SUB = 12
    MUL = 13
    DIV = 14
    FLOATLIT = 15
    INTLIT = 16
    ID = 17
    WS = 18
    ERROR_CHAR = 19
    UNCLOSE_STRING = 20
    ILLEGAL_ESCAPE = 21
    UNTERMINATED_COMMENT = 22

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'return'", "'float'", "'int'", "'{'", "'}'", "'('", "')'", 
            "';'", "','", "'='", "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>",
            "RETURN", "FLOAT", "INT", "LB", "RB", "LP", "RP", "SM", "CM", 
            "EQ", "ADD", "SUB", "MUL", "DIV", "FLOATLIT", "INTLIT", "ID", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "RETURN", "FLOAT", "INT", "LB", "RB", "LP", "RP", "SM", 
                  "CM", "EQ", "ADD", "SUB", "MUL", "DIV", "FLOATLIT", "INTLIT", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


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



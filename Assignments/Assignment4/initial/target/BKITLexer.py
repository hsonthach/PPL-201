# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("\\\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\7\4")
        buf.write("(\n\4\f\4\16\4+\13\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\13\6\13J\n\13\r\13\16\13K\3")
        buf.write("\f\6\fO\n\f\r\f\16\fP\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3")
        buf.write("\17\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2\6\3\2c")
        buf.write("|\6\2\62;C\\aac|\3\2\62;\5\2\13\f\17\17\"\"\2^\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2")
        buf.write("\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2")
        buf.write("\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35")
        buf.write("\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2")
        buf.write("\t,\3\2\2\2\13.\3\2\2\2\r\60\3\2\2\2\17\62\3\2\2\2\21")
        buf.write(";\3\2\2\2\23@\3\2\2\2\25I\3\2\2\2\27N\3\2\2\2\31T\3\2")
        buf.write("\2\2\33V\3\2\2\2\35X\3\2\2\2\37Z\3\2\2\2!\"\7*\2\2\"\4")
        buf.write("\3\2\2\2#$\7+\2\2$\6\3\2\2\2%)\t\2\2\2&(\t\3\2\2\'&\3")
        buf.write("\2\2\2(+\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\b\3\2\2\2+)\3\2")
        buf.write("\2\2,-\7=\2\2-\n\3\2\2\2./\7<\2\2/\f\3\2\2\2\60\61\7\60")
        buf.write("\2\2\61\16\3\2\2\2\62\63\7H\2\2\63\64\7w\2\2\64\65\7p")
        buf.write("\2\2\65\66\7e\2\2\66\67\7v\2\2\678\7k\2\289\7q\2\29:\7")
        buf.write("p\2\2:\20\3\2\2\2;<\7D\2\2<=\7q\2\2=>\7f\2\2>?\7{\2\2")
        buf.write("?\22\3\2\2\2@A\7G\2\2AB\7p\2\2BC\7f\2\2CD\7D\2\2DE\7q")
        buf.write("\2\2EF\7f\2\2FG\7{\2\2G\24\3\2\2\2HJ\t\4\2\2IH\3\2\2\2")
        buf.write("JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2L\26\3\2\2\2MO\t\5\2\2N")
        buf.write("M\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\b")
        buf.write("\f\2\2S\30\3\2\2\2TU\13\2\2\2U\32\3\2\2\2VW\13\2\2\2W")
        buf.write("\34\3\2\2\2XY\13\2\2\2Y\36\3\2\2\2Z[\13\2\2\2[ \3\2\2")
        buf.write("\2\6\2)KP\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    ID = 3
    SEMI = 4
    COLON = 5
    DOT = 6
    FUNCTION = 7
    BODY = 8
    ENDBODY = 9
    INTLIT = 10
    WS = 11
    ERROR_CHAR = 12
    UNCLOSE_STRING = 13
    ILLEGAL_ESCAPE = 14
    UNTERMINATED_COMMENT = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "';'", "':'", "'.'", "'Function'", "'Body'", "'EndBody'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "SEMI", "COLON", "DOT", "FUNCTION", "BODY", "ENDBODY", 
            "INTLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "ID", "SEMI", "COLON", "DOT", "FUNCTION", 
                  "BODY", "ENDBODY", "INTLIT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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



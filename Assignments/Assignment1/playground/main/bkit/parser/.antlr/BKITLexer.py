# Generated from c:\Users\ASUS\Desktop\201\PPL\Assignments\Assignment1\playground\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write("<\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\3\2\3\2\3\2\3\2\3\3\3\3\3\3\7\3\27\n\3\f\3\16\3\32\13")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\5\4.\n\4\3\5\3\5\5\5\62\n\5\3\6\3")
        buf.write("\6\3\6\3\6\5\68\n\6\3\7\3\7\3\7\2\2\b\3\3\5\4\7\2\t\2")
        buf.write("\13\2\r\5\3\2\20\5\2\13\f\17\17\"\"\4\2C\\c|\4\2\"\"\62")
        buf.write(";\3\2\62\62\3\2\63\63\3\2\64\64\3\2\65\65\3\2\66\66\3")
        buf.write("\2\67\67\3\288\3\299\3\2::\7\2\n\f\16\17$$))^^\t\2))^")
        buf.write("^ddhhppttvv\2D\2\3\3\2\2\2\2\5\3\2\2\2\2\r\3\2\2\2\3\17")
        buf.write("\3\2\2\2\5\23\3\2\2\2\7-\3\2\2\2\t\61\3\2\2\2\13\67\3")
        buf.write("\2\2\2\r9\3\2\2\2\17\20\t\2\2\2\20\21\3\2\2\2\21\22\b")
        buf.write("\2\2\2\22\4\3\2\2\2\23\30\t\3\2\2\24\27\n\4\2\2\25\27")
        buf.write("\5\7\4\2\26\24\3\2\2\2\26\25\3\2\2\2\27\32\3\2\2\2\30")
        buf.write("\26\3\2\2\2\30\31\3\2\2\2\31\6\3\2\2\2\32\30\3\2\2\2\33")
        buf.write("\34\t\5\2\2\34.\t\5\2\2\35\36\t\6\2\2\36.\t\6\2\2\37 ")
        buf.write("\t\7\2\2 .\t\7\2\2!\"\t\b\2\2\".\t\b\2\2#$\t\t\2\2$.\t")
        buf.write("\t\2\2%&\t\n\2\2&.\t\n\2\2\'(\t\13\2\2(.\t\13\2\2)*\t")
        buf.write("\f\2\2*.\t\f\2\2+,\t\r\2\2,.\t\r\2\2-\33\3\2\2\2-\35\3")
        buf.write("\2\2\2-\37\3\2\2\2-!\3\2\2\2-#\3\2\2\2-%\3\2\2\2-\'\3")
        buf.write("\2\2\2-)\3\2\2\2-+\3\2\2\2.\b\3\2\2\2/\62\n\16\2\2\60")
        buf.write("\62\5\13\6\2\61/\3\2\2\2\61\60\3\2\2\2\62\n\3\2\2\2\63")
        buf.write("\64\7^\2\2\648\t\17\2\2\65\66\7)\2\2\668\7$\2\2\67\63")
        buf.write("\3\2\2\2\67\65\3\2\2\28\f\3\2\2\29:\13\2\2\2:;\b\7\3\2")
        buf.write(";\16\3\2\2\2\b\2\26\30-\61\67\4\b\2\2\3\7\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WS = 1
    STRING_LITERAL = 2
    ERROR_CHAR = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WS", "STRING_LITERAL", "ERROR_CHAR" ]

    ruleNames = [ "WS", "STRING_LITERAL", "DOUBLE_NUM", "STR_CHAR", "ESC_SEQ", 
                  "ERROR_CHAR" ]

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
       	return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            	raise UnterminatedComment()

     



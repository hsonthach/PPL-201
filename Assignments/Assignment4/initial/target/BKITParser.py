# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write("\32\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\3\2\2")
        buf.write("\4\2\4\2\2\2\30\2\6\3\2\2\2\4\27\3\2\2\2\6\7\7\t\2\2\7")
        buf.write("\b\7\7\2\2\b\t\7\5\2\2\t\n\7\n\2\2\n\13\7\7\2\2\13\f\5")
        buf.write("\4\3\2\f\r\7\6\2\2\r\16\7\13\2\2\16\17\7\b\2\2\17\20\7")
        buf.write("\2\2\3\20\3\3\2\2\2\21\22\7\5\2\2\22\23\7\3\2\2\23\24")
        buf.write("\5\4\3\2\24\25\7\4\2\2\25\30\3\2\2\2\26\30\7\f\2\2\27")
        buf.write("\21\3\2\2\2\27\26\3\2\2\2\30\5\3\2\2\2\3\27")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "<INVALID>", "';'", "':'", 
                     "'.'", "'Function'", "'Body'", "'EndBody'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "ID", "SEMI", 
                      "COLON", "DOT", "FUNCTION", "BODY", "ENDBODY", "INTLIT", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_exp = 1

    ruleNames =  [ "program", "exp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    ID=3
    SEMI=4
    COLON=5
    DOT=6
    FUNCTION=7
    BODY=8
    ENDBODY=9
    INTLIT=10
    WS=11
    ERROR_CHAR=12
    UNCLOSE_STRING=13
    ILLEGAL_ESCAPE=14
    UNTERMINATED_COMMENT=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(BKITParser.FUNCTION, 0)

        def COLON(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COLON)
            else:
                return self.getToken(BKITParser.COLON, i)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def BODY(self):
            return self.getToken(BKITParser.BODY, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(BKITParser.FUNCTION)
            self.state = 5
            self.match(BKITParser.COLON)
            self.state = 6
            self.match(BKITParser.ID)
            self.state = 7
            self.match(BKITParser.BODY)
            self.state = 8
            self.match(BKITParser.COLON)
            self.state = 9
            self.exp()
            self.state = 10
            self.match(BKITParser.SEMI)
            self.state = 11
            self.match(BKITParser.ENDBODY)
            self.state = 12
            self.match(BKITParser.DOT)
            self.state = 13
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def exp(self):
            return self.getTypedRuleContext(BKITParser.ExpContext,0)


        def INTLIT(self):
            return self.getToken(BKITParser.INTLIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = BKITParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.match(BKITParser.ID)
                self.state = 16
                self.match(BKITParser.T__0)
                self.state = 17
                self.exp()
                self.state = 18
                self.match(BKITParser.T__1)
                pass
            elif token in [BKITParser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.match(BKITParser.INTLIT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






# Generated from c:\Users\ASUS\Desktop\201\PPL\Assignments\Assignment1\assignment1\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3L")
        buf.write("\u017a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\3\2\7")
        buf.write("\2L\n\2\f\2\16\2O\13\2\3\2\7\2R\n\2\f\2\16\2U\13\2\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\7\4a\n\4\f\4\16\4")
        buf.write("d\13\4\3\5\3\5\3\5\3\5\7\5j\n\5\f\5\16\5m\13\5\3\5\3\5")
        buf.write("\5\5q\n\5\3\6\3\6\3\6\7\6v\n\6\f\6\16\6y\13\6\3\7\3\7")
        buf.write("\3\7\3\7\7\7\177\n\7\f\7\16\7\u0082\13\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\b\u008a\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\t\7")
        buf.write("\t\u0093\n\t\f\t\16\t\u0096\13\t\3\t\7\t\u0099\n\t\f\t")
        buf.write("\16\t\u009c\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5")
        buf.write("\n\u00a7\n\n\3\13\3\13\3\13\3\13\3\13\7\13\u00ae\n\13")
        buf.write("\f\13\16\13\u00b1\13\13\3\13\5\13\u00b4\n\13\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\7\21\u00e3")
        buf.write("\n\21\f\21\16\21\u00e6\13\21\5\21\u00e8\n\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\5\24\u00f5")
        buf.write("\n\24\3\24\3\24\3\25\3\25\3\25\7\25\u00fc\n\25\f\25\16")
        buf.write("\25\u00ff\13\25\5\25\u0101\n\25\3\26\3\26\3\26\3\26\3")
        buf.write("\26\7\26\u0108\n\26\f\26\16\26\u010b\13\26\5\26\u010d")
        buf.write("\n\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\30\3\30\5\30")
        buf.write("\u0118\n\30\3\31\3\31\3\31\3\31\3\31\5\31\u011f\n\31\3")
        buf.write("\32\3\32\3\32\3\32\3\32\3\32\7\32\u0127\n\32\f\32\16\32")
        buf.write("\u012a\13\32\3\33\3\33\3\33\3\33\3\33\3\33\7\33\u0132")
        buf.write("\n\33\f\33\16\33\u0135\13\33\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\7\34\u013d\n\34\f\34\16\34\u0140\13\34\3\35\3\35")
        buf.write("\3\35\5\35\u0145\n\35\3\36\3\36\3\36\5\36\u014a\n\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\7\37\u0151\n\37\f\37\16\37\u0154")
        buf.write("\13\37\3 \3 \3!\3!\3!\3!\3!\5!\u015d\n!\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\5\"\u0166\n\"\3#\3#\3#\3#\7#\u016c\n#\f")
        buf.write("#\16#\u016f\13#\3#\3#\3$\5$\u0174\n$\3$\3$\3%\3%\3%\2")
        buf.write("\5\62\64\66&\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFH\2\b\4\2\21\26\33 \3\2\16\17")
        buf.write("\4\2\b\t\27\30\4\2\n\f\31\32\4\2\t\t\30\30\3\2AD\2\u0181")
        buf.write("\2M\3\2\2\2\4X\3\2\2\2\6]\3\2\2\2\be\3\2\2\2\nr\3\2\2")
        buf.write("\2\fz\3\2\2\2\16\u0083\3\2\2\2\20\u0094\3\2\2\2\22\u00a6")
        buf.write("\3\2\2\2\24\u00a8\3\2\2\2\26\u00b8\3\2\2\2\30\u00bd\3")
        buf.write("\2\2\2\32\u00c0\3\2\2\2\34\u00c7\3\2\2\2\36\u00ce\3\2")
        buf.write("\2\2 \u00dd\3\2\2\2\"\u00ec\3\2\2\2$\u00ef\3\2\2\2&\u00f2")
        buf.write("\3\2\2\2(\u0100\3\2\2\2*\u0102\3\2\2\2,\u0110\3\2\2\2")
        buf.write(".\u0117\3\2\2\2\60\u011e\3\2\2\2\62\u0120\3\2\2\2\64\u012b")
        buf.write("\3\2\2\2\66\u0136\3\2\2\28\u0144\3\2\2\2:\u0149\3\2\2")
        buf.write("\2<\u014b\3\2\2\2>\u0155\3\2\2\2@\u015c\3\2\2\2B\u0165")
        buf.write("\3\2\2\2D\u0167\3\2\2\2F\u0173\3\2\2\2H\u0177\3\2\2\2")
        buf.write("JL\5\4\3\2KJ\3\2\2\2LO\3\2\2\2MK\3\2\2\2MN\3\2\2\2NS\3")
        buf.write("\2\2\2OM\3\2\2\2PR\5\16\b\2QP\3\2\2\2RU\3\2\2\2SQ\3\2")
        buf.write("\2\2ST\3\2\2\2TV\3\2\2\2US\3\2\2\2VW\7\2\2\3W\3\3\2\2")
        buf.write("\2XY\7E\2\2YZ\7*\2\2Z[\5\6\4\2[\\\7(\2\2\\\5\3\2\2\2]")
        buf.write("b\5\b\5\2^_\7)\2\2_a\5\b\5\2`^\3\2\2\2ad\3\2\2\2b`\3\2")
        buf.write("\2\2bc\3\2\2\2c\7\3\2\2\2db\3\2\2\2ek\7H\2\2fg\7&\2\2")
        buf.write("gh\7\3\2\2hj\7\'\2\2if\3\2\2\2jm\3\2\2\2ki\3\2\2\2kl\3")
        buf.write("\2\2\2lp\3\2\2\2mk\3\2\2\2no\7\20\2\2oq\5@!\2pn\3\2\2")
        buf.write("\2pq\3\2\2\2q\t\3\2\2\2rw\5\f\7\2st\7)\2\2tv\5\f\7\2u")
        buf.write("s\3\2\2\2vy\3\2\2\2wu\3\2\2\2wx\3\2\2\2x\13\3\2\2\2yw")
        buf.write("\3\2\2\2z\u0080\7H\2\2{|\7&\2\2|}\7\3\2\2}\177\7\'\2\2")
        buf.write("~{\3\2\2\2\177\u0082\3\2\2\2\u0080~\3\2\2\2\u0080\u0081")
        buf.write("\3\2\2\2\u0081\r\3\2\2\2\u0082\u0080\3\2\2\2\u0083\u0084")
        buf.write("\7+\2\2\u0084\u0085\7*\2\2\u0085\u0089\7H\2\2\u0086\u0087")
        buf.write("\7.\2\2\u0087\u0088\7*\2\2\u0088\u008a\5\n\6\2\u0089\u0086")
        buf.write("\3\2\2\2\u0089\u008a\3\2\2\2\u008a\u008b\3\2\2\2\u008b")
        buf.write("\u008c\7,\2\2\u008c\u008d\7*\2\2\u008d\u008e\5\20\t\2")
        buf.write("\u008e\u008f\7\67\2\2\u008f\u0090\7\7\2\2\u0090\17\3\2")
        buf.write("\2\2\u0091\u0093\5\4\3\2\u0092\u0091\3\2\2\2\u0093\u0096")
        buf.write("\3\2\2\2\u0094\u0092\3\2\2\2\u0094\u0095\3\2\2\2\u0095")
        buf.write("\u009a\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0099\5\22\n")
        buf.write("\2\u0098\u0097\3\2\2\2\u0099\u009c\3\2\2\2\u009a\u0098")
        buf.write("\3\2\2\2\u009a\u009b\3\2\2\2\u009b\21\3\2\2\2\u009c\u009a")
        buf.write("\3\2\2\2\u009d\u00a7\5\24\13\2\u009e\u00a7\5,\27\2\u009f")
        buf.write("\u00a7\5\32\16\2\u00a0\u00a7\5\36\20\2\u00a1\u00a7\5\"")
        buf.write("\22\2\u00a2\u00a7\5$\23\2\u00a3\u00a7\5&\24\2\u00a4\u00a7")
        buf.write("\5 \21\2\u00a5\u00a7\5\34\17\2\u00a6\u009d\3\2\2\2\u00a6")
        buf.write("\u009e\3\2\2\2\u00a6\u009f\3\2\2\2\u00a6\u00a0\3\2\2\2")
        buf.write("\u00a6\u00a1\3\2\2\2\u00a6\u00a2\3\2\2\2\u00a6\u00a3\3")
        buf.write("\2\2\2\u00a6\u00a4\3\2\2\2\u00a6\u00a5\3\2\2\2\u00a7\23")
        buf.write("\3\2\2\2\u00a8\u00a9\7\61\2\2\u00a9\u00aa\5\60\31\2\u00aa")
        buf.write("\u00ab\7\62\2\2\u00ab\u00af\5\20\t\2\u00ac\u00ae\5\26")
        buf.write("\f\2\u00ad\u00ac\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad")
        buf.write("\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00b3\3\2\2\2\u00b1")
        buf.write("\u00af\3\2\2\2\u00b2\u00b4\5\30\r\2\u00b3\u00b2\3\2\2")
        buf.write("\2\u00b3\u00b4\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6")
        buf.write("\7\65\2\2\u00b6\u00b7\7\7\2\2\u00b7\25\3\2\2\2\u00b8\u00b9")
        buf.write("\7\64\2\2\u00b9\u00ba\5\60\31\2\u00ba\u00bb\7\62\2\2\u00bb")
        buf.write("\u00bc\5\20\t\2\u00bc\27\3\2\2\2\u00bd\u00be\7\63\2\2")
        buf.write("\u00be\u00bf\5\20\t\2\u00bf\31\3\2\2\2\u00c0\u00c1\79")
        buf.write("\2\2\u00c1\u00c2\5\60\31\2\u00c2\u00c3\7:\2\2\u00c3\u00c4")
        buf.write("\5\20\t\2\u00c4\u00c5\7=\2\2\u00c5\u00c6\7\7\2\2\u00c6")
        buf.write("\33\3\2\2\2\u00c7\u00c8\7:\2\2\u00c8\u00c9\5\20\t\2\u00c9")
        buf.write("\u00ca\79\2\2\u00ca\u00cb\5\60\31\2\u00cb\u00cc\7\66\2")
        buf.write("\2\u00cc\u00cd\7\7\2\2\u00cd\35\3\2\2\2\u00ce\u00cf\7")
        buf.write("8\2\2\u00cf\u00d0\7\"\2\2\u00d0\u00d1\7H\2\2\u00d1\u00d2")
        buf.write("\7\20\2\2\u00d2\u00d3\5\60\31\2\u00d3\u00d4\7)\2\2\u00d4")
        buf.write("\u00d5\5\60\31\2\u00d5\u00d6\7)\2\2\u00d6\u00d7\5\60\31")
        buf.write("\2\u00d7\u00d8\7#\2\2\u00d8\u00d9\7:\2\2\u00d9\u00da\5")
        buf.write("\20\t\2\u00da\u00db\7<\2\2\u00db\u00dc\7\7\2\2\u00dc\37")
        buf.write("\3\2\2\2\u00dd\u00de\7H\2\2\u00de\u00e7\7\"\2\2\u00df")
        buf.write("\u00e4\5\60\31\2\u00e0\u00e1\7)\2\2\u00e1\u00e3\5\60\31")
        buf.write("\2\u00e2\u00e0\3\2\2\2\u00e3\u00e6\3\2\2\2\u00e4\u00e2")
        buf.write("\3\2\2\2\u00e4\u00e5\3\2\2\2\u00e5\u00e8\3\2\2\2\u00e6")
        buf.write("\u00e4\3\2\2\2\u00e7\u00df\3\2\2\2\u00e7\u00e8\3\2\2\2")
        buf.write("\u00e8\u00e9\3\2\2\2\u00e9\u00ea\7#\2\2\u00ea\u00eb\7")
        buf.write("(\2\2\u00eb!\3\2\2\2\u00ec\u00ed\7?\2\2\u00ed\u00ee\7")
        buf.write("(\2\2\u00ee#\3\2\2\2\u00ef\u00f0\7@\2\2\u00f0\u00f1\7")
        buf.write("(\2\2\u00f1%\3\2\2\2\u00f2\u00f4\7>\2\2\u00f3\u00f5\5")
        buf.write("\60\31\2\u00f4\u00f3\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5")
        buf.write("\u00f6\3\2\2\2\u00f6\u00f7\7(\2\2\u00f7\'\3\2\2\2\u00f8")
        buf.write("\u00fd\5\60\31\2\u00f9\u00fa\7)\2\2\u00fa\u00fc\5\60\31")
        buf.write("\2\u00fb\u00f9\3\2\2\2\u00fc\u00ff\3\2\2\2\u00fd\u00fb")
        buf.write("\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff")
        buf.write("\u00fd\3\2\2\2\u0100\u00f8\3\2\2\2\u0100\u0101\3\2\2\2")
        buf.write("\u0101)\3\2\2\2\u0102\u0103\7H\2\2\u0103\u010c\7\"\2\2")
        buf.write("\u0104\u0109\5\60\31\2\u0105\u0106\7)\2\2\u0106\u0108")
        buf.write("\5\60\31\2\u0107\u0105\3\2\2\2\u0108\u010b\3\2\2\2\u0109")
        buf.write("\u0107\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010d\3\2\2\2")
        buf.write("\u010b\u0109\3\2\2\2\u010c\u0104\3\2\2\2\u010c\u010d\3")
        buf.write("\2\2\2\u010d\u010e\3\2\2\2\u010e\u010f\7#\2\2\u010f+\3")
        buf.write("\2\2\2\u0110\u0111\5.\30\2\u0111\u0112\7\20\2\2\u0112")
        buf.write("\u0113\5\60\31\2\u0113\u0114\7(\2\2\u0114-\3\2\2\2\u0115")
        buf.write("\u0118\7H\2\2\u0116\u0118\5<\37\2\u0117\u0115\3\2\2\2")
        buf.write("\u0117\u0116\3\2\2\2\u0118/\3\2\2\2\u0119\u011a\5\62\32")
        buf.write("\2\u011a\u011b\t\2\2\2\u011b\u011c\5\62\32\2\u011c\u011f")
        buf.write("\3\2\2\2\u011d\u011f\5\62\32\2\u011e\u0119\3\2\2\2\u011e")
        buf.write("\u011d\3\2\2\2\u011f\61\3\2\2\2\u0120\u0121\b\32\1\2\u0121")
        buf.write("\u0122\5\64\33\2\u0122\u0128\3\2\2\2\u0123\u0124\f\4\2")
        buf.write("\2\u0124\u0125\t\3\2\2\u0125\u0127\5\64\33\2\u0126\u0123")
        buf.write("\3\2\2\2\u0127\u012a\3\2\2\2\u0128\u0126\3\2\2\2\u0128")
        buf.write("\u0129\3\2\2\2\u0129\63\3\2\2\2\u012a\u0128\3\2\2\2\u012b")
        buf.write("\u012c\b\33\1\2\u012c\u012d\5\66\34\2\u012d\u0133\3\2")
        buf.write("\2\2\u012e\u012f\f\4\2\2\u012f\u0130\t\4\2\2\u0130\u0132")
        buf.write("\5\66\34\2\u0131\u012e\3\2\2\2\u0132\u0135\3\2\2\2\u0133")
        buf.write("\u0131\3\2\2\2\u0133\u0134\3\2\2\2\u0134\65\3\2\2\2\u0135")
        buf.write("\u0133\3\2\2\2\u0136\u0137\b\34\1\2\u0137\u0138\58\35")
        buf.write("\2\u0138\u013e\3\2\2\2\u0139\u013a\f\4\2\2\u013a\u013b")
        buf.write("\t\5\2\2\u013b\u013d\58\35\2\u013c\u0139\3\2\2\2\u013d")
        buf.write("\u0140\3\2\2\2\u013e\u013c\3\2\2\2\u013e\u013f\3\2\2\2")
        buf.write("\u013f\67\3\2\2\2\u0140\u013e\3\2\2\2\u0141\u0142\7\r")
        buf.write("\2\2\u0142\u0145\58\35\2\u0143\u0145\5:\36\2\u0144\u0141")
        buf.write("\3\2\2\2\u0144\u0143\3\2\2\2\u01459\3\2\2\2\u0146\u0147")
        buf.write("\t\6\2\2\u0147\u014a\5:\36\2\u0148\u014a\5<\37\2\u0149")
        buf.write("\u0146\3\2\2\2\u0149\u0148\3\2\2\2\u014a;\3\2\2\2\u014b")
        buf.write("\u0152\5> \2\u014c\u014d\7&\2\2\u014d\u014e\5\60\31\2")
        buf.write("\u014e\u014f\7\'\2\2\u014f\u0151\3\2\2\2\u0150\u014c\3")
        buf.write("\2\2\2\u0151\u0154\3\2\2\2\u0152\u0150\3\2\2\2\u0152\u0153")
        buf.write("\3\2\2\2\u0153=\3\2\2\2\u0154\u0152\3\2\2\2\u0155\u0156")
        buf.write("\5B\"\2\u0156?\3\2\2\2\u0157\u015d\7\3\2\2\u0158\u015d")
        buf.write("\7\5\2\2\u0159\u015d\5D#\2\u015a\u015d\7\4\2\2\u015b\u015d")
        buf.write("\7\6\2\2\u015c\u0157\3\2\2\2\u015c\u0158\3\2\2\2\u015c")
        buf.write("\u0159\3\2\2\2\u015c\u015a\3\2\2\2\u015c\u015b\3\2\2\2")
        buf.write("\u015dA\3\2\2\2\u015e\u0166\5@!\2\u015f\u0166\7H\2\2\u0160")
        buf.write("\u0166\5*\26\2\u0161\u0162\7\"\2\2\u0162\u0163\5\60\31")
        buf.write("\2\u0163\u0164\7#\2\2\u0164\u0166\3\2\2\2\u0165\u015e")
        buf.write("\3\2\2\2\u0165\u015f\3\2\2\2\u0165\u0160\3\2\2\2\u0165")
        buf.write("\u0161\3\2\2\2\u0166C\3\2\2\2\u0167\u0168\7$\2\2\u0168")
        buf.write("\u016d\5@!\2\u0169\u016a\7)\2\2\u016a\u016c\5@!\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u016f\3\2\2\2\u016d\u016b\3\2\2\2")
        buf.write("\u016d\u016e\3\2\2\2\u016e\u0170\3\2\2\2\u016f\u016d\3")
        buf.write("\2\2\2\u0170\u0171\7%\2\2\u0171E\3\2\2\2\u0172\u0174\7")
        buf.write("\t\2\2\u0173\u0172\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0175")
        buf.write("\3\2\2\2\u0175\u0176\7\3\2\2\u0176G\3\2\2\2\u0177\u0178")
        buf.write("\t\7\2\2\u0178I\3\2\2\2\"MSbkpw\u0080\u0089\u0094\u009a")
        buf.write("\u00a6\u00af\u00b3\u00e4\u00e7\u00f4\u00fd\u0100\u0109")
        buf.write("\u010c\u0117\u011e\u0128\u0133\u013e\u0144\u0149\u0152")
        buf.write("\u015c\u0165\u016d\u0173")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "'+'", "'-'", "'*'", "'\\'", "'%'", 
                     "'!'", "'&&'", "'||'", "'='", "'<='", "'>='", "'!='", 
                     "'=='", "'<'", "'>'", "'+.'", "'-.'", "'*.'", "'\\.'", 
                     "'<=.'", "'>=.'", "'=\\='", "'=.'", "'<.'", "'>.'", 
                     "<INVALID>", "'('", "')'", "'{'", "'}'", "'['", "']'", 
                     "';'", "','", "':'", "'Function'", "'Body'", "'End'", 
                     "'Parameter'", "'True'", "'False'", "'If'", "'Then'", 
                     "'Else'", "'ElseIf'", "'EndIf'", "'EndDo'", "'EndBody'", 
                     "'For'", "'While'", "'Do'", "'To'", "'EndFor'", "'EndWhile'", 
                     "'Return'", "'Break'", "'Continue'", "'int'", "'string'", 
                     "'float'", "'boolean'", "'Var'", "'of'" ]

    symbolicNames = [ "<INVALID>", "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", 
                      "STRING_LITERAL", "DOT", "ADD", "SUB", "MUL", "DIV", 
                      "MOD", "NOT", "AND", "OR", "ASSIGN", "LTE", "GTE", 
                      "NEQ", "EQ", "LT", "GT", "FADD", "FSUB", "FMUL", "FDIV", 
                      "FLTE", "FGTE", "FNEQ", "FEQ", "FLT", "FGT", "WS", 
                      "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                      "COLON", "FUNCTION", "BODY", "END", "PARAMETER", "TRUE", 
                      "FALSE", "IF", "THEN", "ELSE", "ELSEIF", "ENDIF", 
                      "ENDDO", "ENDBODY", "FOR", "WHILE", "DO", "TO", "ENDFOR", 
                      "ENDWHILE", "RETURN", "BREAK", "CONTINUE", "INTEGER", 
                      "STRING", "FLOAT", "BOOLEAN", "VAR", "OF", "COMMENT_LITERAL", 
                      "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT", 
                      "ERROR_CHAR" ]

    RULE_program = 0
    RULE_global_vardecl = 1
    RULE_vardecl_list = 2
    RULE_var_decl = 3
    RULE_para_decllist = 4
    RULE_para_decl = 5
    RULE_func_decl = 6
    RULE_stmtList = 7
    RULE_stmt = 8
    RULE_ifStmt = 9
    RULE_elifStmt = 10
    RULE_elseStmt = 11
    RULE_whileStmt = 12
    RULE_doWhileStmt = 13
    RULE_forStmt = 14
    RULE_callStmt = 15
    RULE_breakStmt = 16
    RULE_continueStmt = 17
    RULE_returnStmt = 18
    RULE_argulist = 19
    RULE_funcCall = 20
    RULE_assignStmt = 21
    RULE_lhs = 22
    RULE_exp1 = 23
    RULE_exp2 = 24
    RULE_exp3 = 25
    RULE_exp4 = 26
    RULE_exp5 = 27
    RULE_exp6 = 28
    RULE_index_exp = 29
    RULE_exp7 = 30
    RULE_literal = 31
    RULE_operands = 32
    RULE_array_literal = 33
    RULE_number = 34
    RULE_primitive_types = 35

    ruleNames =  [ "program", "global_vardecl", "vardecl_list", "var_decl", 
                   "para_decllist", "para_decl", "func_decl", "stmtList", 
                   "stmt", "ifStmt", "elifStmt", "elseStmt", "whileStmt", 
                   "doWhileStmt", "forStmt", "callStmt", "breakStmt", "continueStmt", 
                   "returnStmt", "argulist", "funcCall", "assignStmt", "lhs", 
                   "exp1", "exp2", "exp3", "exp4", "exp5", "exp6", "index_exp", 
                   "exp7", "literal", "operands", "array_literal", "number", 
                   "primitive_types" ]

    EOF = Token.EOF
    INTEGER_LITERAL=1
    FLOAT_LITERAL=2
    BOOLEAN_LITERAL=3
    STRING_LITERAL=4
    DOT=5
    ADD=6
    SUB=7
    MUL=8
    DIV=9
    MOD=10
    NOT=11
    AND=12
    OR=13
    ASSIGN=14
    LTE=15
    GTE=16
    NEQ=17
    EQ=18
    LT=19
    GT=20
    FADD=21
    FSUB=22
    FMUL=23
    FDIV=24
    FLTE=25
    FGTE=26
    FNEQ=27
    FEQ=28
    FLT=29
    FGT=30
    WS=31
    LP=32
    RP=33
    LCB=34
    RCB=35
    LSB=36
    RSB=37
    SEMI=38
    COMMA=39
    COLON=40
    FUNCTION=41
    BODY=42
    END=43
    PARAMETER=44
    TRUE=45
    FALSE=46
    IF=47
    THEN=48
    ELSE=49
    ELSEIF=50
    ENDIF=51
    ENDDO=52
    ENDBODY=53
    FOR=54
    WHILE=55
    DO=56
    TO=57
    ENDFOR=58
    ENDWHILE=59
    RETURN=60
    BREAK=61
    CONTINUE=62
    INTEGER=63
    STRING=64
    FLOAT=65
    BOOLEAN=66
    VAR=67
    OF=68
    COMMENT_LITERAL=69
    ID=70
    UNCLOSE_STRING=71
    ILLEGAL_ESCAPE=72
    UNTERMINATED_COMMENT=73
    ERROR_CHAR=74

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def global_vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Global_vardeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.Global_vardeclContext,i)


        def func_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Func_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Func_declContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 72
                self.global_vardecl()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.FUNCTION:
                self.state = 78
                self.func_decl()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_vardeclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def vardecl_list(self):
            return self.getTypedRuleContext(BKITParser.Vardecl_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_global_vardecl




    def global_vardecl(self):

        localctx = BKITParser.Global_vardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_global_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(BKITParser.VAR)
            self.state = 87
            self.match(BKITParser.COLON)
            self.state = 88
            self.vardecl_list()
            self.state = 89
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Vardecl_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Var_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Var_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_vardecl_list




    def vardecl_list(self):

        localctx = BKITParser.Vardecl_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_vardecl_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.var_decl()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 92
                self.match(BKITParser.COMMA)
                self.state = 93
                self.var_decl()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTEGER_LITERAL)
            else:
                return self.getToken(BKITParser.INTEGER_LITERAL, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_decl




    def var_decl(self):

        localctx = BKITParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(BKITParser.ID)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 100
                self.match(BKITParser.LSB)
                self.state = 101
                self.match(BKITParser.INTEGER_LITERAL)
                self.state = 102
                self.match(BKITParser.RSB)
                self.state = 107
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 108
                self.match(BKITParser.ASSIGN)
                self.state = 109
                self.literal()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_decllistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def para_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Para_declContext)
            else:
                return self.getTypedRuleContext(BKITParser.Para_declContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_para_decllist




    def para_decllist(self):

        localctx = BKITParser.Para_decllistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_para_decllist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.para_decl()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 113
                self.match(BKITParser.COMMA)
                self.state = 114
                self.para_decl()
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Para_declContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def INTEGER_LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INTEGER_LITERAL)
            else:
                return self.getToken(BKITParser.INTEGER_LITERAL, i)

        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_para_decl




    def para_decl(self):

        localctx = BKITParser.Para_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_para_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(BKITParser.ID)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.LSB:
                self.state = 121
                self.match(BKITParser.LSB)
                self.state = 122
                self.match(BKITParser.INTEGER_LITERAL)
                self.state = 123
                self.match(BKITParser.RSB)
                self.state = 128
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_declContext(ParserRuleContext):

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

        def stmtList(self):
            return self.getTypedRuleContext(BKITParser.StmtListContext,0)


        def ENDBODY(self):
            return self.getToken(BKITParser.ENDBODY, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def PARAMETER(self):
            return self.getToken(BKITParser.PARAMETER, 0)

        def para_decllist(self):
            return self.getTypedRuleContext(BKITParser.Para_decllistContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_func_decl




    def func_decl(self):

        localctx = BKITParser.Func_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_func_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BKITParser.FUNCTION)
            self.state = 130
            self.match(BKITParser.COLON)
            self.state = 131
            self.match(BKITParser.ID)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.PARAMETER:
                self.state = 132
                self.match(BKITParser.PARAMETER)
                self.state = 133
                self.match(BKITParser.COLON)
                self.state = 134
                self.para_decllist()


            self.state = 137
            self.match(BKITParser.BODY)
            self.state = 138
            self.match(BKITParser.COLON)
            self.state = 139
            self.stmtList()
            self.state = 140
            self.match(BKITParser.ENDBODY)
            self.state = 141
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtListContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def global_vardecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Global_vardeclContext)
            else:
                return self.getTypedRuleContext(BKITParser.Global_vardeclContext,i)


        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.StmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.StmtContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_stmtList




    def stmtList(self):

        localctx = BKITParser.StmtListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_stmtList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.VAR:
                self.state = 143
                self.global_vardecl()
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 152
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 149
                    self.stmt() 
                self.state = 154
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStmt(self):
            return self.getTypedRuleContext(BKITParser.IfStmtContext,0)


        def assignStmt(self):
            return self.getTypedRuleContext(BKITParser.AssignStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(BKITParser.WhileStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(BKITParser.ForStmtContext,0)


        def breakStmt(self):
            return self.getTypedRuleContext(BKITParser.BreakStmtContext,0)


        def continueStmt(self):
            return self.getTypedRuleContext(BKITParser.ContinueStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(BKITParser.ReturnStmtContext,0)


        def callStmt(self):
            return self.getTypedRuleContext(BKITParser.CallStmtContext,0)


        def doWhileStmt(self):
            return self.getTypedRuleContext(BKITParser.DoWhileStmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_stmt




    def stmt(self):

        localctx = BKITParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_stmt)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.ifStmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 156
                self.assignStmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 157
                self.whileStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 158
                self.forStmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 159
                self.breakStmt()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 160
                self.continueStmt()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 161
                self.returnStmt()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 162
                self.callStmt()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 163
                self.doWhileStmt()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(BKITParser.IF, 0)

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmtList(self):
            return self.getTypedRuleContext(BKITParser.StmtListContext,0)


        def ENDIF(self):
            return self.getToken(BKITParser.ENDIF, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def elifStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.ElifStmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.ElifStmtContext,i)


        def elseStmt(self):
            return self.getTypedRuleContext(BKITParser.ElseStmtContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_ifStmt




    def ifStmt(self):

        localctx = BKITParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.match(BKITParser.IF)
            self.state = 167
            self.exp1()
            self.state = 168
            self.match(BKITParser.THEN)
            self.state = 169
            self.stmtList()
            self.state = 173
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.ELSEIF:
                self.state = 170
                self.elifStmt()
                self.state = 175
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ELSE:
                self.state = 176
                self.elseStmt()


            self.state = 179
            self.match(BKITParser.ENDIF)
            self.state = 180
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSEIF(self):
            return self.getToken(BKITParser.ELSEIF, 0)

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def THEN(self):
            return self.getToken(BKITParser.THEN, 0)

        def stmtList(self):
            return self.getTypedRuleContext(BKITParser.StmtListContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elifStmt




    def elifStmt(self):

        localctx = BKITParser.ElifStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_elifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(BKITParser.ELSEIF)
            self.state = 183
            self.exp1()
            self.state = 184
            self.match(BKITParser.THEN)
            self.state = 185
            self.stmtList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(BKITParser.ELSE, 0)

        def stmtList(self):
            return self.getTypedRuleContext(BKITParser.StmtListContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_elseStmt




    def elseStmt(self):

        localctx = BKITParser.ElseStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_elseStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.match(BKITParser.ELSE)
            self.state = 188
            self.stmtList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmtList(self):
            return self.getTypedRuleContext(BKITParser.StmtListContext,0)


        def ENDWHILE(self):
            return self.getToken(BKITParser.ENDWHILE, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_whileStmt




    def whileStmt(self):

        localctx = BKITParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(BKITParser.WHILE)
            self.state = 191
            self.exp1()
            self.state = 192
            self.match(BKITParser.DO)
            self.state = 193
            self.stmtList()
            self.state = 194
            self.match(BKITParser.ENDWHILE)
            self.state = 195
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmtList(self):
            return self.getTypedRuleContext(BKITParser.StmtListContext,0)


        def WHILE(self):
            return self.getToken(BKITParser.WHILE, 0)

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def ENDDO(self):
            return self.getToken(BKITParser.ENDDO, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_doWhileStmt




    def doWhileStmt(self):

        localctx = BKITParser.DoWhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_doWhileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(BKITParser.DO)
            self.state = 198
            self.stmtList()
            self.state = 199
            self.match(BKITParser.WHILE)
            self.state = 200
            self.exp1()
            self.state = 201
            self.match(BKITParser.ENDDO)
            self.state = 202
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(BKITParser.FOR, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def DO(self):
            return self.getToken(BKITParser.DO, 0)

        def stmtList(self):
            return self.getTypedRuleContext(BKITParser.StmtListContext,0)


        def ENDFOR(self):
            return self.getToken(BKITParser.ENDFOR, 0)

        def DOT(self):
            return self.getToken(BKITParser.DOT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_forStmt




    def forStmt(self):

        localctx = BKITParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(BKITParser.FOR)
            self.state = 205
            self.match(BKITParser.LP)
            self.state = 206
            self.match(BKITParser.ID)
            self.state = 207
            self.match(BKITParser.ASSIGN)
            self.state = 208
            self.exp1()
            self.state = 209
            self.match(BKITParser.COMMA)
            self.state = 210
            self.exp1()
            self.state = 211
            self.match(BKITParser.COMMA)
            self.state = 212
            self.exp1()
            self.state = 213
            self.match(BKITParser.RP)
            self.state = 214
            self.match(BKITParser.DO)
            self.state = 215
            self.stmtList()
            self.state = 216
            self.match(BKITParser.ENDFOR)
            self.state = 217
            self.match(BKITParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_callStmt




    def callStmt(self):

        localctx = BKITParser.CallStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_callStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(BKITParser.ID)
            self.state = 220
            self.match(BKITParser.LP)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTEGER_LITERAL) | (1 << BKITParser.FLOAT_LITERAL) | (1 << BKITParser.BOOLEAN_LITERAL) | (1 << BKITParser.STRING_LITERAL) | (1 << BKITParser.SUB) | (1 << BKITParser.NOT) | (1 << BKITParser.FSUB) | (1 << BKITParser.LP) | (1 << BKITParser.LCB))) != 0) or _la==BKITParser.ID:
                self.state = 221
                self.exp1()
                self.state = 226
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 222
                    self.match(BKITParser.COMMA)
                    self.state = 223
                    self.exp1()
                    self.state = 228
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 231
            self.match(BKITParser.RP)
            self.state = 232
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(BKITParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_breakStmt




    def breakStmt(self):

        localctx = BKITParser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(BKITParser.BREAK)
            self.state = 235
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(BKITParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_continueStmt




    def continueStmt(self):

        localctx = BKITParser.ContinueStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_continueStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 237
            self.match(BKITParser.CONTINUE)
            self.state = 238
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(BKITParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_returnStmt




    def returnStmt(self):

        localctx = BKITParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 240
            self.match(BKITParser.RETURN)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTEGER_LITERAL) | (1 << BKITParser.FLOAT_LITERAL) | (1 << BKITParser.BOOLEAN_LITERAL) | (1 << BKITParser.STRING_LITERAL) | (1 << BKITParser.SUB) | (1 << BKITParser.NOT) | (1 << BKITParser.FSUB) | (1 << BKITParser.LP) | (1 << BKITParser.LCB))) != 0) or _la==BKITParser.ID:
                self.state = 241
                self.exp1()


            self.state = 244
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgulistContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_argulist




    def argulist(self):

        localctx = BKITParser.ArgulistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_argulist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTEGER_LITERAL) | (1 << BKITParser.FLOAT_LITERAL) | (1 << BKITParser.BOOLEAN_LITERAL) | (1 << BKITParser.STRING_LITERAL) | (1 << BKITParser.SUB) | (1 << BKITParser.NOT) | (1 << BKITParser.FSUB) | (1 << BKITParser.LP) | (1 << BKITParser.LCB))) != 0) or _la==BKITParser.ID:
                self.state = 246
                self.exp1()
                self.state = 251
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 247
                    self.match(BKITParser.COMMA)
                    self.state = 248
                    self.exp1()
                    self.state = 253
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_funcCall




    def funcCall(self):

        localctx = BKITParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(BKITParser.ID)
            self.state = 257
            self.match(BKITParser.LP)
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INTEGER_LITERAL) | (1 << BKITParser.FLOAT_LITERAL) | (1 << BKITParser.BOOLEAN_LITERAL) | (1 << BKITParser.STRING_LITERAL) | (1 << BKITParser.SUB) | (1 << BKITParser.NOT) | (1 << BKITParser.FSUB) | (1 << BKITParser.LP) | (1 << BKITParser.LCB))) != 0) or _la==BKITParser.ID:
                self.state = 258
                self.exp1()
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==BKITParser.COMMA:
                    self.state = 259
                    self.match(BKITParser.COMMA)
                    self.state = 260
                    self.exp1()
                    self.state = 265
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 268
            self.match(BKITParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(BKITParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_assignStmt




    def assignStmt(self):

        localctx = BKITParser.AssignStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self.lhs()
            self.state = 271
            self.match(BKITParser.ASSIGN)
            self.state = 272
            self.exp1()
            self.state = 273
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def index_exp(self):
            return self.getTypedRuleContext(BKITParser.Index_expContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_lhs




    def lhs(self):

        localctx = BKITParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_lhs)
        try:
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 275
                self.match(BKITParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 276
                self.index_exp()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp2Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp2Context,i)


        def LT(self):
            return self.getToken(BKITParser.LT, 0)

        def LTE(self):
            return self.getToken(BKITParser.LTE, 0)

        def EQ(self):
            return self.getToken(BKITParser.EQ, 0)

        def GT(self):
            return self.getToken(BKITParser.GT, 0)

        def GTE(self):
            return self.getToken(BKITParser.GTE, 0)

        def NEQ(self):
            return self.getToken(BKITParser.NEQ, 0)

        def FNEQ(self):
            return self.getToken(BKITParser.FNEQ, 0)

        def FLTE(self):
            return self.getToken(BKITParser.FLTE, 0)

        def FLT(self):
            return self.getToken(BKITParser.FLT, 0)

        def FGTE(self):
            return self.getToken(BKITParser.FGTE, 0)

        def FGT(self):
            return self.getToken(BKITParser.FGT, 0)

        def FEQ(self):
            return self.getToken(BKITParser.FEQ, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp1




    def exp1(self):

        localctx = BKITParser.Exp1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp1)
        self._la = 0 # Token type
        try:
            self.state = 284
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 279
                self.exp2(0)
                self.state = 280
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.LTE) | (1 << BKITParser.GTE) | (1 << BKITParser.NEQ) | (1 << BKITParser.EQ) | (1 << BKITParser.LT) | (1 << BKITParser.GT) | (1 << BKITParser.FLTE) | (1 << BKITParser.FGTE) | (1 << BKITParser.FNEQ) | (1 << BKITParser.FEQ) | (1 << BKITParser.FLT) | (1 << BKITParser.FGT))) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 281
                self.exp2(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 283
                self.exp2(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def exp2(self):
            return self.getTypedRuleContext(BKITParser.Exp2Context,0)


        def AND(self):
            return self.getToken(BKITParser.AND, 0)

        def OR(self):
            return self.getToken(BKITParser.OR, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp2



    def exp2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 287
            self.exp3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 294
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp2)
                    self.state = 289
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 290
                    _la = self._input.LA(1)
                    if not(_la==BKITParser.AND or _la==BKITParser.OR):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 291
                    self.exp3(0) 
                self.state = 296
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def exp3(self):
            return self.getTypedRuleContext(BKITParser.Exp3Context,0)


        def ADD(self):
            return self.getToken(BKITParser.ADD, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def FADD(self):
            return self.getToken(BKITParser.FADD, 0)

        def FSUB(self):
            return self.getToken(BKITParser.FSUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp3



    def exp3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exp3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self.exp4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp3)
                    self.state = 300
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 301
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.ADD) | (1 << BKITParser.SUB) | (1 << BKITParser.FADD) | (1 << BKITParser.FSUB))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 302
                    self.exp4(0) 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp4Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def exp4(self):
            return self.getTypedRuleContext(BKITParser.Exp4Context,0)


        def DIV(self):
            return self.getToken(BKITParser.DIV, 0)

        def MUL(self):
            return self.getToken(BKITParser.MUL, 0)

        def MOD(self):
            return self.getToken(BKITParser.MOD, 0)

        def FMUL(self):
            return self.getToken(BKITParser.FMUL, 0)

        def FDIV(self):
            return self.getToken(BKITParser.FDIV, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_exp4



    def exp4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = BKITParser.Exp4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exp4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.exp5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 316
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = BKITParser.Exp4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp4)
                    self.state = 311
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 312
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.MUL) | (1 << BKITParser.DIV) | (1 << BKITParser.MOD) | (1 << BKITParser.FMUL) | (1 << BKITParser.FDIV))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 313
                    self.exp5() 
                self.state = 318
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp5Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(BKITParser.NOT, 0)

        def exp5(self):
            return self.getTypedRuleContext(BKITParser.Exp5Context,0)


        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp5




    def exp5(self):

        localctx = BKITParser.Exp5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp5)
        try:
            self.state = 322
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 319
                self.match(BKITParser.NOT)
                self.state = 320
                self.exp5()
                pass
            elif token in [BKITParser.INTEGER_LITERAL, BKITParser.FLOAT_LITERAL, BKITParser.BOOLEAN_LITERAL, BKITParser.STRING_LITERAL, BKITParser.SUB, BKITParser.FSUB, BKITParser.LP, BKITParser.LCB, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 321
                self.exp6()
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


    class Exp6Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp6(self):
            return self.getTypedRuleContext(BKITParser.Exp6Context,0)


        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def FSUB(self):
            return self.getToken(BKITParser.FSUB, 0)

        def index_exp(self):
            return self.getTypedRuleContext(BKITParser.Index_expContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp6




    def exp6(self):

        localctx = BKITParser.Exp6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp6)
        self._la = 0 # Token type
        try:
            self.state = 327
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.SUB, BKITParser.FSUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 324
                _la = self._input.LA(1)
                if not(_la==BKITParser.SUB or _la==BKITParser.FSUB):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 325
                self.exp6()
                pass
            elif token in [BKITParser.INTEGER_LITERAL, BKITParser.FLOAT_LITERAL, BKITParser.BOOLEAN_LITERAL, BKITParser.STRING_LITERAL, BKITParser.LP, BKITParser.LCB, BKITParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.index_exp()
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


    class Index_expContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp7(self):
            return self.getTypedRuleContext(BKITParser.Exp7Context,0)


        def LSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSB)
            else:
                return self.getToken(BKITParser.LSB, i)

        def exp1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Exp1Context)
            else:
                return self.getTypedRuleContext(BKITParser.Exp1Context,i)


        def RSB(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSB)
            else:
                return self.getToken(BKITParser.RSB, i)

        def getRuleIndex(self):
            return BKITParser.RULE_index_exp




    def index_exp(self):

        localctx = BKITParser.Index_expContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_index_exp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.exp7()
            self.state = 336
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 330
                    self.match(BKITParser.LSB)
                    self.state = 331
                    self.exp1()
                    self.state = 332
                    self.match(BKITParser.RSB) 
                self.state = 338
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp7Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operands(self):
            return self.getTypedRuleContext(BKITParser.OperandsContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_exp7




    def exp7(self):

        localctx = BKITParser.Exp7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp7)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 339
            self.operands()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BKITParser.INTEGER_LITERAL, 0)

        def BOOLEAN_LITERAL(self):
            return self.getToken(BKITParser.BOOLEAN_LITERAL, 0)

        def array_literal(self):
            return self.getTypedRuleContext(BKITParser.Array_literalContext,0)


        def FLOAT_LITERAL(self):
            return self.getToken(BKITParser.FLOAT_LITERAL, 0)

        def STRING_LITERAL(self):
            return self.getToken(BKITParser.STRING_LITERAL, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_literal)
        try:
            self.state = 346
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INTEGER_LITERAL]:
                self.enterOuterAlt(localctx, 1)
                self.state = 341
                self.match(BKITParser.INTEGER_LITERAL)
                pass
            elif token in [BKITParser.BOOLEAN_LITERAL]:
                self.enterOuterAlt(localctx, 2)
                self.state = 342
                self.match(BKITParser.BOOLEAN_LITERAL)
                pass
            elif token in [BKITParser.LCB]:
                self.enterOuterAlt(localctx, 3)
                self.state = 343
                self.array_literal()
                pass
            elif token in [BKITParser.FLOAT_LITERAL]:
                self.enterOuterAlt(localctx, 4)
                self.state = 344
                self.match(BKITParser.FLOAT_LITERAL)
                pass
            elif token in [BKITParser.STRING_LITERAL]:
                self.enterOuterAlt(localctx, 5)
                self.state = 345
                self.match(BKITParser.STRING_LITERAL)
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


    class OperandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def funcCall(self):
            return self.getTypedRuleContext(BKITParser.FuncCallContext,0)


        def LP(self):
            return self.getToken(BKITParser.LP, 0)

        def exp1(self):
            return self.getTypedRuleContext(BKITParser.Exp1Context,0)


        def RP(self):
            return self.getToken(BKITParser.RP, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_operands




    def operands(self):

        localctx = BKITParser.OperandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operands)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 348
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 349
                self.match(BKITParser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 350
                self.funcCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 351
                self.match(BKITParser.LP)
                self.state = 352
                self.exp1()
                self.state = 353
                self.match(BKITParser.RP)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_literalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(BKITParser.LCB, 0)

        def RCB(self):
            return self.getToken(BKITParser.RCB, 0)

        def literal(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.LiteralContext)
            else:
                return self.getTypedRuleContext(BKITParser.LiteralContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_array_literal




    def array_literal(self):

        localctx = BKITParser.Array_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_array_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 357
            self.match(BKITParser.LCB)

            self.state = 358
            self.literal()
            self.state = 363
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 359
                self.match(BKITParser.COMMA)
                self.state = 360
                self.literal()
                self.state = 365
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 366
            self.match(BKITParser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER_LITERAL(self):
            return self.getToken(BKITParser.INTEGER_LITERAL, 0)

        def SUB(self):
            return self.getToken(BKITParser.SUB, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_number




    def number(self):

        localctx = BKITParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_number)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.SUB:
                self.state = 368
                self.match(BKITParser.SUB)


            self.state = 371
            self.match(BKITParser.INTEGER_LITERAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(BKITParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(BKITParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(BKITParser.STRING, 0)

        def BOOLEAN(self):
            return self.getToken(BKITParser.BOOLEAN, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_primitive_types




    def primitive_types(self):

        localctx = BKITParser.Primitive_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_primitive_types)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 373
            _la = self._input.LA(1)
            if not(((((_la - 63)) & ~0x3f) == 0 and ((1 << (_la - 63)) & ((1 << (BKITParser.INTEGER - 63)) | (1 << (BKITParser.STRING - 63)) | (1 << (BKITParser.FLOAT - 63)) | (1 << (BKITParser.BOOLEAN - 63)))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[24] = self.exp2_sempred
        self._predicates[25] = self.exp3_sempred
        self._predicates[26] = self.exp4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp2_sempred(self, localctx:Exp2Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp3_sempred(self, localctx:Exp3Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp4_sempred(self, localctx:Exp4Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         





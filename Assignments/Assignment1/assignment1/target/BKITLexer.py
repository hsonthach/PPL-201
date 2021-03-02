# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2L")
        buf.write("\u0265\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\3\3\3\5\3\u00a6\n")
        buf.write("\3\3\3\6\3\u00a9\n\3\r\3\16\3\u00aa\3\4\3\4\7\4\u00af")
        buf.write("\n\4\f\4\16\4\u00b2\13\4\3\4\3\4\3\4\3\4\3\4\7\4\u00b9")
        buf.write("\n\4\f\4\16\4\u00bc\13\4\3\4\7\4\u00bf\n\4\f\4\16\4\u00c2")
        buf.write("\13\4\3\4\3\4\3\4\3\4\7\4\u00c8\n\4\f\4\16\4\u00cb\13")
        buf.write("\4\3\4\7\4\u00ce\n\4\f\4\16\4\u00d1\13\4\3\4\3\4\3\4\3")
        buf.write("\4\7\4\u00d7\n\4\f\4\16\4\u00da\13\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4\u00e0\n\4\f\4\16\4\u00e3\13\4\5\4\u00e5\n\4\3\5\6\5")
        buf.write("\u00e8\n\5\r\5\16\5\u00e9\3\5\3\5\3\5\7\5\u00ef\n\5\f")
        buf.write("\5\16\5\u00f2\13\5\3\5\7\5\u00f5\n\5\f\5\16\5\u00f8\13")
        buf.write("\5\3\5\3\5\6\5\u00fc\n\5\r\5\16\5\u00fd\3\5\5\5\u0101")
        buf.write("\n\5\3\5\6\5\u0104\n\5\r\5\16\5\u0105\3\5\3\5\5\5\u010a")
        buf.write("\n\5\3\6\3\6\5\6\u010e\n\6\3\7\3\7\7\7\u0112\n\7\f\7\16")
        buf.write("\7\u0115\13\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\13")
        buf.write("\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\6\"\u0162\n\"\r")
        buf.write("\"\16\"\u0163\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'")
        buf.write("\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3,\3,\3,\3,\3,\3,\3,\3")
        buf.write("-\3-\3-\3-\3-\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\38\38\38\38\38\38\38\38\39\39\39\39\3:\3:\3:\3:\3:\3")
        buf.write(":\3;\3;\3;\3<\3<\3<\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3")
        buf.write(">\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3")
        buf.write("A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3B\3B\3C\3C\3C\3C\3C\3")
        buf.write("C\3C\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3E\3E\3E\3F\3F\3")
        buf.write("F\3F\3G\3G\3G\3H\3H\3H\3H\7H\u0223\nH\fH\16H\u0226\13")
        buf.write("H\3H\3H\3H\3H\3H\3I\3I\7I\u022f\nI\fI\16I\u0232\13I\3")
        buf.write("J\3J\7J\u0236\nJ\fJ\16J\u0239\13J\3J\5J\u023c\nJ\3J\3")
        buf.write("J\3K\3K\7K\u0242\nK\fK\16K\u0245\13K\3K\3K\3K\3L\3L\3")
        buf.write("L\3L\5L\u024e\nL\3M\3M\3M\3M\3M\3M\5M\u0256\nM\3M\3M\3")
        buf.write("N\3N\5N\u025c\nN\3O\3O\3O\3O\5O\u0262\nO\3P\3P\3\u0224")
        buf.write("\2Q\3\2\5\2\7\3\t\4\13\5\r\6\17\7\21\b\23\t\25\n\27\13")
        buf.write("\31\f\33\r\35\16\37\17!\20#\21%\22\'\23)\24+\25-\26/\27")
        buf.write("\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%")
        buf.write("M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67")
        buf.write("q8s9u:w;y<{=}>\177?\u0081@\u0083A\u0085B\u0087C\u0089")
        buf.write("D\u008bE\u008dF\u008fG\u0091H\u0093I\u0095J\u0097\2\u0099")
        buf.write("K\u009b\2\u009d\2\u009fL\3\2\21\3\2\62;\4\2GGgg\4\2--")
        buf.write("//\3\2\63;\5\2CHaach\3\2\629\3\2$$\5\2\13\f\17\17\"\"")
        buf.write("\3\2c|\6\2\62;C\\aac|\4\3\n\f\16\17\t\2))^^ddhhppttvv")
        buf.write("\3\2))\3\2,,\7\2\n\f\16\17$$))^^\2\u0281\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2")
        buf.write("\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2")
        buf.write("\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2")
        buf.write("\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2")
        buf.write("\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3")
        buf.write("\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q")
        buf.write("\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2")
        buf.write("[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2")
        buf.write("\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2")
        buf.write("\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009f\3\2\2\2\3\u00a1\3\2\2")
        buf.write("\2\5\u00a3\3\2\2\2\7\u00e4\3\2\2\2\t\u0109\3\2\2\2\13")
        buf.write("\u010d\3\2\2\2\r\u010f\3\2\2\2\17\u0119\3\2\2\2\21\u011b")
        buf.write("\3\2\2\2\23\u011d\3\2\2\2\25\u011f\3\2\2\2\27\u0121\3")
        buf.write("\2\2\2\31\u0123\3\2\2\2\33\u0125\3\2\2\2\35\u0127\3\2")
        buf.write("\2\2\37\u012a\3\2\2\2!\u012d\3\2\2\2#\u012f\3\2\2\2%\u0132")
        buf.write("\3\2\2\2\'\u0135\3\2\2\2)\u0138\3\2\2\2+\u013b\3\2\2\2")
        buf.write("-\u013d\3\2\2\2/\u013f\3\2\2\2\61\u0142\3\2\2\2\63\u0145")
        buf.write("\3\2\2\2\65\u0148\3\2\2\2\67\u014b\3\2\2\29\u014f\3\2")
        buf.write("\2\2;\u0153\3\2\2\2=\u0157\3\2\2\2?\u015a\3\2\2\2A\u015d")
        buf.write("\3\2\2\2C\u0161\3\2\2\2E\u0167\3\2\2\2G\u0169\3\2\2\2")
        buf.write("I\u016b\3\2\2\2K\u016d\3\2\2\2M\u016f\3\2\2\2O\u0171\3")
        buf.write("\2\2\2Q\u0173\3\2\2\2S\u0175\3\2\2\2U\u0177\3\2\2\2W\u0179")
        buf.write("\3\2\2\2Y\u0182\3\2\2\2[\u0187\3\2\2\2]\u018b\3\2\2\2")
        buf.write("_\u0195\3\2\2\2a\u019a\3\2\2\2c\u01a0\3\2\2\2e\u01a3\3")
        buf.write("\2\2\2g\u01a8\3\2\2\2i\u01ad\3\2\2\2k\u01b4\3\2\2\2m\u01ba")
        buf.write("\3\2\2\2o\u01c0\3\2\2\2q\u01c8\3\2\2\2s\u01cc\3\2\2\2")
        buf.write("u\u01d2\3\2\2\2w\u01d5\3\2\2\2y\u01d8\3\2\2\2{\u01df\3")
        buf.write("\2\2\2}\u01e8\3\2\2\2\177\u01ef\3\2\2\2\u0081\u01f5\3")
        buf.write("\2\2\2\u0083\u01fe\3\2\2\2\u0085\u0202\3\2\2\2\u0087\u0209")
        buf.write("\3\2\2\2\u0089\u020f\3\2\2\2\u008b\u0217\3\2\2\2\u008d")
        buf.write("\u021b\3\2\2\2\u008f\u021e\3\2\2\2\u0091\u022c\3\2\2\2")
        buf.write("\u0093\u0233\3\2\2\2\u0095\u023f\3\2\2\2\u0097\u024d\3")
        buf.write("\2\2\2\u0099\u024f\3\2\2\2\u009b\u025b\3\2\2\2\u009d\u0261")
        buf.write("\3\2\2\2\u009f\u0263\3\2\2\2\u00a1\u00a2\t\2\2\2\u00a2")
        buf.write("\4\3\2\2\2\u00a3\u00a5\t\3\2\2\u00a4\u00a6\t\4\2\2\u00a5")
        buf.write("\u00a4\3\2\2\2\u00a5\u00a6\3\2\2\2\u00a6\u00a8\3\2\2\2")
        buf.write("\u00a7\u00a9\5\3\2\2\u00a8\u00a7\3\2\2\2\u00a9\u00aa\3")
        buf.write("\2\2\2\u00aa\u00a8\3\2\2\2\u00aa\u00ab\3\2\2\2\u00ab\6")
        buf.write("\3\2\2\2\u00ac\u00b0\t\5\2\2\u00ad\u00af\t\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\u00b2\3\2\2\2\u00b0\u00ae\3\2\2\2")
        buf.write("\u00b0\u00b1\3\2\2\2\u00b1\u00e5\3\2\2\2\u00b2\u00b0\3")
        buf.write("\2\2\2\u00b3\u00e5\7\62\2\2\u00b4\u00b5\7\62\2\2\u00b5")
        buf.write("\u00b6\7z\2\2\u00b6\u00ba\3\2\2\2\u00b7\u00b9\t\6\2\2")
        buf.write("\u00b8\u00b7\3\2\2\2\u00b9\u00bc\3\2\2\2\u00ba\u00b8\3")
        buf.write("\2\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00c0\3\2\2\2\u00bc\u00ba")
        buf.write("\3\2\2\2\u00bd\u00bf\t\2\2\2\u00be\u00bd\3\2\2\2\u00bf")
        buf.write("\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3\2\2\2")
        buf.write("\u00c1\u00e5\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c4\7")
        buf.write("\62\2\2\u00c4\u00c5\7Z\2\2\u00c5\u00c9\3\2\2\2\u00c6\u00c8")
        buf.write("\t\6\2\2\u00c7\u00c6\3\2\2\2\u00c8\u00cb\3\2\2\2\u00c9")
        buf.write("\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca\u00cf\3\2\2\2")
        buf.write("\u00cb\u00c9\3\2\2\2\u00cc\u00ce\t\2\2\2\u00cd\u00cc\3")
        buf.write("\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2\u00cf\u00d0")
        buf.write("\3\2\2\2\u00d0\u00e5\3\2\2\2\u00d1\u00cf\3\2\2\2\u00d2")
        buf.write("\u00d3\7\62\2\2\u00d3\u00d4\7q\2\2\u00d4\u00d8\3\2\2\2")
        buf.write("\u00d5\u00d7\t\7\2\2\u00d6\u00d5\3\2\2\2\u00d7\u00da\3")
        buf.write("\2\2\2\u00d8\u00d6\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00e5")
        buf.write("\3\2\2\2\u00da\u00d8\3\2\2\2\u00db\u00dc\7\62\2\2\u00dc")
        buf.write("\u00dd\7Q\2\2\u00dd\u00e1\3\2\2\2\u00de\u00e0\t\7\2\2")
        buf.write("\u00df\u00de\3\2\2\2\u00e0\u00e3\3\2\2\2\u00e1\u00df\3")
        buf.write("\2\2\2\u00e1\u00e2\3\2\2\2\u00e2\u00e5\3\2\2\2\u00e3\u00e1")
        buf.write("\3\2\2\2\u00e4\u00ac\3\2\2\2\u00e4\u00b3\3\2\2\2\u00e4")
        buf.write("\u00b4\3\2\2\2\u00e4\u00c3\3\2\2\2\u00e4\u00d2\3\2\2\2")
        buf.write("\u00e4\u00db\3\2\2\2\u00e5\b\3\2\2\2\u00e6\u00e8\5\3\2")
        buf.write("\2\u00e7\u00e6\3\2\2\2\u00e8\u00e9\3\2\2\2\u00e9\u00e7")
        buf.write("\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00eb\3\2\2\2\u00eb")
        buf.write("\u00f0\5\17\b\2\u00ec\u00ef\5\3\2\2\u00ed\u00ef\5\5\3")
        buf.write("\2\u00ee\u00ec\3\2\2\2\u00ee\u00ed\3\2\2\2\u00ef\u00f2")
        buf.write("\3\2\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1")
        buf.write("\u010a\3\2\2\2\u00f2\u00f0\3\2\2\2\u00f3\u00f5\5\3\2\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6\u00f4\3")
        buf.write("\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f9\3\2\2\2\u00f8\u00f6")
        buf.write("\3\2\2\2\u00f9\u00fb\5\17\b\2\u00fa\u00fc\5\3\2\2\u00fb")
        buf.write("\u00fa\3\2\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fb\3\2\2\2")
        buf.write("\u00fd\u00fe\3\2\2\2\u00fe\u0100\3\2\2\2\u00ff\u0101\5")
        buf.write("\5\3\2\u0100\u00ff\3\2\2\2\u0100\u0101\3\2\2\2\u0101\u010a")
        buf.write("\3\2\2\2\u0102\u0104\5\3\2\2\u0103\u0102\3\2\2\2\u0104")
        buf.write("\u0105\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2")
        buf.write("\u0106\u0107\3\2\2\2\u0107\u0108\5\5\3\2\u0108\u010a\3")
        buf.write("\2\2\2\u0109\u00e7\3\2\2\2\u0109\u00f6\3\2\2\2\u0109\u0103")
        buf.write("\3\2\2\2\u010a\n\3\2\2\2\u010b\u010e\5_\60\2\u010c\u010e")
        buf.write("\5a\61\2\u010d\u010b\3\2\2\2\u010d\u010c\3\2\2\2\u010e")
        buf.write("\f\3\2\2\2\u010f\u0113\t\b\2\2\u0110\u0112\5\u009bN\2")
        buf.write("\u0111\u0110\3\2\2\2\u0112\u0115\3\2\2\2\u0113\u0111\3")
        buf.write("\2\2\2\u0113\u0114\3\2\2\2\u0114\u0116\3\2\2\2\u0115\u0113")
        buf.write("\3\2\2\2\u0116\u0117\t\b\2\2\u0117\u0118\b\7\2\2\u0118")
        buf.write("\16\3\2\2\2\u0119\u011a\7\60\2\2\u011a\20\3\2\2\2\u011b")
        buf.write("\u011c\7-\2\2\u011c\22\3\2\2\2\u011d\u011e\7/\2\2\u011e")
        buf.write("\24\3\2\2\2\u011f\u0120\7,\2\2\u0120\26\3\2\2\2\u0121")
        buf.write("\u0122\7^\2\2\u0122\30\3\2\2\2\u0123\u0124\7\'\2\2\u0124")
        buf.write("\32\3\2\2\2\u0125\u0126\7#\2\2\u0126\34\3\2\2\2\u0127")
        buf.write("\u0128\7(\2\2\u0128\u0129\7(\2\2\u0129\36\3\2\2\2\u012a")
        buf.write("\u012b\7~\2\2\u012b\u012c\7~\2\2\u012c \3\2\2\2\u012d")
        buf.write("\u012e\7?\2\2\u012e\"\3\2\2\2\u012f\u0130\7>\2\2\u0130")
        buf.write("\u0131\7?\2\2\u0131$\3\2\2\2\u0132\u0133\7@\2\2\u0133")
        buf.write("\u0134\7?\2\2\u0134&\3\2\2\2\u0135\u0136\7#\2\2\u0136")
        buf.write("\u0137\7?\2\2\u0137(\3\2\2\2\u0138\u0139\7?\2\2\u0139")
        buf.write("\u013a\7?\2\2\u013a*\3\2\2\2\u013b\u013c\7>\2\2\u013c")
        buf.write(",\3\2\2\2\u013d\u013e\7@\2\2\u013e.\3\2\2\2\u013f\u0140")
        buf.write("\7-\2\2\u0140\u0141\7\60\2\2\u0141\60\3\2\2\2\u0142\u0143")
        buf.write("\7/\2\2\u0143\u0144\7\60\2\2\u0144\62\3\2\2\2\u0145\u0146")
        buf.write("\7,\2\2\u0146\u0147\7\60\2\2\u0147\64\3\2\2\2\u0148\u0149")
        buf.write("\7^\2\2\u0149\u014a\7\60\2\2\u014a\66\3\2\2\2\u014b\u014c")
        buf.write("\7>\2\2\u014c\u014d\7?\2\2\u014d\u014e\7\60\2\2\u014e")
        buf.write("8\3\2\2\2\u014f\u0150\7@\2\2\u0150\u0151\7?\2\2\u0151")
        buf.write("\u0152\7\60\2\2\u0152:\3\2\2\2\u0153\u0154\7?\2\2\u0154")
        buf.write("\u0155\7^\2\2\u0155\u0156\7?\2\2\u0156<\3\2\2\2\u0157")
        buf.write("\u0158\7?\2\2\u0158\u0159\7\60\2\2\u0159>\3\2\2\2\u015a")
        buf.write("\u015b\7>\2\2\u015b\u015c\7\60\2\2\u015c@\3\2\2\2\u015d")
        buf.write("\u015e\7@\2\2\u015e\u015f\7\60\2\2\u015fB\3\2\2\2\u0160")
        buf.write("\u0162\t\t\2\2\u0161\u0160\3\2\2\2\u0162\u0163\3\2\2\2")
        buf.write("\u0163\u0161\3\2\2\2\u0163\u0164\3\2\2\2\u0164\u0165\3")
        buf.write("\2\2\2\u0165\u0166\b\"\3\2\u0166D\3\2\2\2\u0167\u0168")
        buf.write("\7*\2\2\u0168F\3\2\2\2\u0169\u016a\7+\2\2\u016aH\3\2\2")
        buf.write("\2\u016b\u016c\7}\2\2\u016cJ\3\2\2\2\u016d\u016e\7\177")
        buf.write("\2\2\u016eL\3\2\2\2\u016f\u0170\7]\2\2\u0170N\3\2\2\2")
        buf.write("\u0171\u0172\7_\2\2\u0172P\3\2\2\2\u0173\u0174\7=\2\2")
        buf.write("\u0174R\3\2\2\2\u0175\u0176\7.\2\2\u0176T\3\2\2\2\u0177")
        buf.write("\u0178\7<\2\2\u0178V\3\2\2\2\u0179\u017a\7H\2\2\u017a")
        buf.write("\u017b\7w\2\2\u017b\u017c\7p\2\2\u017c\u017d\7e\2\2\u017d")
        buf.write("\u017e\7v\2\2\u017e\u017f\7k\2\2\u017f\u0180\7q\2\2\u0180")
        buf.write("\u0181\7p\2\2\u0181X\3\2\2\2\u0182\u0183\7D\2\2\u0183")
        buf.write("\u0184\7q\2\2\u0184\u0185\7f\2\2\u0185\u0186\7{\2\2\u0186")
        buf.write("Z\3\2\2\2\u0187\u0188\7G\2\2\u0188\u0189\7p\2\2\u0189")
        buf.write("\u018a\7f\2\2\u018a\\\3\2\2\2\u018b\u018c\7R\2\2\u018c")
        buf.write("\u018d\7c\2\2\u018d\u018e\7t\2\2\u018e\u018f\7c\2\2\u018f")
        buf.write("\u0190\7o\2\2\u0190\u0191\7g\2\2\u0191\u0192\7v\2\2\u0192")
        buf.write("\u0193\7g\2\2\u0193\u0194\7t\2\2\u0194^\3\2\2\2\u0195")
        buf.write("\u0196\7V\2\2\u0196\u0197\7t\2\2\u0197\u0198\7w\2\2\u0198")
        buf.write("\u0199\7g\2\2\u0199`\3\2\2\2\u019a\u019b\7H\2\2\u019b")
        buf.write("\u019c\7c\2\2\u019c\u019d\7n\2\2\u019d\u019e\7u\2\2\u019e")
        buf.write("\u019f\7g\2\2\u019fb\3\2\2\2\u01a0\u01a1\7K\2\2\u01a1")
        buf.write("\u01a2\7h\2\2\u01a2d\3\2\2\2\u01a3\u01a4\7V\2\2\u01a4")
        buf.write("\u01a5\7j\2\2\u01a5\u01a6\7g\2\2\u01a6\u01a7\7p\2\2\u01a7")
        buf.write("f\3\2\2\2\u01a8\u01a9\7G\2\2\u01a9\u01aa\7n\2\2\u01aa")
        buf.write("\u01ab\7u\2\2\u01ab\u01ac\7g\2\2\u01ach\3\2\2\2\u01ad")
        buf.write("\u01ae\7G\2\2\u01ae\u01af\7n\2\2\u01af\u01b0\7u\2\2\u01b0")
        buf.write("\u01b1\7g\2\2\u01b1\u01b2\7K\2\2\u01b2\u01b3\7h\2\2\u01b3")
        buf.write("j\3\2\2\2\u01b4\u01b5\7G\2\2\u01b5\u01b6\7p\2\2\u01b6")
        buf.write("\u01b7\7f\2\2\u01b7\u01b8\7K\2\2\u01b8\u01b9\7h\2\2\u01b9")
        buf.write("l\3\2\2\2\u01ba\u01bb\7G\2\2\u01bb\u01bc\7p\2\2\u01bc")
        buf.write("\u01bd\7f\2\2\u01bd\u01be\7F\2\2\u01be\u01bf\7q\2\2\u01bf")
        buf.write("n\3\2\2\2\u01c0\u01c1\7G\2\2\u01c1\u01c2\7p\2\2\u01c2")
        buf.write("\u01c3\7f\2\2\u01c3\u01c4\7D\2\2\u01c4\u01c5\7q\2\2\u01c5")
        buf.write("\u01c6\7f\2\2\u01c6\u01c7\7{\2\2\u01c7p\3\2\2\2\u01c8")
        buf.write("\u01c9\7H\2\2\u01c9\u01ca\7q\2\2\u01ca\u01cb\7t\2\2\u01cb")
        buf.write("r\3\2\2\2\u01cc\u01cd\7Y\2\2\u01cd\u01ce\7j\2\2\u01ce")
        buf.write("\u01cf\7k\2\2\u01cf\u01d0\7n\2\2\u01d0\u01d1\7g\2\2\u01d1")
        buf.write("t\3\2\2\2\u01d2\u01d3\7F\2\2\u01d3\u01d4\7q\2\2\u01d4")
        buf.write("v\3\2\2\2\u01d5\u01d6\7V\2\2\u01d6\u01d7\7q\2\2\u01d7")
        buf.write("x\3\2\2\2\u01d8\u01d9\7G\2\2\u01d9\u01da\7p\2\2\u01da")
        buf.write("\u01db\7f\2\2\u01db\u01dc\7H\2\2\u01dc\u01dd\7q\2\2\u01dd")
        buf.write("\u01de\7t\2\2\u01dez\3\2\2\2\u01df\u01e0\7G\2\2\u01e0")
        buf.write("\u01e1\7p\2\2\u01e1\u01e2\7f\2\2\u01e2\u01e3\7Y\2\2\u01e3")
        buf.write("\u01e4\7j\2\2\u01e4\u01e5\7k\2\2\u01e5\u01e6\7n\2\2\u01e6")
        buf.write("\u01e7\7g\2\2\u01e7|\3\2\2\2\u01e8\u01e9\7T\2\2\u01e9")
        buf.write("\u01ea\7g\2\2\u01ea\u01eb\7v\2\2\u01eb\u01ec\7w\2\2\u01ec")
        buf.write("\u01ed\7t\2\2\u01ed\u01ee\7p\2\2\u01ee~\3\2\2\2\u01ef")
        buf.write("\u01f0\7D\2\2\u01f0\u01f1\7t\2\2\u01f1\u01f2\7g\2\2\u01f2")
        buf.write("\u01f3\7c\2\2\u01f3\u01f4\7m\2\2\u01f4\u0080\3\2\2\2\u01f5")
        buf.write("\u01f6\7E\2\2\u01f6\u01f7\7q\2\2\u01f7\u01f8\7p\2\2\u01f8")
        buf.write("\u01f9\7v\2\2\u01f9\u01fa\7k\2\2\u01fa\u01fb\7p\2\2\u01fb")
        buf.write("\u01fc\7w\2\2\u01fc\u01fd\7g\2\2\u01fd\u0082\3\2\2\2\u01fe")
        buf.write("\u01ff\7k\2\2\u01ff\u0200\7p\2\2\u0200\u0201\7v\2\2\u0201")
        buf.write("\u0084\3\2\2\2\u0202\u0203\7u\2\2\u0203\u0204\7v\2\2\u0204")
        buf.write("\u0205\7t\2\2\u0205\u0206\7k\2\2\u0206\u0207\7p\2\2\u0207")
        buf.write("\u0208\7i\2\2\u0208\u0086\3\2\2\2\u0209\u020a\7h\2\2\u020a")
        buf.write("\u020b\7n\2\2\u020b\u020c\7q\2\2\u020c\u020d\7c\2\2\u020d")
        buf.write("\u020e\7v\2\2\u020e\u0088\3\2\2\2\u020f\u0210\7d\2\2\u0210")
        buf.write("\u0211\7q\2\2\u0211\u0212\7q\2\2\u0212\u0213\7n\2\2\u0213")
        buf.write("\u0214\7g\2\2\u0214\u0215\7c\2\2\u0215\u0216\7p\2\2\u0216")
        buf.write("\u008a\3\2\2\2\u0217\u0218\7X\2\2\u0218\u0219\7c\2\2\u0219")
        buf.write("\u021a\7t\2\2\u021a\u008c\3\2\2\2\u021b\u021c\7q\2\2\u021c")
        buf.write("\u021d\7h\2\2\u021d\u008e\3\2\2\2\u021e\u021f\7,\2\2\u021f")
        buf.write("\u0220\7,\2\2\u0220\u0224\3\2\2\2\u0221\u0223\13\2\2\2")
        buf.write("\u0222\u0221\3\2\2\2\u0223\u0226\3\2\2\2\u0224\u0225\3")
        buf.write("\2\2\2\u0224\u0222\3\2\2\2\u0225\u0227\3\2\2\2\u0226\u0224")
        buf.write("\3\2\2\2\u0227\u0228\7,\2\2\u0228\u0229\7,\2\2\u0229\u022a")
        buf.write("\3\2\2\2\u022a\u022b\bH\3\2\u022b\u0090\3\2\2\2\u022c")
        buf.write("\u0230\t\n\2\2\u022d\u022f\t\13\2\2\u022e\u022d\3\2\2")
        buf.write("\2\u022f\u0232\3\2\2\2\u0230\u022e\3\2\2\2\u0230\u0231")
        buf.write("\3\2\2\2\u0231\u0092\3\2\2\2\u0232\u0230\3\2\2\2\u0233")
        buf.write("\u0237\7$\2\2\u0234\u0236\5\u009bN\2\u0235\u0234\3\2\2")
        buf.write("\2\u0236\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238")
        buf.write("\3\2\2\2\u0238\u023b\3\2\2\2\u0239\u0237\3\2\2\2\u023a")
        buf.write("\u023c\t\f\2\2\u023b\u023a\3\2\2\2\u023c\u023d\3\2\2\2")
        buf.write("\u023d\u023e\bJ\4\2\u023e\u0094\3\2\2\2\u023f\u0243\7")
        buf.write("$\2\2\u0240\u0242\5\u009bN\2\u0241\u0240\3\2\2\2\u0242")
        buf.write("\u0245\3\2\2\2\u0243\u0241\3\2\2\2\u0243\u0244\3\2\2\2")
        buf.write("\u0244\u0246\3\2\2\2\u0245\u0243\3\2\2\2\u0246\u0247\5")
        buf.write("\u0097L\2\u0247\u0248\bK\5\2\u0248\u0096\3\2\2\2\u0249")
        buf.write("\u024a\7^\2\2\u024a\u024e\n\r\2\2\u024b\u024c\t\16\2\2")
        buf.write("\u024c\u024e\n\b\2\2\u024d\u0249\3\2\2\2\u024d\u024b\3")
        buf.write("\2\2\2\u024e\u0098\3\2\2\2\u024f\u0250\7,\2\2\u0250\u0251")
        buf.write("\7,\2\2\u0251\u0255\3\2\2\2\u0252\u0256\n\17\2\2\u0253")
        buf.write("\u0254\7,\2\2\u0254\u0256\n\17\2\2\u0255\u0252\3\2\2\2")
        buf.write("\u0255\u0253\3\2\2\2\u0256\u0257\3\2\2\2\u0257\u0258\b")
        buf.write("M\6\2\u0258\u009a\3\2\2\2\u0259\u025c\n\20\2\2\u025a\u025c")
        buf.write("\5\u009dO\2\u025b\u0259\3\2\2\2\u025b\u025a\3\2\2\2\u025c")
        buf.write("\u009c\3\2\2\2\u025d\u025e\7^\2\2\u025e\u0262\t\r\2\2")
        buf.write("\u025f\u0260\7)\2\2\u0260\u0262\7$\2\2\u0261\u025d\3\2")
        buf.write("\2\2\u0261\u025f\3\2\2\2\u0262\u009e\3\2\2\2\u0263\u0264")
        buf.write("\13\2\2\2\u0264\u00a0\3\2\2\2!\2\u00a5\u00aa\u00b0\u00ba")
        buf.write("\u00c0\u00c9\u00cf\u00d8\u00e1\u00e4\u00e9\u00ee\u00f0")
        buf.write("\u00f6\u00fd\u0100\u0105\u0109\u010d\u0113\u0163\u0224")
        buf.write("\u0230\u0237\u023b\u0243\u024d\u0255\u025b\u0261\7\3\7")
        buf.write("\2\b\2\2\3J\3\3K\4\3M\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER_LITERAL = 1
    FLOAT_LITERAL = 2
    BOOLEAN_LITERAL = 3
    STRING_LITERAL = 4
    DOT = 5
    ADD = 6
    SUB = 7
    MUL = 8
    DIV = 9
    MOD = 10
    NOT = 11
    AND = 12
    OR = 13
    ASSIGN = 14
    LTE = 15
    GTE = 16
    NEQ = 17
    EQ = 18
    LT = 19
    GT = 20
    FADD = 21
    FSUB = 22
    FMUL = 23
    FDIV = 24
    FLTE = 25
    FGTE = 26
    FNEQ = 27
    FEQ = 28
    FLT = 29
    FGT = 30
    WS = 31
    LP = 32
    RP = 33
    LCB = 34
    RCB = 35
    LSB = 36
    RSB = 37
    SEMI = 38
    COMMA = 39
    COLON = 40
    FUNCTION = 41
    BODY = 42
    END = 43
    PARAMETER = 44
    TRUE = 45
    FALSE = 46
    IF = 47
    THEN = 48
    ELSE = 49
    ELSEIF = 50
    ENDIF = 51
    ENDDO = 52
    ENDBODY = 53
    FOR = 54
    WHILE = 55
    DO = 56
    TO = 57
    ENDFOR = 58
    ENDWHILE = 59
    RETURN = 60
    BREAK = 61
    CONTINUE = 62
    INTEGER = 63
    STRING = 64
    FLOAT = 65
    BOOLEAN = 66
    VAR = 67
    OF = 68
    COMMENT_LITERAL = 69
    ID = 70
    UNCLOSE_STRING = 71
    ILLEGAL_ESCAPE = 72
    UNTERMINATED_COMMENT = 73
    ERROR_CHAR = 74

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'+'", "'-'", "'*'", "'\\'", "'%'", "'!'", "'&&'", "'||'", 
            "'='", "'<='", "'>='", "'!='", "'=='", "'<'", "'>'", "'+.'", 
            "'-.'", "'*.'", "'\\.'", "'<=.'", "'>=.'", "'=\\='", "'=.'", 
            "'<.'", "'>.'", "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", 
            "','", "':'", "'Function'", "'Body'", "'End'", "'Parameter'", 
            "'True'", "'False'", "'If'", "'Then'", "'Else'", "'ElseIf'", 
            "'EndIf'", "'EndDo'", "'EndBody'", "'For'", "'While'", "'Do'", 
            "'To'", "'EndFor'", "'EndWhile'", "'Return'", "'Break'", "'Continue'", 
            "'int'", "'string'", "'float'", "'boolean'", "'Var'", "'of'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
            "DOT", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
            "ASSIGN", "LTE", "GTE", "NEQ", "EQ", "LT", "GT", "FADD", "FSUB", 
            "FMUL", "FDIV", "FLTE", "FGTE", "FNEQ", "FEQ", "FLT", "FGT", 
            "WS", "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
            "COLON", "FUNCTION", "BODY", "END", "PARAMETER", "TRUE", "FALSE", 
            "IF", "THEN", "ELSE", "ELSEIF", "ENDIF", "ENDDO", "ENDBODY", 
            "FOR", "WHILE", "DO", "TO", "ENDFOR", "ENDWHILE", "RETURN", 
            "BREAK", "CONTINUE", "INTEGER", "STRING", "FLOAT", "BOOLEAN", 
            "VAR", "OF", "COMMENT_LITERAL", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT", "ERROR_CHAR" ]

    ruleNames = [ "DIGIT", "EXPONENT", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                  "BOOLEAN_LITERAL", "STRING_LITERAL", "DOT", "ADD", "SUB", 
                  "MUL", "DIV", "MOD", "NOT", "AND", "OR", "ASSIGN", "LTE", 
                  "GTE", "NEQ", "EQ", "LT", "GT", "FADD", "FSUB", "FMUL", 
                  "FDIV", "FLTE", "FGTE", "FNEQ", "FEQ", "FLT", "FGT", "WS", 
                  "LP", "RP", "LCB", "RCB", "LSB", "RSB", "SEMI", "COMMA", 
                  "COLON", "FUNCTION", "BODY", "END", "PARAMETER", "TRUE", 
                  "FALSE", "IF", "THEN", "ELSE", "ELSEIF", "ENDIF", "ENDDO", 
                  "ENDBODY", "FOR", "WHILE", "DO", "TO", "ENDFOR", "ENDWHILE", 
                  "RETURN", "BREAK", "CONTINUE", "INTEGER", "STRING", "FLOAT", 
                  "BOOLEAN", "VAR", "OF", "COMMENT_LITERAL", "ID", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "ESC_ILLEGAL", "UNTERMINATED_COMMENT", 
                  "STR_CHAR", "ESC_SEQ", "ERROR_CHAR" ]

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


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.STRING_LITERAL_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            actions[75] = self.UNTERMINATED_COMMENT_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LITERAL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

            		y = str(self.text)
            		self.text = y[1:-1]
            	
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            		y = str(self.text)
            		possible = ['\b', '\t', '\n', '\f', '\r', '\"', "\'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def UNTERMINATED_COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise UnterminatedComment()
            	
     



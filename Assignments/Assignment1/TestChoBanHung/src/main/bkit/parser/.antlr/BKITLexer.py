# Generated from c:\Users\ASUS\Desktop\201\PPL\Assignments\Assignment1\TestChoBanHung\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2O")
        buf.write("\u0274\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\3\2\3\2\3")
        buf.write("\3\3\3\5\3\u00ac\n\3\3\3\6\3\u00af\n\3\r\3\16\3\u00b0")
        buf.write("\3\4\3\4\7\4\u00b5\n\4\f\4\16\4\u00b8\13\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\7\4\u00bf\n\4\f\4\16\4\u00c2\13\4\3\4\7\4\u00c5")
        buf.write("\n\4\f\4\16\4\u00c8\13\4\3\4\3\4\3\4\3\4\7\4\u00ce\n\4")
        buf.write("\f\4\16\4\u00d1\13\4\3\4\7\4\u00d4\n\4\f\4\16\4\u00d7")
        buf.write("\13\4\3\4\3\4\3\4\3\4\7\4\u00dd\n\4\f\4\16\4\u00e0\13")
        buf.write("\4\3\4\3\4\3\4\3\4\7\4\u00e6\n\4\f\4\16\4\u00e9\13\4\5")
        buf.write("\4\u00eb\n\4\3\5\6\5\u00ee\n\5\r\5\16\5\u00ef\3\5\3\5")
        buf.write("\3\5\7\5\u00f5\n\5\f\5\16\5\u00f8\13\5\3\5\7\5\u00fb\n")
        buf.write("\5\f\5\16\5\u00fe\13\5\3\5\3\5\6\5\u0102\n\5\r\5\16\5")
        buf.write("\u0103\3\5\5\5\u0107\n\5\3\5\6\5\u010a\n\5\r\5\16\5\u010b")
        buf.write("\3\5\3\5\5\5\u0110\n\5\3\6\3\6\5\6\u0114\n\6\3\7\3\7\7")
        buf.write("\7\u0118\n\7\f\7\16\7\u011b\13\7\3\7\3\7\3\7\3\b\3\b\7")
        buf.write("\b\u0122\n\b\f\b\16\b\u0125\13\b\3\b\3\b\3\t\3\t\3\t\7")
        buf.write("\t\u012c\n\t\f\t\16\t\u012f\13\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\20\3\21\3\21\3\21\3\22\3\22\3\23\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3\"\3\"\3\"\3#")
        buf.write("\6#\u017c\n#\r#\16#\u017d\3#\3#\3$\3$\3%\3%\3&\3&\3\'")
        buf.write("\3\'\3(\3(\3)\3)\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3")
        buf.write("\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64")
        buf.write("\3\64\3\64\3\64\3\64\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\38\38\38\38\38\38\38\3")
        buf.write("9\39\39\39\39\39\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3<\3<\3<\3<\3=\3=\3=\3=\3=\3=\3>\3>\3>\3?\3?\3?\3")
        buf.write("@\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3A\3A\3A\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3")
        buf.write("D\3D\3E\3E\3E\3E\3F\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3")
        buf.write("G\3H\3H\3H\3H\3H\3H\3H\3H\3I\3I\3I\3I\3J\3J\3J\3K\3K\3")
        buf.write("K\3K\3K\3K\3L\3L\7L\u0249\nL\fL\16L\u024c\13L\3M\3M\7")
        buf.write("M\u0250\nM\fM\16M\u0253\13M\3M\5M\u0256\nM\3M\3M\3N\3")
        buf.write("N\7N\u025c\nN\fN\16N\u025f\13N\3N\3N\3N\3O\3O\5O\u0266")
        buf.write("\nO\3P\3P\3P\3Q\3Q\3Q\5Q\u026e\nQ\3R\3R\3R\3S\3S\3\u012d")
        buf.write("\2T\3\2\5\2\7\3\t\4\13\5\r\6\17\7\21\b\23\t\25\n\27\13")
        buf.write("\31\f\33\r\35\16\37\17!\20#\21%\22\'\23)\24+\25-\26/\27")
        buf.write("\61\30\63\31\65\32\67\339\34;\35=\36?\37A C!E\"G#I$K%")
        buf.write("M&O\'Q(S)U*W+Y,[-]._/a\60c\61e\62g\63i\64k\65m\66o\67")
        buf.write("q8s9u:w;y<{=}>\177?\u0081@\u0083A\u0085B\u0087C\u0089")
        buf.write("D\u008bE\u008dF\u008fG\u0091H\u0093I\u0095J\u0097K\u0099")
        buf.write("L\u009bM\u009d\2\u009f\2\u00a1\2\u00a3N\u00a5O\3\2\17")
        buf.write("\3\2\62;\4\2GGgg\3\2\63;\5\2CHaach\3\2\629\4\2\f\f\16")
        buf.write("\17\5\2\13\f\17\17\"\"\5\2C\\aac|\6\2\62;C\\aac|\7\3\n")
        buf.write("\f\16\17$$))^^\7\2\n\f\16\17$$))^^\n\2$$))^^ddhhppttv")
        buf.write("v\3\2^^\2\u028f\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2")
        buf.write("\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25")
        buf.write("\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3")
        buf.write("\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2")
        buf.write("\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2")
        buf.write("\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\2")
        buf.write("9\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2")
        buf.write("\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2")
        buf.write("\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2")
        buf.write("\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3")
        buf.write("\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i")
        buf.write("\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2")
        buf.write("s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2")
        buf.write("\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2")
        buf.write("\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2")
        buf.write("\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\3\u00a7\3\2\2\2\5\u00a9\3\2\2\2\7\u00ea\3\2\2")
        buf.write("\2\t\u010f\3\2\2\2\13\u0113\3\2\2\2\r\u0115\3\2\2\2\17")
        buf.write("\u011f\3\2\2\2\21\u0128\3\2\2\2\23\u0135\3\2\2\2\25\u0137")
        buf.write("\3\2\2\2\27\u0139\3\2\2\2\31\u013b\3\2\2\2\33\u013d\3")
        buf.write("\2\2\2\35\u013f\3\2\2\2\37\u0141\3\2\2\2!\u0144\3\2\2")
        buf.write("\2#\u0147\3\2\2\2%\u0149\3\2\2\2\'\u014c\3\2\2\2)\u014f")
        buf.write("\3\2\2\2+\u0152\3\2\2\2-\u0155\3\2\2\2/\u0157\3\2\2\2")
        buf.write("\61\u0159\3\2\2\2\63\u015c\3\2\2\2\65\u015f\3\2\2\2\67")
        buf.write("\u0162\3\2\2\29\u0165\3\2\2\2;\u0169\3\2\2\2=\u016d\3")
        buf.write("\2\2\2?\u0171\3\2\2\2A\u0174\3\2\2\2C\u0177\3\2\2\2E\u017b")
        buf.write("\3\2\2\2G\u0181\3\2\2\2I\u0183\3\2\2\2K\u0185\3\2\2\2")
        buf.write("M\u0187\3\2\2\2O\u0189\3\2\2\2Q\u018b\3\2\2\2S\u018d\3")
        buf.write("\2\2\2U\u018f\3\2\2\2W\u0191\3\2\2\2Y\u0193\3\2\2\2[\u0195")
        buf.write("\3\2\2\2]\u019e\3\2\2\2_\u01a4\3\2\2\2a\u01a9\3\2\2\2")
        buf.write("c\u01ad\3\2\2\2e\u01b7\3\2\2\2g\u01bc\3\2\2\2i\u01c2\3")
        buf.write("\2\2\2k\u01c5\3\2\2\2m\u01ca\3\2\2\2o\u01cf\3\2\2\2q\u01d6")
        buf.write("\3\2\2\2s\u01dc\3\2\2\2u\u01e2\3\2\2\2w\u01ea\3\2\2\2")
        buf.write("y\u01ee\3\2\2\2{\u01f4\3\2\2\2}\u01f7\3\2\2\2\177\u01fa")
        buf.write("\3\2\2\2\u0081\u0201\3\2\2\2\u0083\u020a\3\2\2\2\u0085")
        buf.write("\u0211\3\2\2\2\u0087\u0217\3\2\2\2\u0089\u0220\3\2\2\2")
        buf.write("\u008b\u0224\3\2\2\2\u008d\u022b\3\2\2\2\u008f\u0231\3")
        buf.write("\2\2\2\u0091\u0239\3\2\2\2\u0093\u023d\3\2\2\2\u0095\u0240")
        buf.write("\3\2\2\2\u0097\u0246\3\2\2\2\u0099\u024d\3\2\2\2\u009b")
        buf.write("\u0259\3\2\2\2\u009d\u0265\3\2\2\2\u009f\u0267\3\2\2\2")
        buf.write("\u00a1\u026d\3\2\2\2\u00a3\u026f\3\2\2\2\u00a5\u0272\3")
        buf.write("\2\2\2\u00a7\u00a8\t\2\2\2\u00a8\4\3\2\2\2\u00a9\u00ab")
        buf.write("\t\3\2\2\u00aa\u00ac\7/\2\2\u00ab\u00aa\3\2\2\2\u00ab")
        buf.write("\u00ac\3\2\2\2\u00ac\u00ae\3\2\2\2\u00ad\u00af\5\3\2\2")
        buf.write("\u00ae\u00ad\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0\u00ae\3")
        buf.write("\2\2\2\u00b0\u00b1\3\2\2\2\u00b1\6\3\2\2\2\u00b2\u00b6")
        buf.write("\t\4\2\2\u00b3\u00b5\t\2\2\2\u00b4\u00b3\3\2\2\2\u00b5")
        buf.write("\u00b8\3\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2")
        buf.write("\u00b7\u00eb\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00eb\7")
        buf.write("\62\2\2\u00ba\u00bb\7\62\2\2\u00bb\u00bc\7z\2\2\u00bc")
        buf.write("\u00c0\3\2\2\2\u00bd\u00bf\t\5\2\2\u00be\u00bd\3\2\2\2")
        buf.write("\u00bf\u00c2\3\2\2\2\u00c0\u00be\3\2\2\2\u00c0\u00c1\3")
        buf.write("\2\2\2\u00c1\u00c6\3\2\2\2\u00c2\u00c0\3\2\2\2\u00c3\u00c5")
        buf.write("\t\2\2\2\u00c4\u00c3\3\2\2\2\u00c5\u00c8\3\2\2\2\u00c6")
        buf.write("\u00c4\3\2\2\2\u00c6\u00c7\3\2\2\2\u00c7\u00eb\3\2\2\2")
        buf.write("\u00c8\u00c6\3\2\2\2\u00c9\u00ca\7\62\2\2\u00ca\u00cb")
        buf.write("\7Z\2\2\u00cb\u00cf\3\2\2\2\u00cc\u00ce\t\5\2\2\u00cd")
        buf.write("\u00cc\3\2\2\2\u00ce\u00d1\3\2\2\2\u00cf\u00cd\3\2\2\2")
        buf.write("\u00cf\u00d0\3\2\2\2\u00d0\u00d5\3\2\2\2\u00d1\u00cf\3")
        buf.write("\2\2\2\u00d2\u00d4\t\2\2\2\u00d3\u00d2\3\2\2\2\u00d4\u00d7")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d5\u00d6\3\2\2\2\u00d6")
        buf.write("\u00eb\3\2\2\2\u00d7\u00d5\3\2\2\2\u00d8\u00d9\7\62\2")
        buf.write("\2\u00d9\u00da\7q\2\2\u00da\u00de\3\2\2\2\u00db\u00dd")
        buf.write("\t\6\2\2\u00dc\u00db\3\2\2\2\u00dd\u00e0\3\2\2\2\u00de")
        buf.write("\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00eb\3\2\2\2")
        buf.write("\u00e0\u00de\3\2\2\2\u00e1\u00e2\7\62\2\2\u00e2\u00e3")
        buf.write("\7Q\2\2\u00e3\u00e7\3\2\2\2\u00e4\u00e6\t\6\2\2\u00e5")
        buf.write("\u00e4\3\2\2\2\u00e6\u00e9\3\2\2\2\u00e7\u00e5\3\2\2\2")
        buf.write("\u00e7\u00e8\3\2\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3")
        buf.write("\2\2\2\u00ea\u00b2\3\2\2\2\u00ea\u00b9\3\2\2\2\u00ea\u00ba")
        buf.write("\3\2\2\2\u00ea\u00c9\3\2\2\2\u00ea\u00d8\3\2\2\2\u00ea")
        buf.write("\u00e1\3\2\2\2\u00eb\b\3\2\2\2\u00ec\u00ee\5\3\2\2\u00ed")
        buf.write("\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef\u00ed\3\2\2\2")
        buf.write("\u00ef\u00f0\3\2\2\2\u00f0\u00f1\3\2\2\2\u00f1\u00f6\5")
        buf.write("S*\2\u00f2\u00f5\5\3\2\2\u00f3\u00f5\5\5\3\2\u00f4\u00f2")
        buf.write("\3\2\2\2\u00f4\u00f3\3\2\2\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f4\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u0110\3\2\2\2")
        buf.write("\u00f8\u00f6\3\2\2\2\u00f9\u00fb\5\3\2\2\u00fa\u00f9\3")
        buf.write("\2\2\2\u00fb\u00fe\3\2\2\2\u00fc\u00fa\3\2\2\2\u00fc\u00fd")
        buf.write("\3\2\2\2\u00fd\u00ff\3\2\2\2\u00fe\u00fc\3\2\2\2\u00ff")
        buf.write("\u0101\5S*\2\u0100\u0102\5\3\2\2\u0101\u0100\3\2\2\2\u0102")
        buf.write("\u0103\3\2\2\2\u0103\u0101\3\2\2\2\u0103\u0104\3\2\2\2")
        buf.write("\u0104\u0106\3\2\2\2\u0105\u0107\5\5\3\2\u0106\u0105\3")
        buf.write("\2\2\2\u0106\u0107\3\2\2\2\u0107\u0110\3\2\2\2\u0108\u010a")
        buf.write("\5\3\2\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2\2\2\u010b")
        buf.write("\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\u010e\5\5\3\2\u010e\u0110\3\2\2\2\u010f\u00ed\3")
        buf.write("\2\2\2\u010f\u00fc\3\2\2\2\u010f\u0109\3\2\2\2\u0110\n")
        buf.write("\3\2\2\2\u0111\u0114\5e\63\2\u0112\u0114\5g\64\2\u0113")
        buf.write("\u0111\3\2\2\2\u0113\u0112\3\2\2\2\u0114\f\3\2\2\2\u0115")
        buf.write("\u0119\7$\2\2\u0116\u0118\5\u009dO\2\u0117\u0116\3\2\2")
        buf.write("\2\u0118\u011b\3\2\2\2\u0119\u0117\3\2\2\2\u0119\u011a")
        buf.write("\3\2\2\2\u011a\u011c\3\2\2\2\u011b\u0119\3\2\2\2\u011c")
        buf.write("\u011d\7$\2\2\u011d\u011e\b\7\2\2\u011e\16\3\2\2\2\u011f")
        buf.write("\u0123\7,\2\2\u0120\u0122\n\7\2\2\u0121\u0120\3\2\2\2")
        buf.write("\u0122\u0125\3\2\2\2\u0123\u0121\3\2\2\2\u0123\u0124\3")
        buf.write("\2\2\2\u0124\u0126\3\2\2\2\u0125\u0123\3\2\2\2\u0126\u0127")
        buf.write("\b\b\3\2\u0127\20\3\2\2\2\u0128\u0129\7,\2\2\u0129\u012d")
        buf.write("\7,\2\2\u012a\u012c\13\2\2\2\u012b\u012a\3\2\2\2\u012c")
        buf.write("\u012f\3\2\2\2\u012d\u012e\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012e\u0130\3\2\2\2\u012f\u012d\3\2\2\2\u0130\u0131\7")
        buf.write(",\2\2\u0131\u0132\7,\2\2\u0132\u0133\3\2\2\2\u0133\u0134")
        buf.write("\b\t\3\2\u0134\22\3\2\2\2\u0135\u0136\7-\2\2\u0136\24")
        buf.write("\3\2\2\2\u0137\u0138\7/\2\2\u0138\26\3\2\2\2\u0139\u013a")
        buf.write("\7,\2\2\u013a\30\3\2\2\2\u013b\u013c\7\61\2\2\u013c\32")
        buf.write("\3\2\2\2\u013d\u013e\7\'\2\2\u013e\34\3\2\2\2\u013f\u0140")
        buf.write("\7#\2\2\u0140\36\3\2\2\2\u0141\u0142\7(\2\2\u0142\u0143")
        buf.write("\7(\2\2\u0143 \3\2\2\2\u0144\u0145\7~\2\2\u0145\u0146")
        buf.write("\7~\2\2\u0146\"\3\2\2\2\u0147\u0148\7?\2\2\u0148$\3\2")
        buf.write("\2\2\u0149\u014a\7>\2\2\u014a\u014b\7?\2\2\u014b&\3\2")
        buf.write("\2\2\u014c\u014d\7@\2\2\u014d\u014e\7?\2\2\u014e(\3\2")
        buf.write("\2\2\u014f\u0150\7#\2\2\u0150\u0151\7?\2\2\u0151*\3\2")
        buf.write("\2\2\u0152\u0153\7?\2\2\u0153\u0154\7?\2\2\u0154,\3\2")
        buf.write("\2\2\u0155\u0156\7>\2\2\u0156.\3\2\2\2\u0157\u0158\7@")
        buf.write("\2\2\u0158\60\3\2\2\2\u0159\u015a\7-\2\2\u015a\u015b\7")
        buf.write("\60\2\2\u015b\62\3\2\2\2\u015c\u015d\7/\2\2\u015d\u015e")
        buf.write("\7\60\2\2\u015e\64\3\2\2\2\u015f\u0160\7,\2\2\u0160\u0161")
        buf.write("\7\60\2\2\u0161\66\3\2\2\2\u0162\u0163\7\61\2\2\u0163")
        buf.write("\u0164\7\60\2\2\u01648\3\2\2\2\u0165\u0166\7>\2\2\u0166")
        buf.write("\u0167\7?\2\2\u0167\u0168\7\60\2\2\u0168:\3\2\2\2\u0169")
        buf.write("\u016a\7@\2\2\u016a\u016b\7?\2\2\u016b\u016c\7\60\2\2")
        buf.write("\u016c<\3\2\2\2\u016d\u016e\7?\2\2\u016e\u016f\7\61\2")
        buf.write("\2\u016f\u0170\7?\2\2\u0170>\3\2\2\2\u0171\u0172\7?\2")
        buf.write("\2\u0172\u0173\7\60\2\2\u0173@\3\2\2\2\u0174\u0175\7>")
        buf.write("\2\2\u0175\u0176\7\60\2\2\u0176B\3\2\2\2\u0177\u0178\7")
        buf.write("@\2\2\u0178\u0179\7\60\2\2\u0179D\3\2\2\2\u017a\u017c")
        buf.write("\t\b\2\2\u017b\u017a\3\2\2\2\u017c\u017d\3\2\2\2\u017d")
        buf.write("\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e\u017f\3\2\2\2")
        buf.write("\u017f\u0180\b#\3\2\u0180F\3\2\2\2\u0181\u0182\7*\2\2")
        buf.write("\u0182H\3\2\2\2\u0183\u0184\7+\2\2\u0184J\3\2\2\2\u0185")
        buf.write("\u0186\7}\2\2\u0186L\3\2\2\2\u0187\u0188\7\177\2\2\u0188")
        buf.write("N\3\2\2\2\u0189\u018a\7]\2\2\u018aP\3\2\2\2\u018b\u018c")
        buf.write("\7_\2\2\u018cR\3\2\2\2\u018d\u018e\7\60\2\2\u018eT\3\2")
        buf.write("\2\2\u018f\u0190\7=\2\2\u0190V\3\2\2\2\u0191\u0192\7.")
        buf.write("\2\2\u0192X\3\2\2\2\u0193\u0194\7<\2\2\u0194Z\3\2\2\2")
        buf.write("\u0195\u0196\7H\2\2\u0196\u0197\7w\2\2\u0197\u0198\7p")
        buf.write("\2\2\u0198\u0199\7e\2\2\u0199\u019a\7v\2\2\u019a\u019b")
        buf.write("\7k\2\2\u019b\u019c\7q\2\2\u019c\u019d\7p\2\2\u019d\\")
        buf.write("\3\2\2\2\u019e\u019f\7D\2\2\u019f\u01a0\7g\2\2\u01a0\u01a1")
        buf.write("\7i\2\2\u01a1\u01a2\7k\2\2\u01a2\u01a3\7p\2\2\u01a3^\3")
        buf.write("\2\2\2\u01a4\u01a5\7D\2\2\u01a5\u01a6\7q\2\2\u01a6\u01a7")
        buf.write("\7f\2\2\u01a7\u01a8\7{\2\2\u01a8`\3\2\2\2\u01a9\u01aa")
        buf.write("\7G\2\2\u01aa\u01ab\7p\2\2\u01ab\u01ac\7f\2\2\u01acb\3")
        buf.write("\2\2\2\u01ad\u01ae\7R\2\2\u01ae\u01af\7c\2\2\u01af\u01b0")
        buf.write("\7t\2\2\u01b0\u01b1\7c\2\2\u01b1\u01b2\7o\2\2\u01b2\u01b3")
        buf.write("\7g\2\2\u01b3\u01b4\7v\2\2\u01b4\u01b5\7g\2\2\u01b5\u01b6")
        buf.write("\7t\2\2\u01b6d\3\2\2\2\u01b7\u01b8\7V\2\2\u01b8\u01b9")
        buf.write("\7t\2\2\u01b9\u01ba\7w\2\2\u01ba\u01bb\7g\2\2\u01bbf\3")
        buf.write("\2\2\2\u01bc\u01bd\7H\2\2\u01bd\u01be\7c\2\2\u01be\u01bf")
        buf.write("\7n\2\2\u01bf\u01c0\7u\2\2\u01c0\u01c1\7g\2\2\u01c1h\3")
        buf.write("\2\2\2\u01c2\u01c3\7K\2\2\u01c3\u01c4\7h\2\2\u01c4j\3")
        buf.write("\2\2\2\u01c5\u01c6\7V\2\2\u01c6\u01c7\7j\2\2\u01c7\u01c8")
        buf.write("\7g\2\2\u01c8\u01c9\7p\2\2\u01c9l\3\2\2\2\u01ca\u01cb")
        buf.write("\7G\2\2\u01cb\u01cc\7n\2\2\u01cc\u01cd\7u\2\2\u01cd\u01ce")
        buf.write("\7g\2\2\u01cen\3\2\2\2\u01cf\u01d0\7G\2\2\u01d0\u01d1")
        buf.write("\7n\2\2\u01d1\u01d2\7u\2\2\u01d2\u01d3\7g\2\2\u01d3\u01d4")
        buf.write("\7K\2\2\u01d4\u01d5\7h\2\2\u01d5p\3\2\2\2\u01d6\u01d7")
        buf.write("\7G\2\2\u01d7\u01d8\7p\2\2\u01d8\u01d9\7f\2\2\u01d9\u01da")
        buf.write("\7k\2\2\u01da\u01db\7h\2\2\u01dbr\3\2\2\2\u01dc\u01dd")
        buf.write("\7G\2\2\u01dd\u01de\7p\2\2\u01de\u01df\7f\2\2\u01df\u01e0")
        buf.write("\7F\2\2\u01e0\u01e1\7q\2\2\u01e1t\3\2\2\2\u01e2\u01e3")
        buf.write("\7G\2\2\u01e3\u01e4\7p\2\2\u01e4\u01e5\7f\2\2\u01e5\u01e6")
        buf.write("\7D\2\2\u01e6\u01e7\7q\2\2\u01e7\u01e8\7f\2\2\u01e8\u01e9")
        buf.write("\7{\2\2\u01e9v\3\2\2\2\u01ea\u01eb\7H\2\2\u01eb\u01ec")
        buf.write("\7q\2\2\u01ec\u01ed\7t\2\2\u01edx\3\2\2\2\u01ee\u01ef")
        buf.write("\7Y\2\2\u01ef\u01f0\7j\2\2\u01f0\u01f1\7k\2\2\u01f1\u01f2")
        buf.write("\7n\2\2\u01f2\u01f3\7g\2\2\u01f3z\3\2\2\2\u01f4\u01f5")
        buf.write("\7F\2\2\u01f5\u01f6\7q\2\2\u01f6|\3\2\2\2\u01f7\u01f8")
        buf.write("\7V\2\2\u01f8\u01f9\7q\2\2\u01f9~\3\2\2\2\u01fa\u01fb")
        buf.write("\7G\2\2\u01fb\u01fc\7p\2\2\u01fc\u01fd\7f\2\2\u01fd\u01fe")
        buf.write("\7H\2\2\u01fe\u01ff\7q\2\2\u01ff\u0200\7t\2\2\u0200\u0080")
        buf.write("\3\2\2\2\u0201\u0202\7G\2\2\u0202\u0203\7p\2\2\u0203\u0204")
        buf.write("\7f\2\2\u0204\u0205\7Y\2\2\u0205\u0206\7j\2\2\u0206\u0207")
        buf.write("\7k\2\2\u0207\u0208\7n\2\2\u0208\u0209\7g\2\2\u0209\u0082")
        buf.write("\3\2\2\2\u020a\u020b\7t\2\2\u020b\u020c\7g\2\2\u020c\u020d")
        buf.write("\7v\2\2\u020d\u020e\7w\2\2\u020e\u020f\7t\2\2\u020f\u0210")
        buf.write("\7p\2\2\u0210\u0084\3\2\2\2\u0211\u0212\7d\2\2\u0212\u0213")
        buf.write("\7t\2\2\u0213\u0214\7g\2\2\u0214\u0215\7c\2\2\u0215\u0216")
        buf.write("\7m\2\2\u0216\u0086\3\2\2\2\u0217\u0218\7e\2\2\u0218\u0219")
        buf.write("\7q\2\2\u0219\u021a\7p\2\2\u021a\u021b\7v\2\2\u021b\u021c")
        buf.write("\7k\2\2\u021c\u021d\7p\2\2\u021d\u021e\7w\2\2\u021e\u021f")
        buf.write("\7g\2\2\u021f\u0088\3\2\2\2\u0220\u0221\7k\2\2\u0221\u0222")
        buf.write("\7p\2\2\u0222\u0223\7v\2\2\u0223\u008a\3\2\2\2\u0224\u0225")
        buf.write("\7u\2\2\u0225\u0226\7v\2\2\u0226\u0227\7t\2\2\u0227\u0228")
        buf.write("\7k\2\2\u0228\u0229\7p\2\2\u0229\u022a\7i\2\2\u022a\u008c")
        buf.write("\3\2\2\2\u022b\u022c\7h\2\2\u022c\u022d\7n\2\2\u022d\u022e")
        buf.write("\7q\2\2\u022e\u022f\7c\2\2\u022f\u0230\7v\2\2\u0230\u008e")
        buf.write("\3\2\2\2\u0231\u0232\7d\2\2\u0232\u0233\7q\2\2\u0233\u0234")
        buf.write("\7q\2\2\u0234\u0235\7n\2\2\u0235\u0236\7g\2\2\u0236\u0237")
        buf.write("\7c\2\2\u0237\u0238\7p\2\2\u0238\u0090\3\2\2\2\u0239\u023a")
        buf.write("\7X\2\2\u023a\u023b\7c\2\2\u023b\u023c\7t\2\2\u023c\u0092")
        buf.write("\3\2\2\2\u023d\u023e\7q\2\2\u023e\u023f\7h\2\2\u023f\u0094")
        buf.write("\3\2\2\2\u0240\u0241\7c\2\2\u0241\u0242\7t\2\2\u0242\u0243")
        buf.write("\7t\2\2\u0243\u0244\7c\2\2\u0244\u0245\7{\2\2\u0245\u0096")
        buf.write("\3\2\2\2\u0246\u024a\t\t\2\2\u0247\u0249\t\n\2\2\u0248")
        buf.write("\u0247\3\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248\3\2\2\2")
        buf.write("\u024a\u024b\3\2\2\2\u024b\u0098\3\2\2\2\u024c\u024a\3")
        buf.write("\2\2\2\u024d\u0251\7$\2\2\u024e\u0250\5\u009dO\2\u024f")
        buf.write("\u024e\3\2\2\2\u0250\u0253\3\2\2\2\u0251\u024f\3\2\2\2")
        buf.write("\u0251\u0252\3\2\2\2\u0252\u0255\3\2\2\2\u0253\u0251\3")
        buf.write("\2\2\2\u0254\u0256\t\13\2\2\u0255\u0254\3\2\2\2\u0256")
        buf.write("\u0257\3\2\2\2\u0257\u0258\bM\4\2\u0258\u009a\3\2\2\2")
        buf.write("\u0259\u025d\7$\2\2\u025a\u025c\5\u009dO\2\u025b\u025a")
        buf.write("\3\2\2\2\u025c\u025f\3\2\2\2\u025d\u025b\3\2\2\2\u025d")
        buf.write("\u025e\3\2\2\2\u025e\u0260\3\2\2\2\u025f\u025d\3\2\2\2")
        buf.write("\u0260\u0261\5\u00a1Q\2\u0261\u0262\bN\5\2\u0262\u009c")
        buf.write("\3\2\2\2\u0263\u0266\n\f\2\2\u0264\u0266\5\u009fP\2\u0265")
        buf.write("\u0263\3\2\2\2\u0265\u0264\3\2\2\2\u0266\u009e\3\2\2\2")
        buf.write("\u0267\u0268\7^\2\2\u0268\u0269\t\r\2\2\u0269\u00a0\3")
        buf.write("\2\2\2\u026a\u026b\7^\2\2\u026b\u026e\n\r\2\2\u026c\u026e")
        buf.write("\n\16\2\2\u026d\u026a\3\2\2\2\u026d\u026c\3\2\2\2\u026e")
        buf.write("\u00a2\3\2\2\2\u026f\u0270\13\2\2\2\u0270\u0271\bR\6\2")
        buf.write("\u0271\u00a4\3\2\2\2\u0272\u0273\13\2\2\2\u0273\u00a6")
        buf.write("\3\2\2\2 \2\u00ab\u00b0\u00b6\u00c0\u00c6\u00cf\u00d5")
        buf.write("\u00de\u00e7\u00ea\u00ef\u00f4\u00f6\u00fc\u0103\u0106")
        buf.write("\u010b\u010f\u0113\u0119\u0123\u012d\u017d\u024a\u0251")
        buf.write("\u0255\u025d\u0265\u026d\7\3\7\2\b\2\2\3M\3\3N\4\3R\5")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    INTEGER_LITERAL = 1
    FLOAT_LITERAL = 2
    BOOLEAN_LITERAL = 3
    STRING_LITERAL = 4
    CMTLINE = 5
    CMTBLOCK = 6
    ADD = 7
    SUB = 8
    MUL = 9
    DIV = 10
    MOD = 11
    NOT = 12
    AND = 13
    OR = 14
    ASSIGN = 15
    LTE = 16
    GTE = 17
    NEQ = 18
    EQ = 19
    LT = 20
    GT = 21
    FADD = 22
    FSUB = 23
    FMUL = 24
    FDIV = 25
    FLTE = 26
    FGTE = 27
    FNEQ = 28
    FEQ = 29
    FLT = 30
    FGT = 31
    WS = 32
    LP = 33
    RP = 34
    LCB = 35
    RCB = 36
    LSB = 37
    RSB = 38
    DOT = 39
    SEMI = 40
    COMMA = 41
    COLON = 42
    FUNCTION = 43
    BEGIN = 44
    BODY = 45
    END = 46
    PARAMETER = 47
    TRUE = 48
    FALSE = 49
    IF = 50
    THEN = 51
    ELSE = 52
    ELSEIF = 53
    ENDIF = 54
    ENDDO = 55
    ENDBODY = 56
    FOR = 57
    WHILE = 58
    DO = 59
    TO = 60
    ENDFOR = 61
    ENDWHILE = 62
    RETURN = 63
    BREAK = 64
    CONTINUE = 65
    INTEGER = 66
    STRING = 67
    FLOAT = 68
    BOOLEAN = 69
    VAR = 70
    OF = 71
    ARRAY = 72
    ID = 73
    UNCLOSE_STRING = 74
    ILLEGAL_ESCAPE = 75
    ERROR_CHAR = 76
    UNTERMINATED_COMMENT = 77

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'!'", "'&&'", "'||'", "'='", 
            "'<='", "'>='", "'!='", "'=='", "'<'", "'>'", "'+.'", "'-.'", 
            "'*.'", "'/.'", "'<=.'", "'>=.'", "'=/='", "'=.'", "'<.'", "'>.'", 
            "'('", "')'", "'{'", "'}'", "'['", "']'", "'.'", "';'", "','", 
            "':'", "'Function'", "'Begin'", "'Body'", "'End'", "'Parameter'", 
            "'True'", "'False'", "'If'", "'Then'", "'Else'", "'ElseIf'", 
            "'Endif'", "'EndDo'", "'EndBody'", "'For'", "'While'", "'Do'", 
            "'To'", "'EndFor'", "'EndWhile'", "'return'", "'break'", "'continue'", 
            "'int'", "'string'", "'float'", "'boolean'", "'Var'", "'of'", 
            "'array'" ]

    symbolicNames = [ "<INVALID>",
            "INTEGER_LITERAL", "FLOAT_LITERAL", "BOOLEAN_LITERAL", "STRING_LITERAL", 
            "CMTLINE", "CMTBLOCK", "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", 
            "AND", "OR", "ASSIGN", "LTE", "GTE", "NEQ", "EQ", "LT", "GT", 
            "FADD", "FSUB", "FMUL", "FDIV", "FLTE", "FGTE", "FNEQ", "FEQ", 
            "FLT", "FGT", "WS", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
            "DOT", "SEMI", "COMMA", "COLON", "FUNCTION", "BEGIN", "BODY", 
            "END", "PARAMETER", "TRUE", "FALSE", "IF", "THEN", "ELSE", "ELSEIF", 
            "ENDIF", "ENDDO", "ENDBODY", "FOR", "WHILE", "DO", "TO", "ENDFOR", 
            "ENDWHILE", "RETURN", "BREAK", "CONTINUE", "INTEGER", "STRING", 
            "FLOAT", "BOOLEAN", "VAR", "OF", "ARRAY", "ID", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "DIGIT", "EXPONENT", "INTEGER_LITERAL", "FLOAT_LITERAL", 
                  "BOOLEAN_LITERAL", "STRING_LITERAL", "CMTLINE", "CMTBLOCK", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "NOT", "AND", "OR", 
                  "ASSIGN", "LTE", "GTE", "NEQ", "EQ", "LT", "GT", "FADD", 
                  "FSUB", "FMUL", "FDIV", "FLTE", "FGTE", "FNEQ", "FEQ", 
                  "FLT", "FGT", "WS", "LP", "RP", "LCB", "RCB", "LSB", "RSB", 
                  "DOT", "SEMI", "COMMA", "COLON", "FUNCTION", "BEGIN", 
                  "BODY", "END", "PARAMETER", "TRUE", "FALSE", "IF", "THEN", 
                  "ELSE", "ELSEIF", "ENDIF", "ENDDO", "ENDBODY", "FOR", 
                  "WHILE", "DO", "TO", "ENDFOR", "ENDWHILE", "RETURN", "BREAK", 
                  "CONTINUE", "INTEGER", "STRING", "FLOAT", "BOOLEAN", "VAR", 
                  "OF", "ARRAY", "ID", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "STR_CHAR", "ESC_SEQ", "ESC_ILLEGAL", "ERROR_CHAR", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            return super().emit();


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[5] = self.STRING_LITERAL_action 
            actions[75] = self.UNCLOSE_STRING_action 
            actions[76] = self.ILLEGAL_ESCAPE_action 
            actions[80] = self.ERROR_CHAR_action 
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
            		possible = ['\b', '\t', '\n', '\f', '\r', '"', "'", '\\']
            		if y[-1] in possible:
            			raise UncloseString(y[1:-1])
            		else:
            			raise UncloseString(y[1:])
            	
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

            		y = str(self.text)
            		raise IllegalEscape(y[1:])
            	
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

            		raise ErrorToken(self.text)
            	
     



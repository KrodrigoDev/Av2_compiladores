# Generated from ScalarProduct.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,18,146,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,4,0,32,8,0,11,0,12,0,33,1,1,1,1,1,1,1,1,1,1,1,2,1,
        2,1,2,1,2,4,2,45,8,2,11,2,12,2,46,1,3,1,3,1,3,1,3,3,3,53,8,3,1,3,
        1,3,1,3,1,3,1,4,1,4,1,4,5,4,62,8,4,10,4,12,4,65,9,4,1,5,1,5,1,5,
        3,5,70,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,3,7,79,8,7,1,7,1,7,1,8,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,91,8,9,10,9,12,9,94,9,9,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,3,10,104,8,10,1,10,1,10,1,10,5,10,
        109,8,10,10,10,12,10,112,9,10,1,11,1,11,3,11,116,8,11,1,11,1,11,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,13,
        1,13,1,13,3,13,135,8,13,1,13,1,13,1,14,3,14,140,8,14,1,14,1,14,3,
        14,144,8,14,1,14,0,1,20,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,0,0,151,0,31,1,0,0,0,2,35,1,0,0,0,4,44,1,0,0,0,6,48,1,0,0,0,8,
        58,1,0,0,0,10,66,1,0,0,0,12,71,1,0,0,0,14,75,1,0,0,0,16,82,1,0,0,
        0,18,87,1,0,0,0,20,103,1,0,0,0,22,113,1,0,0,0,24,119,1,0,0,0,26,
        131,1,0,0,0,28,139,1,0,0,0,30,32,3,2,1,0,31,30,1,0,0,0,32,33,1,0,
        0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,1,1,0,0,0,35,36,5,1,0,0,36,37,
        5,15,0,0,37,38,5,12,0,0,38,39,3,4,2,0,39,3,1,0,0,0,40,45,3,6,3,0,
        41,45,3,12,6,0,42,45,3,14,7,0,43,45,3,16,8,0,44,40,1,0,0,0,44,41,
        1,0,0,0,44,42,1,0,0,0,44,43,1,0,0,0,45,46,1,0,0,0,46,44,1,0,0,0,
        46,47,1,0,0,0,47,5,1,0,0,0,48,49,5,2,0,0,49,50,5,15,0,0,50,52,5,
        8,0,0,51,53,3,8,4,0,52,51,1,0,0,0,52,53,1,0,0,0,53,54,1,0,0,0,54,
        55,5,9,0,0,55,56,5,12,0,0,56,57,3,4,2,0,57,7,1,0,0,0,58,63,3,10,
        5,0,59,60,5,13,0,0,60,62,3,10,5,0,61,59,1,0,0,0,62,65,1,0,0,0,63,
        61,1,0,0,0,63,64,1,0,0,0,64,9,1,0,0,0,65,63,1,0,0,0,66,69,5,15,0,
        0,67,68,5,12,0,0,68,70,5,15,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,11,
        1,0,0,0,71,72,5,15,0,0,72,73,5,5,0,0,73,74,3,20,10,0,74,13,1,0,0,
        0,75,76,5,15,0,0,76,78,5,8,0,0,77,79,3,18,9,0,78,77,1,0,0,0,78,79,
        1,0,0,0,79,80,1,0,0,0,80,81,5,9,0,0,81,15,1,0,0,0,82,83,5,4,0,0,
        83,84,5,8,0,0,84,85,3,20,10,0,85,86,5,9,0,0,86,17,1,0,0,0,87,92,
        3,20,10,0,88,89,5,13,0,0,89,91,3,20,10,0,90,88,1,0,0,0,91,94,1,0,
        0,0,92,90,1,0,0,0,92,93,1,0,0,0,93,19,1,0,0,0,94,92,1,0,0,0,95,96,
        6,10,-1,0,96,104,5,15,0,0,97,104,3,26,13,0,98,104,5,16,0,0,99,104,
        3,22,11,0,100,104,3,14,7,0,101,104,5,17,0,0,102,104,3,24,12,0,103,
        95,1,0,0,0,103,97,1,0,0,0,103,98,1,0,0,0,103,99,1,0,0,0,103,100,
        1,0,0,0,103,101,1,0,0,0,103,102,1,0,0,0,104,110,1,0,0,0,105,106,
        10,8,0,0,106,107,5,14,0,0,107,109,3,20,10,9,108,105,1,0,0,0,109,
        112,1,0,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,21,1,0,0,0,112,110,
        1,0,0,0,113,115,5,10,0,0,114,116,3,18,9,0,115,114,1,0,0,0,115,116,
        1,0,0,0,116,117,1,0,0,0,117,118,5,11,0,0,118,23,1,0,0,0,119,120,
        5,10,0,0,120,121,3,20,10,0,121,122,5,14,0,0,122,123,3,20,10,0,123,
        124,5,6,0,0,124,125,5,15,0,0,125,126,5,13,0,0,126,127,5,15,0,0,127,
        128,5,7,0,0,128,129,3,14,7,0,129,130,5,11,0,0,130,25,1,0,0,0,131,
        132,5,15,0,0,132,134,5,10,0,0,133,135,3,28,14,0,134,133,1,0,0,0,
        134,135,1,0,0,0,135,136,1,0,0,0,136,137,5,11,0,0,137,27,1,0,0,0,
        138,140,5,16,0,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,
        141,143,5,12,0,0,142,144,5,16,0,0,143,142,1,0,0,0,143,144,1,0,0,
        0,144,29,1,0,0,0,14,33,44,46,52,63,69,78,92,103,110,115,134,139,
        143
    ]

class ScalarProductParser ( Parser ):

    grammarFileName = "ScalarProduct.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'def'", "'return'", "'print'", 
                     "'='", "'for'", "'in'", "'('", "')'", "'['", "']'", 
                     "':'", "','" ]

    symbolicNames = [ "<INVALID>", "CLASSE", "FUNC", "RETORNAR", "IMPRIMIR", 
                      "NOVO", "PARA", "EM", "ABRE_PARENTESES", "FECHA_PARENTESES", 
                      "ABRE_COLCHETES", "FECHA_COLCHETES", "DOIS_PONTOS", 
                      "VIRGULA", "OPERADOR_MATEMATICO", "ID", "NUMERO", 
                      "TEXTO", "WS" ]

    RULE_programa = 0
    RULE_declaracaoClasse = 1
    RULE_bloco = 2
    RULE_declaracaoFuncao = 3
    RULE_listaParametros = 4
    RULE_parametro = 5
    RULE_atribuicao = 6
    RULE_chamadaFuncao = 7
    RULE_imprimirStatement = 8
    RULE_argumentos = 9
    RULE_expressao = 10
    RULE_listaExpressao = 11
    RULE_compreensaoLista = 12
    RULE_acessoLista = 13
    RULE_slice = 14

    ruleNames =  [ "programa", "declaracaoClasse", "bloco", "declaracaoFuncao", 
                   "listaParametros", "parametro", "atribuicao", "chamadaFuncao", 
                   "imprimirStatement", "argumentos", "expressao", "listaExpressao", 
                   "compreensaoLista", "acessoLista", "slice" ]

    EOF = Token.EOF
    CLASSE=1
    FUNC=2
    RETORNAR=3
    IMPRIMIR=4
    NOVO=5
    PARA=6
    EM=7
    ABRE_PARENTESES=8
    FECHA_PARENTESES=9
    ABRE_COLCHETES=10
    FECHA_COLCHETES=11
    DOIS_PONTOS=12
    VIRGULA=13
    OPERADOR_MATEMATICO=14
    ID=15
    NUMERO=16
    TEXTO=17
    WS=18

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracaoClasse(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScalarProductParser.DeclaracaoClasseContext)
            else:
                return self.getTypedRuleContext(ScalarProductParser.DeclaracaoClasseContext,i)


        def getRuleIndex(self):
            return ScalarProductParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = ScalarProductParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 30
                self.declaracaoClasse()
                self.state = 33 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoClasseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASSE(self):
            return self.getToken(ScalarProductParser.CLASSE, 0)

        def ID(self):
            return self.getToken(ScalarProductParser.ID, 0)

        def DOIS_PONTOS(self):
            return self.getToken(ScalarProductParser.DOIS_PONTOS, 0)

        def bloco(self):
            return self.getTypedRuleContext(ScalarProductParser.BlocoContext,0)


        def getRuleIndex(self):
            return ScalarProductParser.RULE_declaracaoClasse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoClasse" ):
                listener.enterDeclaracaoClasse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoClasse" ):
                listener.exitDeclaracaoClasse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracaoClasse" ):
                return visitor.visitDeclaracaoClasse(self)
            else:
                return visitor.visitChildren(self)




    def declaracaoClasse(self):

        localctx = ScalarProductParser.DeclaracaoClasseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracaoClasse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(ScalarProductParser.CLASSE)
            self.state = 36
            self.match(ScalarProductParser.ID)
            self.state = 37
            self.match(ScalarProductParser.DOIS_PONTOS)
            self.state = 38
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracaoFuncao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScalarProductParser.DeclaracaoFuncaoContext)
            else:
                return self.getTypedRuleContext(ScalarProductParser.DeclaracaoFuncaoContext,i)


        def atribuicao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScalarProductParser.AtribuicaoContext)
            else:
                return self.getTypedRuleContext(ScalarProductParser.AtribuicaoContext,i)


        def chamadaFuncao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScalarProductParser.ChamadaFuncaoContext)
            else:
                return self.getTypedRuleContext(ScalarProductParser.ChamadaFuncaoContext,i)


        def imprimirStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScalarProductParser.ImprimirStatementContext)
            else:
                return self.getTypedRuleContext(ScalarProductParser.ImprimirStatementContext,i)


        def getRuleIndex(self):
            return ScalarProductParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloco" ):
                return visitor.visitBloco(self)
            else:
                return visitor.visitChildren(self)




    def bloco(self):

        localctx = ScalarProductParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_bloco)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                    if la_ == 1:
                        self.state = 40
                        self.declaracaoFuncao()
                        pass

                    elif la_ == 2:
                        self.state = 41
                        self.atribuicao()
                        pass

                    elif la_ == 3:
                        self.state = 42
                        self.chamadaFuncao()
                        pass

                    elif la_ == 4:
                        self.state = 43
                        self.imprimirStatement()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 46 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracaoFuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(ScalarProductParser.FUNC, 0)

        def ID(self):
            return self.getToken(ScalarProductParser.ID, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(ScalarProductParser.ABRE_PARENTESES, 0)

        def FECHA_PARENTESES(self):
            return self.getToken(ScalarProductParser.FECHA_PARENTESES, 0)

        def DOIS_PONTOS(self):
            return self.getToken(ScalarProductParser.DOIS_PONTOS, 0)

        def bloco(self):
            return self.getTypedRuleContext(ScalarProductParser.BlocoContext,0)


        def listaParametros(self):
            return self.getTypedRuleContext(ScalarProductParser.ListaParametrosContext,0)


        def getRuleIndex(self):
            return ScalarProductParser.RULE_declaracaoFuncao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracaoFuncao" ):
                listener.enterDeclaracaoFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracaoFuncao" ):
                listener.exitDeclaracaoFuncao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracaoFuncao" ):
                return visitor.visitDeclaracaoFuncao(self)
            else:
                return visitor.visitChildren(self)




    def declaracaoFuncao(self):

        localctx = ScalarProductParser.DeclaracaoFuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaracaoFuncao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.match(ScalarProductParser.FUNC)
            self.state = 49
            self.match(ScalarProductParser.ID)
            self.state = 50
            self.match(ScalarProductParser.ABRE_PARENTESES)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 51
                self.listaParametros()


            self.state = 54
            self.match(ScalarProductParser.FECHA_PARENTESES)
            self.state = 55
            self.match(ScalarProductParser.DOIS_PONTOS)
            self.state = 56
            self.bloco()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaParametrosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parametro(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScalarProductParser.ParametroContext)
            else:
                return self.getTypedRuleContext(ScalarProductParser.ParametroContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(ScalarProductParser.VIRGULA)
            else:
                return self.getToken(ScalarProductParser.VIRGULA, i)

        def getRuleIndex(self):
            return ScalarProductParser.RULE_listaParametros

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaParametros" ):
                listener.enterListaParametros(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaParametros" ):
                listener.exitListaParametros(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaParametros" ):
                return visitor.visitListaParametros(self)
            else:
                return visitor.visitChildren(self)




    def listaParametros(self):

        localctx = ScalarProductParser.ListaParametrosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listaParametros)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.parametro()
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 59
                self.match(ScalarProductParser.VIRGULA)
                self.state = 60
                self.parametro()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametroContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ScalarProductParser.ID)
            else:
                return self.getToken(ScalarProductParser.ID, i)

        def DOIS_PONTOS(self):
            return self.getToken(ScalarProductParser.DOIS_PONTOS, 0)

        def getRuleIndex(self):
            return ScalarProductParser.RULE_parametro

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParametro" ):
                listener.enterParametro(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParametro" ):
                listener.exitParametro(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParametro" ):
                return visitor.visitParametro(self)
            else:
                return visitor.visitChildren(self)




    def parametro(self):

        localctx = ScalarProductParser.ParametroContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_parametro)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(ScalarProductParser.ID)
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 67
                self.match(ScalarProductParser.DOIS_PONTOS)
                self.state = 68
                self.match(ScalarProductParser.ID)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AtribuicaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ScalarProductParser.ID, 0)

        def NOVO(self):
            return self.getToken(ScalarProductParser.NOVO, 0)

        def expressao(self):
            return self.getTypedRuleContext(ScalarProductParser.ExpressaoContext,0)


        def getRuleIndex(self):
            return ScalarProductParser.RULE_atribuicao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtribuicao" ):
                listener.enterAtribuicao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtribuicao" ):
                listener.exitAtribuicao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAtribuicao" ):
                return visitor.visitAtribuicao(self)
            else:
                return visitor.visitChildren(self)




    def atribuicao(self):

        localctx = ScalarProductParser.AtribuicaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atribuicao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ScalarProductParser.ID)
            self.state = 72
            self.match(ScalarProductParser.NOVO)
            self.state = 73
            self.expressao(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ChamadaFuncaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ScalarProductParser.ID, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(ScalarProductParser.ABRE_PARENTESES, 0)

        def FECHA_PARENTESES(self):
            return self.getToken(ScalarProductParser.FECHA_PARENTESES, 0)

        def argumentos(self):
            return self.getTypedRuleContext(ScalarProductParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return ScalarProductParser.RULE_chamadaFuncao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterChamadaFuncao" ):
                listener.enterChamadaFuncao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitChamadaFuncao" ):
                listener.exitChamadaFuncao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitChamadaFuncao" ):
                return visitor.visitChamadaFuncao(self)
            else:
                return visitor.visitChildren(self)




    def chamadaFuncao(self):

        localctx = ScalarProductParser.ChamadaFuncaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_chamadaFuncao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(ScalarProductParser.ID)

            self.state = 76
            self.match(ScalarProductParser.ABRE_PARENTESES)
            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 230400) != 0):
                self.state = 77
                self.argumentos()


            self.state = 80
            self.match(ScalarProductParser.FECHA_PARENTESES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImprimirStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPRIMIR(self):
            return self.getToken(ScalarProductParser.IMPRIMIR, 0)

        def ABRE_PARENTESES(self):
            return self.getToken(ScalarProductParser.ABRE_PARENTESES, 0)

        def expressao(self):
            return self.getTypedRuleContext(ScalarProductParser.ExpressaoContext,0)


        def FECHA_PARENTESES(self):
            return self.getToken(ScalarProductParser.FECHA_PARENTESES, 0)

        def getRuleIndex(self):
            return ScalarProductParser.RULE_imprimirStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImprimirStatement" ):
                listener.enterImprimirStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImprimirStatement" ):
                listener.exitImprimirStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImprimirStatement" ):
                return visitor.visitImprimirStatement(self)
            else:
                return visitor.visitChildren(self)




    def imprimirStatement(self):

        localctx = ScalarProductParser.ImprimirStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_imprimirStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(ScalarProductParser.IMPRIMIR)
            self.state = 83
            self.match(ScalarProductParser.ABRE_PARENTESES)
            self.state = 84
            self.expressao(0)
            self.state = 85
            self.match(ScalarProductParser.FECHA_PARENTESES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScalarProductParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ScalarProductParser.ExpressaoContext,i)


        def VIRGULA(self, i:int=None):
            if i is None:
                return self.getTokens(ScalarProductParser.VIRGULA)
            else:
                return self.getToken(ScalarProductParser.VIRGULA, i)

        def getRuleIndex(self):
            return ScalarProductParser.RULE_argumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentos" ):
                listener.enterArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentos" ):
                listener.exitArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentos" ):
                return visitor.visitArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def argumentos(self):

        localctx = ScalarProductParser.ArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.expressao(0)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 88
                self.match(ScalarProductParser.VIRGULA)
                self.state = 89
                self.expressao(0)
                self.state = 94
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ScalarProductParser.ID, 0)

        def acessoLista(self):
            return self.getTypedRuleContext(ScalarProductParser.AcessoListaContext,0)


        def NUMERO(self):
            return self.getToken(ScalarProductParser.NUMERO, 0)

        def listaExpressao(self):
            return self.getTypedRuleContext(ScalarProductParser.ListaExpressaoContext,0)


        def chamadaFuncao(self):
            return self.getTypedRuleContext(ScalarProductParser.ChamadaFuncaoContext,0)


        def TEXTO(self):
            return self.getToken(ScalarProductParser.TEXTO, 0)

        def compreensaoLista(self):
            return self.getTypedRuleContext(ScalarProductParser.CompreensaoListaContext,0)


        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScalarProductParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ScalarProductParser.ExpressaoContext,i)


        def OPERADOR_MATEMATICO(self):
            return self.getToken(ScalarProductParser.OPERADOR_MATEMATICO, 0)

        def getRuleIndex(self):
            return ScalarProductParser.RULE_expressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressao" ):
                listener.enterExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressao" ):
                listener.exitExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressao" ):
                return visitor.visitExpressao(self)
            else:
                return visitor.visitChildren(self)



    def expressao(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ScalarProductParser.ExpressaoContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 20
        self.enterRecursionRule(localctx, 20, self.RULE_expressao, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 96
                self.match(ScalarProductParser.ID)
                pass

            elif la_ == 2:
                self.state = 97
                self.acessoLista()
                pass

            elif la_ == 3:
                self.state = 98
                self.match(ScalarProductParser.NUMERO)
                pass

            elif la_ == 4:
                self.state = 99
                self.listaExpressao()
                pass

            elif la_ == 5:
                self.state = 100
                self.chamadaFuncao()
                pass

            elif la_ == 6:
                self.state = 101
                self.match(ScalarProductParser.TEXTO)
                pass

            elif la_ == 7:
                self.state = 102
                self.compreensaoLista()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 110
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ScalarProductParser.ExpressaoContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expressao)
                    self.state = 105
                    if not self.precpred(self._ctx, 8):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                    self.state = 106
                    self.match(ScalarProductParser.OPERADOR_MATEMATICO)
                    self.state = 107
                    self.expressao(9) 
                self.state = 112
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ListaExpressaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_COLCHETES(self):
            return self.getToken(ScalarProductParser.ABRE_COLCHETES, 0)

        def FECHA_COLCHETES(self):
            return self.getToken(ScalarProductParser.FECHA_COLCHETES, 0)

        def argumentos(self):
            return self.getTypedRuleContext(ScalarProductParser.ArgumentosContext,0)


        def getRuleIndex(self):
            return ScalarProductParser.RULE_listaExpressao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaExpressao" ):
                listener.enterListaExpressao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaExpressao" ):
                listener.exitListaExpressao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaExpressao" ):
                return visitor.visitListaExpressao(self)
            else:
                return visitor.visitChildren(self)




    def listaExpressao(self):

        localctx = ScalarProductParser.ListaExpressaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listaExpressao)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(ScalarProductParser.ABRE_COLCHETES)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 230400) != 0):
                self.state = 114
                self.argumentos()


            self.state = 117
            self.match(ScalarProductParser.FECHA_COLCHETES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompreensaoListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ABRE_COLCHETES(self):
            return self.getToken(ScalarProductParser.ABRE_COLCHETES, 0)

        def expressao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ScalarProductParser.ExpressaoContext)
            else:
                return self.getTypedRuleContext(ScalarProductParser.ExpressaoContext,i)


        def OPERADOR_MATEMATICO(self):
            return self.getToken(ScalarProductParser.OPERADOR_MATEMATICO, 0)

        def PARA(self):
            return self.getToken(ScalarProductParser.PARA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(ScalarProductParser.ID)
            else:
                return self.getToken(ScalarProductParser.ID, i)

        def VIRGULA(self):
            return self.getToken(ScalarProductParser.VIRGULA, 0)

        def EM(self):
            return self.getToken(ScalarProductParser.EM, 0)

        def chamadaFuncao(self):
            return self.getTypedRuleContext(ScalarProductParser.ChamadaFuncaoContext,0)


        def FECHA_COLCHETES(self):
            return self.getToken(ScalarProductParser.FECHA_COLCHETES, 0)

        def getRuleIndex(self):
            return ScalarProductParser.RULE_compreensaoLista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompreensaoLista" ):
                listener.enterCompreensaoLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompreensaoLista" ):
                listener.exitCompreensaoLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompreensaoLista" ):
                return visitor.visitCompreensaoLista(self)
            else:
                return visitor.visitChildren(self)




    def compreensaoLista(self):

        localctx = ScalarProductParser.CompreensaoListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_compreensaoLista)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(ScalarProductParser.ABRE_COLCHETES)
            self.state = 120
            self.expressao(0)
            self.state = 121
            self.match(ScalarProductParser.OPERADOR_MATEMATICO)
            self.state = 122
            self.expressao(0)
            self.state = 123
            self.match(ScalarProductParser.PARA)
            self.state = 124
            self.match(ScalarProductParser.ID)
            self.state = 125
            self.match(ScalarProductParser.VIRGULA)
            self.state = 126
            self.match(ScalarProductParser.ID)
            self.state = 127
            self.match(ScalarProductParser.EM)
            self.state = 128
            self.chamadaFuncao()
            self.state = 129
            self.match(ScalarProductParser.FECHA_COLCHETES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AcessoListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(ScalarProductParser.ID, 0)

        def ABRE_COLCHETES(self):
            return self.getToken(ScalarProductParser.ABRE_COLCHETES, 0)

        def FECHA_COLCHETES(self):
            return self.getToken(ScalarProductParser.FECHA_COLCHETES, 0)

        def slice_(self):
            return self.getTypedRuleContext(ScalarProductParser.SliceContext,0)


        def getRuleIndex(self):
            return ScalarProductParser.RULE_acessoLista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcessoLista" ):
                listener.enterAcessoLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcessoLista" ):
                listener.exitAcessoLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcessoLista" ):
                return visitor.visitAcessoLista(self)
            else:
                return visitor.visitChildren(self)




    def acessoLista(self):

        localctx = ScalarProductParser.AcessoListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_acessoLista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(ScalarProductParser.ID)
            self.state = 132
            self.match(ScalarProductParser.ABRE_COLCHETES)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==16:
                self.state = 133
                self.slice_()


            self.state = 136
            self.match(ScalarProductParser.FECHA_COLCHETES)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SliceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOIS_PONTOS(self):
            return self.getToken(ScalarProductParser.DOIS_PONTOS, 0)

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(ScalarProductParser.NUMERO)
            else:
                return self.getToken(ScalarProductParser.NUMERO, i)

        def getRuleIndex(self):
            return ScalarProductParser.RULE_slice

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSlice" ):
                listener.enterSlice(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSlice" ):
                listener.exitSlice(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSlice" ):
                return visitor.visitSlice(self)
            else:
                return visitor.visitChildren(self)




    def slice_(self):

        localctx = ScalarProductParser.SliceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_slice)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 138
                self.match(ScalarProductParser.NUMERO)


            self.state = 141
            self.match(ScalarProductParser.DOIS_PONTOS)
            self.state = 143
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 142
                self.match(ScalarProductParser.NUMERO)


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
        self._predicates[10] = self.expressao_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expressao_sempred(self, localctx:ExpressaoContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 8)
         





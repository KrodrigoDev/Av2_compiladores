# Generated from ScalarProduct.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ScalarProductParser import ScalarProductParser
else:
    from ScalarProductParser import ScalarProductParser

# This class defines a complete generic visitor for a parse tree produced by ScalarProductParser.

class ScalarProductVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ScalarProductParser#programa.
    def visitPrograma(self, ctx:ScalarProductParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#declaracaoClasse.
    def visitDeclaracaoClasse(self, ctx:ScalarProductParser.DeclaracaoClasseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#bloco.
    def visitBloco(self, ctx:ScalarProductParser.BlocoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#declaracaoFuncao.
    def visitDeclaracaoFuncao(self, ctx:ScalarProductParser.DeclaracaoFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#listaParametros.
    def visitListaParametros(self, ctx:ScalarProductParser.ListaParametrosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#parametro.
    def visitParametro(self, ctx:ScalarProductParser.ParametroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#atribuicao.
    def visitAtribuicao(self, ctx:ScalarProductParser.AtribuicaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#chamadaFuncao.
    def visitChamadaFuncao(self, ctx:ScalarProductParser.ChamadaFuncaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#imprimirStatement.
    def visitImprimirStatement(self, ctx:ScalarProductParser.ImprimirStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#argumentos.
    def visitArgumentos(self, ctx:ScalarProductParser.ArgumentosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#expressao.
    def visitExpressao(self, ctx:ScalarProductParser.ExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#listaExpressao.
    def visitListaExpressao(self, ctx:ScalarProductParser.ListaExpressaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#compreensaoLista.
    def visitCompreensaoLista(self, ctx:ScalarProductParser.CompreensaoListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#acessoLista.
    def visitAcessoLista(self, ctx:ScalarProductParser.AcessoListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ScalarProductParser#slice.
    def visitSlice(self, ctx:ScalarProductParser.SliceContext):
        return self.visitChildren(ctx)



del ScalarProductParser
from antlr4 import *

from arquivos_gramatica.ScalarProductLexer import ScalarProductLexer
from arquivos_gramatica.ScalarProductParser import ScalarProductParser

from analisador_sematico import SemanticAnalyzer


def main():
    with open('entrada.py', 'r', encoding='utf-8') as f:
        codigo_entrada = f.read()

    fluxo_entrada = InputStream(codigo_entrada)
    lexer = ScalarProductLexer(fluxo_entrada)
    tokens = CommonTokenStream(lexer)
    parser = ScalarProductParser(tokens)

    arvore = parser.programa()

    visitante = SemanticAnalyzer()
    visitante.visit(arvore)


main()

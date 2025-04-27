from antlr4 import *
from arquivos_gramatica.ScalarProductLexer import ScalarProductLexer
from arquivos_gramatica.ScalarProductParser import ScalarProductParser
from antlr4.tree.Tree import TerminalNode


def run():
    import subprocess

    # Caminhos para os arquivos do ANTLR
    antlr_jar_path = '../Av2_compiladores/antlr-4.13.2-complete.jar'
    target_dir = '../Av2_compiladores/arquivos_gramatica/'

    # Comando para gerar os arquivos com ANTLR
    command = [
        'java',
        '-jar',
        antlr_jar_path,
        '-Dlanguage=Python3',  # Definindo a linguagem de saída como Python3
        '-o', target_dir,  # Diretório de saída
        'ScalarProduct.g4'
    ]

    # Executando o comando ANTLR
    try:
        subprocess.run(command, check=True)
        print("ANTLR gerado com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o ANTLR: {e}")
        return


run()


def analisar_codigo(codigo_fonte):
    # Criação do fluxo de entrada a partir do código fonte
    input_stream = InputStream(codigo_fonte)

    # Instanciando o lexer e o parser
    lexer = ScalarProductLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = ScalarProductParser(token_stream)

    # Analisando o código a partir da regra inicial 'prog'
    tree = parser.programa()

    # Exibindo a árvore sintática gerada
    print("Árvore Sintática:")
    print(tree.toStringTree(recog=parser))  # Exibe a árvore sintática gerada

    # Percorrendo a árvore para identificar e exibir nós terminais
    print("\nTokens na árvore sintática (nós terminais):")
    for child in tree.getChildren():
        if isinstance(child, TerminalNode):  # Verifica se o nó é um TerminalNode
            print(f"Nó terminal: {child.getText()}")  # Exibe o texto do token

    # Verificando erros sintáticos
    if parser.getNumberOfSyntaxErrors() > 0:
        print("Erro(s) sintático(s) encontrado(s).")
    else:
        print("Código sintaticamente correto!")


with open('entrada.py', 'r', encoding='utf-8') as f:
    source = f.read()

# Analisando o código fonte após gerar o lexer e o parser com ANTLR
analisar_codigo(source)

import re
import pandas as pd

# Definições dos tokens
padroes_tokens = [
    ('CLASS', r'\bclass\b'),
    ('INIT', r'__init__'),
    ('PALAVRA_RESERVADA', r'\b(range|return|print|if|else|while|return|break|continue|for|in|def)\b'),
    ('IDENTIFICADOR', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('NUMERO', r'\d+'),
    ('ATRIBUICAO', r'='),
    ('PARENTESE_ESQUERDO', r'\('),
    ('PARENTESE_DIREITO', r'\)'),
    ('COLCHETE_ESQUERDO', r'\['),
    ('COLCHETE_DIREITO', r'\]'),
    ('DOIS_PONTOS', r':'),
    ('VIRGULA', r','),
    ('PONTO', r'\.'),
    ('SOMA', r'\+'),
    # ('SUBTRAÇÃO', r'\-'),
    ('MULTIPLICACAO', r'\*'),
    ('TEXTO', r'"[^"]*"|\'[^\']*\''),
    ('NOVA_LINHA', r'\n'),
    ('ESPACO', r'[ \t]+'),
]

# Compilar o padrão geral
padrao_geral = re.compile('|'.join(f'(?P<{nome}>{regex})' for nome, regex in padroes_tokens))


def analisador_lexico(codigo_fonte):
    posicao = 0
    tokens_encontrados = []

    while posicao < len(codigo_fonte):
        correspondencia = padrao_geral.match(codigo_fonte, posicao)

        if correspondencia:
            tipo_token = correspondencia.lastgroup
            valor_token = correspondencia.group(tipo_token)

            if tipo_token != 'ESPACO' and tipo_token != 'NOVA_LINHA':
                print(f'Token: {tipo_token}, Valor: "{valor_token}"')
                tokens_encontrados.append({'Token': tipo_token, 'Valor': valor_token})

            posicao = correspondencia.end()

        else:
            print(f'Caractere inválido: {codigo_fonte[posicao]}')
            tokens_encontrados.append({'Token': 'INVALIDO', 'Valor': codigo_fonte[posicao]})
            posicao += 1

    return tokens_encontrados


with open('entrada.py', 'r', encoding='utf-8') as f:
    source = f.read()

# Analisando e coletando tokens
tokens = analisador_lexico(source)

df = pd.DataFrame(tokens)
df.to_csv('tokens_gerados.csv', index=False, sep=';')

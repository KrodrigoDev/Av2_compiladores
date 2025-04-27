# Compilador Simples de Produto Escalar

---
## Propósito

Este projeto tem como objetivo construir um compilador simples que percorra as fases de **Análise Léxica**, **Análise Sintática** e **Análise Semântica**, utilizando como entrada um código em Python que realiza o **produto escalar** de duas listas.

---

## Ferramentas Utilizadas

- **Linguagem:** Python 3
- **Bibliotecas:**
  - `re` — utilizada para a análise léxica (expressões regulares)
  - `pandas` — utilizada para gerar e salvar tabelas (CSV)
- **Editor:** PyCharm
- **Ferramentas Auxiliares:** 
  - **ANTLR Tool Preview** — para criação e visualização de gramáticas.

---

## Código Fonte de Entrada

O código utilizado como entrada em todas as fases do compilador é o seguinte:

```python
class Linear_algebrar:
    def __init__(self):
        print('Vamos começar a brincar...')

    def scalar_product(self, m1: list, m2: list):
        step_one = [x * y for x, y in zip(m1, m2)]
        step_two = sum(step_one[:])

        return step_two

linear = Linear_algebrar()

res = linear.scalar_product([2, 4, 2], [2, 4, 2])

print(f'Resultado da multiplicação de matrizes: {res}')
```

---

# Fases do Compilador

## Fase 1 — Análise Léxica

**O que foi realizado:**

- Definição dos **tokens** a serem reconhecidos: palavras reservadas, identificadores, números, símbolos, operadores e textos.
- Implementação de um **analisador léxico** em Python utilizando a biblioteca `re` (expressões regulares).
- Identificação dos tokens válidos e inválidos no código-fonte.
- Geração de uma **tabela CSV** com o resultado da análise, utilizando `pandas`.

---

## Fase 2 — Análise Sintática

**O que foi realizado:**

- Definição de uma **Gramática Livre de Contexto (GLC)** capaz de validar a estrutura dos tokens extraídos.
- Criação de um arquivo `.g4` com as regras para:
  - Definição de classes (`class`),
  - Definição de funções (`def`),
  - Atribuições de variáveis (`=`),
  - Chamadas de funções e métodos (`objeto.metodo()`),
  - Estruturas de listas e operações matemáticas.
- Utilização do **ANTLR Tool Preview** para:
  - **Visualizar a árvore sintática** gerada,
  - **Detectar erros sintáticos** automaticamente.

---

## Fase 3 — Análise Semântica

**Status:**  
🚧 Ainda não iniciada. Em breve!

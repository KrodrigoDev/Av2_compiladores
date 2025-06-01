from arquivos_gramatica.ScalarProductVisitor import ScalarProductVisitor
from arquivos_gramatica.ScalarProductParser import ScalarProductParser


class SemanticAnalyzer(ScalarProductVisitor):
    def __init__(self):
        self.symbol_table = {}  # Tabela de símbolos
        self.ast = []  # Árvore de sintaxe abstrata

    def visitPrograma(self, ctx: ScalarProductParser.ProgramaContext):
        print("\n=== Iniciando Análise Semântica ===\n")
        self.visitChildren(ctx)

        print("\n=== Tabela de Símbolos ===")
        for nome, info in self.symbol_table.items():
            print(f"  {nome}: {info}")

        print("\n=== Árvore de Sintaxe Abstrata (AST) ===")
        for nodo in self.ast:
            print(" ", nodo)

        print("\n=== Fim da Análise Semântica ===")

    def visitDeclaracaoFuncao(self, ctx: ScalarProductParser.DeclaracaoFuncaoContext):
        nome_funcao = ctx.ID().getText()
        parametros = []

        if ctx.listaParametros():
            for parametro in ctx.listaParametros().parametro():
                nome_param = parametro.ID()[0].getText()
                parametros.append(nome_param)
                self.symbol_table[nome_param] = "PARAMETRO"

        self.symbol_table[nome_funcao] = {
            "tipo": "FUNCAO",
            "parametros": parametros
        }

        self.ast.append({
            "tipo": "declaracao_funcao",
            "nome": nome_funcao,
            "parametros": parametros,
            "linha": ctx.start.line
        })

        self.visit(ctx.bloco())

    def visitBloco(self, ctx: ScalarProductParser.BlocoContext):
        for child in ctx.children:
            self.visit(child)

    def visitAtribuicao(self, ctx: ScalarProductParser.AtribuicaoContext):
        nome_variavel = ctx.ID().getText()
        tipo_rhs = self.visit(ctx.expressao())

        # Verifica se está usando variável não declarada
        if ctx.expressao().ID():
            rhs_nome = ctx.expressao().ID().getText()
            if rhs_nome not in self.symbol_table:
                print(f"[Erro - linha {ctx.start.line}] Variável '{rhs_nome}' usada antes de ser declarada.")
                tipo_rhs = "DESCONHECIDO"

        if nome_variavel in self.symbol_table:
            print(f"[Aviso] Variável '{nome_variavel}' reatribuída. Tipo anterior: {self.symbol_table[nome_variavel]}")
        else:
            print(f"[Info] Declarando variável '{nome_variavel}' com tipo '{tipo_rhs}'.")

        self.symbol_table[nome_variavel] = tipo_rhs if tipo_rhs else "DESCONHECIDO"

        self.ast.append({
            "tipo": "atribuicao",
            "variavel": nome_variavel,
            "valor": tipo_rhs,
            "linha": ctx.start.line
        })

    def visitExpressao(self, ctx: ScalarProductParser.ExpressaoContext):
        if ctx.NUMERO():
            return "NUMERO"
        elif ctx.TEXTO():
            return "TEXTO"
        elif ctx.compreensaoLista() or ctx.listaExpressao():
            return "LISTA"
        elif ctx.chamadaFuncao():
            return self.visit(ctx.chamadaFuncao())
        elif ctx.acessoLista():
            return "LISTA"
        elif ctx.ID():
            nome = ctx.ID().getText()
            if nome not in self.symbol_table:
                print(f"[Erro - linha {ctx.start.line}] Variável '{nome}' não declarada.")
                return "DESCONHECIDO"
            return self.symbol_table[nome]
        elif ctx.expressao(0) and ctx.expressao(1):
            tipo_esq = self.visit(ctx.expressao(0))
            tipo_dir = self.visit(ctx.expressao(1))

            if tipo_esq != tipo_dir:
                print(f"[Erro - linha {ctx.start.line}] Operação entre tipos incompatíveis: {tipo_esq} e {tipo_dir}.")
                return "TIPO_INCOMPATIVEL"

            if tipo_esq == "NUMERO":
                return "NUMERO"
            elif tipo_esq == "LISTA":
                return "LISTA"

            print(f"[Erro - linha {ctx.start.line}] Operação inválida entre tipos {tipo_esq} e {tipo_dir}.")
            return "TIPO_INVALIDO"

        return None

    def visitCompreensaoLista(self, ctx: ScalarProductParser.CompreensaoListaContext):
        return "LISTA"

    def visitChamadaFuncao(self, ctx: ScalarProductParser.ChamadaFuncaoContext):
        nome_funcao = ctx.ID().getText()

        # Funções built-in
        if nome_funcao in ["sum", "zip", "print"]:
            if ctx.argumentos():
                argumentos = ctx.argumentos().expressao()
                for arg in argumentos:
                    tipo_arg = self.visit(arg)
                    if tipo_arg == "DESCONHECIDO":
                        print(
                            f"[Aviso - linha {ctx.start.line}] Argumento indefinido na chamada à função '{nome_funcao}'.")
            return "NUMERO" if nome_funcao == "sum" else "LISTA" if nome_funcao == "zip" else "VOID"

        # Verificação de função declarada
        if nome_funcao in self.symbol_table and self.symbol_table[nome_funcao]["tipo"] == "FUNCAO":
            func_info = self.symbol_table[nome_funcao]
            param_esperados = len(func_info["parametros"])
            param_recebidos = len(ctx.argumentos().expressao()) if ctx.argumentos() else 0

            if param_esperados != param_recebidos:
                print(
                    f"[Erro - linha {ctx.start.line}] Função '{nome_funcao}' esperava {param_esperados} argumento(s), mas recebeu {param_recebidos}.")

            self.ast.append({
                "tipo": "chamada_funcao",
                "nome": nome_funcao,
                "args": param_recebidos,
                "linha": ctx.start.line
            })

            return "NUMERO"  # você pode adaptar para o tipo real da função
        else:
            print(f"[Erro - linha {ctx.start.line}] Chamada à função não definida '{nome_funcao}'.")
            return "FUNCAO_NAO_DEFINIDA"

    def visitAcessoLista(self, ctx: ScalarProductParser.AcessoListaContext):
        return "LISTA"

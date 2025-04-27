grammar ScalarProduct;


// Tokens
CLASSE : 'class';
FUNC : 'def';
RETORNAR : 'return';
IMPRIMIR : 'print';
NOVO : '=';
PARA : 'for';
EM : 'in';
ABRE_PARENTESES : '(';
FECHA_PARENTESES : ')';
ABRE_COLCHETES : '[';
FECHA_COLCHETES : ']';
DOIS_PONTOS : ':';
VIRGULA : ',';
OPERADOR_MATEMATICO : '*' | '+' | '-' | '/';
ID : [a-zA-Z_][a-zA-Z0-9_]*;
NUMERO : [0-9]+;
TEXTO : '\'' (~['\r\n])* '\'';
WS : [ \t\r\n]+ -> skip;

// Regras
programa : declaracaoClasse+;

declaracaoClasse : CLASSE ID DOIS_PONTOS bloco;

bloco : (declaracaoFuncao | atribuicao | chamadaFuncao | imprimirStatement)+;

declaracaoFuncao : FUNC ID ABRE_PARENTESES listaParametros? FECHA_PARENTESES DOIS_PONTOS bloco;

listaParametros : parametro (VIRGULA parametro)*;
parametro : ID (DOIS_PONTOS ID)?;

atribuicao : ID NOVO expressao;

chamadaFuncao : ID (ABRE_PARENTESES argumentos? FECHA_PARENTESES);

imprimirStatement : IMPRIMIR ABRE_PARENTESES expressao FECHA_PARENTESES;

argumentos : expressao (VIRGULA expressao)*;

expressao
    : ID
    | acessoLista
    | NUMERO
    | listaExpressao
    | chamadaFuncao
    | TEXTO
    | compreensaoLista
    ;

listaExpressao : ABRE_COLCHETES argumentos? FECHA_COLCHETES;

compreensaoLista
    : ABRE_COLCHETES expressao OPERADOR_MATEMATICO expressao PARA ID VIRGULA ID EM chamadaFuncao FECHA_COLCHETES
    ;

acessoLista
    : ID ABRE_COLCHETES slice? FECHA_COLCHETES
    ;

slice
    : (NUMERO)? DOIS_PONTOS (NUMERO)?
    ;

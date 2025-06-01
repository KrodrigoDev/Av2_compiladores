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
        '-visitor',
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
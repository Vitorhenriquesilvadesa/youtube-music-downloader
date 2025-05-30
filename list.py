import os


def listar_arquivos_sem_extensao(diretorio):
    for root, dirs, files in os.walk(diretorio):
        for nome_arquivo in files:
            nome_sem_extensao, _ = os.path.splitext(nome_arquivo)
            print(nome_sem_extensao)


# Exemplo de uso:
diretorio_alvo = "D:/"  # substitua pelo caminho desejado
listar_arquivos_sem_extensao(diretorio_alvo)

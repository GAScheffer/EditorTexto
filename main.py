import os

# local do arquivo a ser alterado:
local = input(" Digite o caminho completo da pasta onde está o arquivo: ")

# Quais são os Prefixos e os Sufixos
prefixo = input(f'Digite os caracteres que ficarão ANTES das palavras já existente no arquivo: ')
sufixo = input(f'digite os caracteres que ficarão DEPOIS das palavras já existentes no arquivo: ')


# abrir o arquivo de texto original para leitura
with open(os.path.join(local, "documento.txt"), "r") as arquivo_original:
    # ler o conteúdo do arquivo em uma variável
    conteudo = arquivo_original.read()

# dividir o conteúdo do arquivo em uma lista de palavras
palavras = conteudo.split()

# criar uma lista vazia para armazenar as palavras modificadas
palavras_modificadas = []

# percorrer a lista de palavras e adicionar os caracteres necessários

for palavra in palavras:
    palavra_modificada = prefixo + palavra + sufixo + "\n"
    palavras_modificadas.append(palavra_modificada)

# juntar as palavras modificadas de volta em uma string
novo_conteudo = " ".join(palavras_modificadas)

# abrir um novo arquivo de texto para escrita
with open(os.path.join(local, "resultado.txt"), "w") as arquivo_modificado:
    # escrever o conteúdo modificado no novo arquivo
    arquivo_modificado.write(novo_conteudo)

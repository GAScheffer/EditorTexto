import os

# LOCAL DO ARQUIVO A SER ALTERADO:
"""
Escolha qual melhor forma deseja proceder. Pode definir como forma de input e
sempre digitar o caminho quando executar o script ou deixa o caminho como forma fixa.
Aquele que desejar, remova a cerquilha da frente: 
"""
# local = input(" Digite o caminho completo da pasta onde está o arquivo com o nome do arquivo: ")
# local = "/home/gustavo/Área de Trabalho/exemplo.txt"


# INPUT DOS PREFIXOS E DOS SUFIXOS:
prefixo = input(f'Digite os caracteres que ficarão ANTES das palavras já existente no arquivo: ')
sufixo = input(f'digite os caracteres que ficarão DEPOIS das palavras já existentes no arquivo: ')

# ABRIR O ARQUIVO DE TEXTO ORIGINAL PARA LEITURA.
"""
Na linha 21, altere o nome do "documentos.txt" com o nome do arquivo que será carregado
"""
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

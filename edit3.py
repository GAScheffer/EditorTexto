# abrir o arquivo de texto original para leitura
with open("/home/gustavo/Área de Trabalho/exemplo.txt", "r") as arquivo_original:
    # ler o conteúdo do arquivo em uma variável
    conteudo = arquivo_original.read()

# dividir o conteúdo do arquivo em uma lista de palavras
palavras = conteudo.split()

# criar uma lista vazia para armazenar as palavras modificadas
palavras_modificadas = []

# percorrer a lista de palavras e adicionar os caracteres necessários
for palavra in palavras:
    palavra_modificada = "AAA" + palavra + "XXX" + "\n"
    palavras_modificadas.append(palavra_modificada)

# juntar as palavras modificadas de volta em uma string
novo_conteudo = " ".join(palavras_modificadas)

# abrir um novo arquivo de texto para escrita
with open("/home/gustavo/Área de Trabalho/resultado.txt", "w") as arquivo_modificado:
    # escrever o conteúdo modificado no novo arquivo
    arquivo_modificado.write(novo_conteudo)

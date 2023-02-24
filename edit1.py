import re

# abrir o arquivo de entrada em modo leitura
with open('/home/gustavo/Área de Trabalho/exemplo.txt', 'r') as arquivo_entrada:
    # ler as linhas do arquivo e armazená-las em uma lista
    linhas = arquivo_entrada.readlines()

# criar um novo arquivo de saída em modo escrita
with open('/home/gustavo/Área de Trabalho/arquivo_saida1.txt', 'w') as arquivo_saida:
    # percorrer cada linha da lista
    for linha in linhas:
        # usar a expressão regular para encontrar os números na linha
        numeros = re.findall('\d+', linha)

        # adicionar as três letras antes e depois de cada número encontrado
        for numero in numeros:
            linha = re.sub(numero, 'AAA' + numero + 'ZZZ', linha)

        # escrever a linha modificada no novo arquivo de saída
        arquivo_saida.write(linha)
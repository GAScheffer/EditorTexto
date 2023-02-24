
with open('/home/gustavo/Área de Trabalho/exemplo.txt', 'r') as arquivo:
    # ler as linhas do arquivo e armazená-las em uma lista
    linhas = arquivo.readlines()

for i in range(len(linhas)):
    linha = linhas[i].strip()    # remove espaços em branco e quebras de linha
    nova_linha = ""
    for j in range(len(linha)):
        if linha[j].isdigit():    # verifica se o caractere é um digito numérico
            nova_linha += "AAA" + linha[j] + "XXX"    # adiciona as três letras antes e depois do dígito
        else:
            nova_linha += linha[j]    # mantém o caractere original se não for um dígito
        linhas[i] = nova_linha + "\n"    # adiciona uma quebra de linha no final da linha

with open('/home/gustavo/Área de Trabalho/arquivo_saida.txt', 'w') as arquivo:
    arquivo.writelines(linhas)

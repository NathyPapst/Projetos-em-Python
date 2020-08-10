# Projeto 4 - Matrizes
# Isabela Marim - 31958397 e Nathalia Papst - 31919928

def arquivo (matriz):
    arquivo = open("matriz4.txt","r") # leitura do arquivo
    while True: #repetição para poder ler o arquivo inetiro
        linha_coluna = arquivo.readline() #leitura de uma linha do arquivo
        if linha_coluna == "": 
            break
        valor = linha_coluna.split(" ")
        for i in range(len(valor)): # repetição para transformação dos valores para float
            valor[i] = float(valor[i])
        print(valor)
        linha = [] # criação da linha da matriz
        for x in range (len(valor)): # for para adicionar os valores floats na linha
            linha.append(valor[x]) #adiciona os valores de valor na lista linha
        matriz.append(linha) # adiciona a linha na matriz
    arquivo.close() #fecha o arquivo
    return matriz #retorna a matriz

def linhas (soma_das_linhas,matriz): # realiza a soma das linhas
    linhas = int(matriz[0][0]) #tranforma o primeiro elemento da primeira linha da matriz em inteiro
    colunas = int(matriz[0][1]) #tranforma o primeiro elemento da segunda coluna da matriz em inteiro
    for j in range (1,linhas + 1): # repetição para acumular a soma de cada linha
        soma_linha = 0
        for k in range (colunas): #repetição para passar pelo número de colunas
            soma_linha += matriz[j][k] #efetua a soma de cada linha
        soma_das_linhas.append(soma_linha) # adicionando a soma na lista
    return soma_das_linhas #retorna a lista

def colunas (soma_das_colunas,matriz): # realiza a soma das colunas
    linhas = int(matriz[0][0]) #tranforma o primeiro elemento da primeira linha da matriz em inteiro
    colunas = int(matriz[0][1]) #tranforma o primeiro elemento da segunda coluna da matriz em inteiro
    for l in range (colunas): # repetição para acumular a soma de cada coluna
        soma_coluna = 0
        for m in range (1,linhas+1): #repetição para passar por todas as linhas começando da segundo até uma além da última
            soma_coluna += matriz[m][l] #efetua a soma de cada coluna
        soma_das_colunas.append(soma_coluna) # adicionando a soma na lista
    return soma_das_colunas #retorna a lista 
   
def centro_linhas (soma_das_linhas): #função para descobrir o centro de gravidade das linhas
    lista_soma_cima = [] #criação da lista das somas acima a linha selecionada
    lista_soma_baixo = [] #criação da lista das somas abaixo a linha selecionada
    for y in range (1,len(soma_das_linhas)-1): #repetição passando pelas linhas começando da segunda e indo até a penúltima
        indice_esquerda = 0
        indice_direita = len(soma_das_linhas)-1
        soma_cima = 0
        soma_baixo = 0
        while indice_esquerda < y: #repetição enquanto o índice da esquerda for menor que y
            soma_cima += soma_das_linhas[indice_esquerda] #efetua a soma das linhas de cima da linha selecionada
            indice_esquerda += 1 #aumenta o tamanho do índice da esquerda
        lista_soma_cima.append(soma_cima) #adiciona a soma de cima a lista de somas de cima
        while indice_direita > y: #repetição enquanto o índice da direita é maior que y
            soma_baixo += soma_das_linhas[indice_direita] #efetua a soma das linhas abaixo da linha selecionada
            indice_direita -= 1 #diminui o tamanho do índice da direita
        lista_soma_baixo.append(soma_baixo) #adiciona a soma de baixo a lista de somas de baixo

    menor_dif_linhas = 100
    indice_menor_dif_linhas = 0
    for w in range (len(lista_soma_cima)): #repetição passando pela lista da soma de cima
        dif = abs(lista_soma_cima[w] - lista_soma_baixo[w]) #efetua a subtração modular entre a lista das somas de cima pela lista das somas de baixo
        if dif < menor_dif_linhas: #condicional para quando a diferença for menor diferença das linhas
            menor_dif_linhas = dif #diferença se tranforma na menor diferença das linhas
            indice_menor_dif_linhas = w+2 
    return indice_menor_dif_linhas

def centro_colunas (soma_das_colunas): #função para descobrir o centro de gravidade das linhas
    lista_soma_esquerda = [] #criação da lista das somas a esquerda da coluna selecionada
    lista_soma_direita = [] #criação da lista das somas a direita da coluna selecionada
    for y in range (1,len(soma_das_colunas)-1): #repetição passando pelas colunas começando da segunda e indo até a penúltima
        indice_cima = 0
        indice_baixo = len(soma_das_colunas)-1
        soma_esquerda = 0
        soma_direita = 0
        while indice_cima < y: #repetição enquanto o índice de cima for menor que y
            soma_esquerda += soma_das_colunas[indice_cima] #efetua a soma das colunas a esquerda da coluna selecionada
            indice_cima += 1 #aumenta o tamanho do índice de cima
        lista_soma_esquerda.append(soma_esquerda) #adiciona a soma da esquerda a lista de somas da esquerda
        while indice_baixo > y: #repetição enquanto o índice da direita é maior que y
            soma_direita += soma_das_colunas[indice_baixo] #efetua a soma das colunas a direita da linha selecionada
            indice_baixo -= 1 #diminui o tamanho do índice de baixo
        lista_soma_direita.append(soma_direita) #adiciona a soma da direita a lista de somas da direita

    menor_dif_colunas = 100
    indice_menor_dif_colunas = 0
    for w in range (len(lista_soma_esquerda)): #repetição passando pela lista da soma da esquerda
        dif = abs(lista_soma_esquerda[w] - lista_soma_direita[w]) #efetua a subtração modular entre a lista das somas da esquerda pela lista das somas da direita
        if dif < menor_dif_colunas: #condicional para quando a diferença for menor diferença das linhas
            menor_dif_colunas = dif #diferença se tranforma na menor diferença das linhas
            indice_menor_dif_colunas = w+2
    return indice_menor_dif_colunas


def main():
    matriz = [] # criação da matriz
    print("Matriz:")
    arquivo (matriz)
    soma_das_linhas = [] # criação da lista para guardar as somas das linhas
    linhas (soma_das_linhas,matriz) #chama a função
    soma_das_colunas = [] # criação da lista para guardar as somas das colunas
    colunas (soma_das_colunas,matriz) #chama a função     
    print("\nCentro de gravidade: (",centro_linhas (soma_das_linhas),";",centro_colunas (soma_das_colunas),")") #imprime chamando a função
    

main()

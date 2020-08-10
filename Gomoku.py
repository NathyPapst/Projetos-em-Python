#Gomoku
#Isabela Marim - 31958397
#Nathalia Papst - 31919928

def initialize (matriz): #função que cria a matriz vazia
  for i in range (15):
    linha = [0]*15
    matriz.append(linha)
  return matriz

def printMat (matriz): #função que imprime a matriz com os elementos certos
  print("\n    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14")
  for i in range (15):
    if i < 10:
      print(i,end="  ")
    else:
      print(i,end=" ")
    for j in range (15):
      if matriz[i][j] == 0:
        print("|_|",end=" ")
      elif matriz[i][j] == 1:
        print("|1|",end=" ")
      elif matriz[i][j] == -1:
        print("|2|",end=" ")
    print("\n")

def step(matriz,lin,col,cod): #função que controla os espaços livres e ocupados da matriz
  if matriz[lin][col] != 0:
    return False  
  else:
    if cod == "1":
      matriz[lin][col] = 1
    else: 
      matriz[lin][col] = -1
    return True
  
def status(matriz,cod): #função que define quando algumjogador ganha ouo empate

  cont1_lin = 0
  cont1_col = 0
  cont2_lin = 0
  cont2_col = 0

  #vitória por linha e coluna para ambos jogadores
  for i in range (15):
    for j in range (15):
      if matriz [i][j] == 1: #jogador 1 linha
        cont1_lin += 1
        if cont1_lin == 5:
            return 1
      else:
        cont1_lin = 0
      if matriz [j][i] == 1: #jogador 1 coluna
        cont1_col += 1
        if cont1_col == 5:
            return 1
      else:
        cont1_col = 0

      if matriz [i][j] == -1: #jogador 2 linha
        cont2_lin -= 1
        if cont2_lin == -5:
            return 2
      else:
        cont2_lin = 0
      if matriz [j][i] == -1: #jogador 2 coluna
        cont2_col -= 1
        if cont2_col == -5:
            return 2
      else:
        cont2_col = 0
  
  
  #vitória por diagonal para ambos os jogadores
  for i in range(0, len(matriz)): # \ de baixo 
    cont_direita_baixo1 = 0 
    cont_direita_baixo2 = 0
    j = 0
    while i < len(matriz) and j < len(matriz[0]):
        if matriz[i][j] == 1: # jogador 1
            cont_direita_baixo1 += 1
            cont_direita_baixo2 = 0
            if cont_direita_baixo1 == 5:
                return 1
        elif matriz[i][j] == -1: # jogador 2 
            cont_direita_baixo2 += 1
            cont_direita_baixo1 = 0
            if cont_direita_baixo2 == 5:
                return 2
        else:
            cont_direita_baixo2 = 0
            cont_direita_baixo1 = 0
        i += 1
        j += 1
  
  for j in range(1, len(matriz[0])): # \ de cima
    cont_direita_cima1 = 0
    cont_direita_cima2 = 0
    i = 0
    while i < len(matriz) and j < len(matriz[0]):
        if matriz[i][j] == 1: # jogador 1
            cont_direita_cima1 += 1
            cont_direita_cima2 = 0
            if cont_direita_cima1 == 5:
                return 1
        elif matriz[i][j] == -1: # jogador 2
            cont_direita_cima2 += 1
            cont_direita_cima1 = 0
            if cont_direita_cima2 == 5:
                return 2
        else:
            cont_direita_cima2 = 0
            cont_direita_cima1 = 0
        i += 1
        j += 1
  
  for j in range(1, len(matriz[0])): # / de cima
    cont_esquerda_cima1 = 0
    cont_esquerda_cima2 = 0
    i = 0
    while i < len(matriz) and j >=0:
      if matriz[i][j] == 1: # jogador 1
        cont_esquerda_cima1 += 1
        cont_esquerda_cima2 = 0
        if cont_esquerda_cima1 == 5:
          return 1
      elif matriz[i][j] == -1: # jogador 2
        cont_esquerda_cima2 += 1
        cont_esquerda_cima1 = 0
        if cont_esquerda_cima2 == 5:
          return 2
      else:
        cont_esquerda_cima2 = 0
        cont_esquerda_cima1 = 0
      i += 1
      j -= 1
  
  for i in range(1, len(matriz)): # / de baixo
    cont_esquerda_baixo1 = 0
    cont_esquerda_baixo2 = 0
    j = len(matriz[0]) - 1
    while i < len(matriz) and j < len(matriz[0]):
      if matriz[i][j] == 1: # jogador 1
        cont_esquerda_baixo1 += 1
        cont_esquerda_baixo2 = 0
        if cont_esquerda_baixo1 == 5:
          return 1
      elif matriz[i][j] == -1: # jogador 2
        cont_esquerda_baixo2 += 1
        cont_esquerda_baixo1 = 0
        if cont_esquerda_baixo2 == 5:
          return 2
      else:
        cont_esquerda_baixo2 = 0
        cont_esquerda_baixo1 = 0
      i += 1
      j -= 1
    
  #empate entre os jogadores
  empate = 0
  for i in range (15):
    for j in range (15):
      if matriz[i][j] == 1 or matriz[i][j] == -1:
        empate += 1
  if empate == 225:
    return 0
  
  return -1

def game (): #função principal que chama todas as outras e realiza alguns comandos para o funcionamento total
  matriz = []
  initialize(matriz) #chama a função que criou a matriz
  fim = ""

  while fim == "":
    jogador = 0
    printMat (matriz) #chama a função que imprime a matriz

    while fim == "":
      
      if jogador % 2 == 0: #condicional para definir a rodada de cada jogador
        print("\n----- Jogador 1 -----")
        codigo = "1"
      else:
        print("\n----- Jogador 2 -----")
        codigo = "2"
    
      linha  = int(input("\nLinha: ")) #validação da linha da matriz
      while linha >= 15 or linha < 0:
        linha  = int(input("Linha inválida! Digite novamente: "))
      coluna = int(input("Coluna: ")) #validação da coluna da matriz
      while coluna >= 15 or coluna < 0:
        coluna  = int(input("Coluna inválida! Digite novamente: "))
      
      if step(matriz,linha,coluna,codigo) == False:
        jogador -= 1
        print("\nPosição inválida!")
      else:
        printMat(matriz)
      
      if status(matriz,codigo) == 1: #vitória do jogador 1
        print("\n-----------------------")
        print("  O jogador 1 venceu!")
        print("-----------------------")
        fim = True
      elif status(matriz,codigo) == 2: #vitória do jogador 2
        print("\n-----------------------")
        print("  O jogador 2 venceu!")
        print("-----------------------")
        fim = True
      elif status(matriz,codigo) == 0: #empate entre os jogadores
        print("\n--------------")
        print("   Empate!")
        print("--------------")
        fim = True

      jogador += 1

game() #chama a função principal
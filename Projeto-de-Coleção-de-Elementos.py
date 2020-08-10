def imprimeColecao(colecao,qtd): #função que imprime o vetor apenas com a quantidade de elementos válidos presentes nele
   print("\nColeção = [",end=' ')
   for i in range(qtd):
      print( colecao[i],end=' ')
   print("]\n")

def addFinal(colecao,qtd,elem): #função que adiciona um certo elemento digitado pelo usuário ao final do vetor
   if qtd < 100:
      colecao[qtd]=elem
      qtd += 1
   return qtd

def addPosicao(colecao,qtd,elem,posicao): #função que adiciona um certo elemento numa certa posição digitados pelo usuário
  if qtd< 100:
    if posicao == qtd:
      colecao[posicao] = elem
      qtd += 1
    else:
      for i in range (qtd,posicao,-1):
        colecao[i] = colecao[i-1]
      colecao[posicao] = elem
      qtd += 1
  return qtd

def removerPos(colecao,qtd,posicaoRemov): #função que remove o elemento de uma certa posição digitada pelo usuário
  for i in range (posicaoRemov, qtd-1):
    colecao[i] = colecao[i+1]
  qtd -= 1
  return qtd

def remover1Ocorrencia(colecao,qtd,elemRemov): #função que remove a primeira ocorrência, de um certo número digitado pelo usuário, do vetor 
  if elemRemov in colecao:
    cont = 0
    for i in range (qtd):
      if colecao[i] == elemRemov:
        cont = i
        while cont < qtd:
          colecao[cont] = colecao[cont+1]
          cont += 1
        break
    qtd -= 1
  else:
    print("\nEsse elemento não pertence a coleção")
  return qtd

def removerTodos(colecao,qtd,elemRemov): # função que remove todas as ocorrências, de um certo elemento digitado pelo usuário, do vetor
  if elemRemov in colecao:
    while elemRemov in colecao:
      cont = 0
      for i in range (qtd):
        if colecao[i] == elemRemov:
          cont = i
          while cont < qtd:
            colecao[cont] = colecao[cont+1]
            cont += 1
          break
      qtd -= 1
  else:
    print("\nEsse elemento não pertence a coleção")
  return qtd

def elem_naColecao(colecao,qtd,elem_busca): #função que busca um certo elemento, digitado pelo usuário, no vetor e retorna sua posição a ele, caso não esteja retorna -1
  for i in range (qtd):
    if colecao[i]==elem_busca:
      print("\nO elemento",elem_busca,"está na posição",i,"da coleção.")
      break
  else:
    print("-1")
  return qtd
  
def soma_igual_elem(colecao,qtd,elem_soma): #função que busca dois elementos no vetor que somados resultam no elemento digitado pelo usuário, se existe retorna True, se não, retorna False
  for i in range(qtd-1):
    for j in range(i+1,qtd):
      if colecao[i] + colecao[j] == elem_soma:
        return True
        break
  return False

def main(): #função principal 
  colecao = [0]*100 #vetor de 100 posições
  qtd = 0 #quantidade de elementos válidos no vetor
  opc = 0 #opção do usuário
     
  while opc != 8: #enquanto a opção for menor que 8 imprimirá as seguintes frases
    print("\n1 - Adicionar um elemento no final da coleção")
    print("2 - Adicionar um elemento em uma posição da coleção")
    print("3 - Remover um elemento em uma posição na coleção")
    print("4 - Remover a primeira ocorrência do elemento na coleção")
    print("5 - Remover todas as ocorrências de um elemento na coleção")
    print("6 - Verificar se dado um elemento está contido na coleção")
    print("7 - Verificar se dado um valor existem dois elementos na coleção que somados é igual ao valor informado")
    print("8 - sair")
    opc = int(input("\nInsira a opção: ")) #input para o usuário digitar sua opção
    while opc>8 or opc<1: #enquanto a opção for maior que 8 ou menor que 1, o usuário terá que digitar novamente
      opc=int(input("Opção inválida! Digite novamente: ")) 
    
    # Adicionar um elemento no final da coleção
    if opc == 1: #condicional para casoo usuário escolha a opção 1
      elem = int(input("\nDigite um elemento: "))
      qtd = addFinal(colecao,qtd,elem )
     
    # Adicionar um elemento em uma posição da coleção
    posAdd = 0
    if opc == 2: #condicional para caso o usuário escolha a opção 2
      elem = int(input("\nDigite um elemento: "))
      posicao = int(input("\nDigite a posição para inserí-lo: "))
      while posicao > qtd: #enquanto posição for menor que a quantidade de elementos válidos no vetor, o usuário deverá digitar novamente
        posicao = int(input("Insira novamente: "))

      posAdd = addPosicao(colecao,qtd,elem,posicao)
      if posAdd > qtd:
        qtd = posAdd
    
    # Remover um elemento em uma posição na coleção
    if opc == 3: #condicional para caso o usuário escolha a opção 3
      posicaoRemov = int(input("\nInsira a posição a ser removida: "))
      while posicaoRemov > qtd-1:
        posicaoRemov = int(input("Insira a posição novamente: "))
      qtd = removerPos(colecao,qtd,posicaoRemov)
    
    # Remover a primeira ocorrência do elemento na coleção
    if opc == 4: #condicional para caso o usuário escolha a opção 4
      elemRemov = int(input("\nInsira o elemento: "))
      qtd = remover1Ocorrencia(colecao,qtd,elemRemov) 

    #Remover todas as ocorrências de um elemento na coleção
    if opc == 5: #condicional para caso o usuário escolha a opção 5
      elemRemov = int(input("\nInsira o elemento: "))
      qtd = removerTodos(colecao,qtd,elemRemov)

    #Verificar se dado um elemento está contido na coleção
    if opc == 6: #condicional para caso o usuário escolha a opção 6
      elem_busca = int(input("\nInsira o elemento que deseja buscar: "))
      qtd=elem_naColecao(colecao,qtd,elem_busca)
    
    #Verificar se dado um valor existem dois elementos na coleção que somados é igual ao valor informado
    if opc == 7: #condicional para caso o usuário escolha a opção 7
      elem_soma = int(input("\nInsira a soma: "))
      print(soma_igual_elem(colecao,qtd,elem_soma))

    # imprime o vetor colecao
    imprimeColecao(colecao,qtd)
  print("Fim do programa")
      
main()
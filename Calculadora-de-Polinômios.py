def imprimirPoli (grau,poli): #função para imprimir o polinômio
  polinomio = ""
  if poli[0] != 0: #condcional para caso o elemento da posição 0 do polinômio seja diferente de 0
    if poli[0] > 0: #condicional para caso o elemento da posição 0 do polinômio seja maior que 0
      polinomio += str(poli[0]) #o elemento é adicionado na string
    else: #caso não
      polinomio += str("(") + str(poli[0]) + str(")") #o elemento é adicionado na string entre parênteses
  
  if grau > 0: #condicional para caso o grau do polinômio seja maior que 0
    if poli[1] != 0: #condicional para caso o elemento da posição 1 do polinômio seja diferente de 0
      if grau > 0: #condicional para caso o grau do polinômio seja maior que 0
        polinomio += " + " 
        if poli[1] > 0: #condicional para caso o elemento da posição 1 do polinômio seja maior que 0
          polinomio += str(poli[1]) + str("x") #o elemento e x são adicionados na string
        else: #caso não
          polinomio += str("(") + str(poli[1]) + str(")") + "x" #o elemento entre parênteses e x são adicionados na string
  
  if grau > 1: #condicional para caso o grau do polinômio seja maior que 1
    for i in range (2,grau+1): #repetição de 2 até grau
      if poli[i] != 0: #condicional para caso o elemento da posição i do polinômio seja diferente de 0
        polinomio += " + " #adiciona + na string
        if poli[i] != 0: #condicional para caso o elemento da posição i do polinômio seja diferente de 0
          if poli[i] < 0: #condicional para caso o elemento da posição i do polinômio seja menor que 0
            polinomio += str("(") + str(poli[i])+ str(")") #o elemento é adicionado na string, entre parênteses
            polinomio += "x^" #x^é adicionado na string
          else: #caso não
            polinomio += str(poli[i]) + "x^" #apenas x^é adicionado na string
          if i == grau: #condicional para caso i ser igual o grau do polinômio
            polinomio += str(i) + " " #adiciona o i e um espaço na string
          else: #caso não
            polinomio += str(i) #adiciona apenas o i
  return polinomio #retorna a string

def calcValor (grau,poli,x): #função para calcular o valor do polinômio
  soma = 0 #variável para armazenar a soma
  for i in range (grau+1): #repetição de 0 até grau
    soma += poli[i](x*i) #equação da soma é armazenada na variável
  return soma #retorna a soma

def soma (grau,poli,grau2,poli2): #função para calcular a soma de dois polinômios
  if grau == grau2: #condicional para caso o grau do polinômio 1 seja igual ao grau do polinômio 2
    grau3 = grau #variável para armazenar o grau do polinõmio resultante da soma
    poli3 = [0]*(grau3+1) #criação do polinômio 3
    for i in range (grau+1): #repetição de 0 até grau
      poli3[i] = poli[i] + poli2[i] #soma do polinômio 1 e 2 sendo armazenada no polinômio 3
  elif grau > grau2: #condicional para caso o grau do polinômio 1 seja maior que o grau do polinômio 2
    grau3 = grau #variável para armazenar o grau do polinômio resultante da soma
    poli3 = [0]*(grau3+1) #criação do polinômio 3
    for i in range (grau2+1):  #repetição de 0 até grau2
      poli3[i] = poli[i] + poli2[i] #soma do polinômio 1 e 2 sendo armazenada no polinômio 3
    for x in range (grau2+1,grau+1): #repetiçao da posição seguinte da última do grau 2 até grau
      poli3[x] = poli[x] #o espaço restante do polinômio 3 é preeenchido com o restante do polinômio 1 que não se modificou na soma
  else: #caso não
    grau3 = grau2 #variável para armazenar o grau do polinômio 3
    poli3 = [0]*(grau3+1) #criação do polinômio 3
    for i in range (grau+1): #repetição de 0 até grau
      poli3[i] = poli[i] + poli2[i] #soma dos polinômios 1 e 2 sendo armazenada no polinômio 3
    for x in range (grau+1,grau2+1): #repetição da posição seguinte da última do grau até grau 2 
      poli3[x] = poli2[x] #o espaço restante do polinômio 3 é preeenchido com o restante do polinômio 2 que não se modificou na soma
  return imprimirPoli (grau3,poli3) #retorna o polinômio 3

def multi(poli,poli4): #função para multiplicar 2 polinômios
  poli5 = [0]*(len(poli) + len(poli4) - 1) #criação do polinômio 5
  grau5 = len(poli5)-1 #variável para armazenar o grau do polinômio 5
  for i in range (len(poli)): #repetiçao de 0 até o final do polinômio 1
    for j in range (len(poli4)): #repetição de 0 até o final do polinômio 4
      poli5[i+j] += poli[i] * poli4[j] #equação da multiplicação entre o polinômio 1 e o 4 sendo armazenada no polinômio 5
  return imprimirPoli (grau5,poli5) #retorna o polinômio 5

def main(): #função principal
  grau = int(input("\nInsira o grau do polinômio: ")) #input para o usuário digitar o grau do polinômio 1
  poli = [0]*(grau+1) #criação do polinômio 1
  for i in range (grau+1): #repetição de 0 até grau
    print("\nInsira o coeficiente do grau",i) #imprime a mensagem
    poli[i] = int(input()) #input para o usuário digitar os elementos do polinômio 1
  
  print("\nP(x) =",imprimirPoli(grau,poli)) #imprime o polinômio 1
  opc = 0 #variável para armazenar a opção do usuário

  while opc != 4: #repetição para enquanto a opção for diferente de 4
    print("\n1 - Calcular o valor de polinômio") #imprime a mensagem
    print("2 - Calcular a soma de polinômios") #imprime a mensagem
    print("3 - Calcular a multiplicação de polinômios") #imprime a mensagem#imprime a mensagem
    print("4 - Sair") #imprime a mensagem
    opc = int(input("\nInsira a opção: ")) #input para o usuário digitar sua opção
  
    if opc == 1: #condicional para caso a opção seja igual a 1
      x = int(input("\nInsira o valor de x: ")) #input para o usuário digitar o valor de x
      print("\nP(x) =",imprimirPoli(grau,poli)) #imprime o polinômio 1
      print("P (",x,") =",calcValor(grau,poli,x) #chama a função

    if opc == 2: #condicional para caso a opção seja igual a 2
      grau2 = int(input("\nInsira o grau do polinômio 2: ")) #input para o usuário digitar o grau do polinômioo 2
      poli2 = [0]*(grau2+1) #criação do polinômio 2
      for i in range (grau2+1): #repetição de 0 até o grau do polinômio 2
        print("\nInsira o coeficiente do grau",i)
        poli2[i] = int(input()) #input para o usuário digitar os elementos do polinõmio 2
      print("\nP(x) =",imprimirPoli(grau,poli)) #imprime o polinômio 1
      print("Q(x) =",imprimirPoli(grau2,poli2)) #imprime o polinômio 2
      print("\nP(x) + Q(x) =",soma(grau,poli,grau2,poli2)) #imprime o polinômio resultante da soma dos 2 polinômios

    if opc == 3: #condicional para caso a opção seja igual a 2
      grau4 = int(input("\nInsira o grau do polinômio 2: ")) #input para o usuário digitar o grau do polinômio 4
      poli4 = [0]*(grau4+1) #criação do polinômio 4
      for i in range (grau4+1): #repetição de 0 até grau 4
        print("\nInsira o coeficiente do grau",i)
        poli4[i] = int(input()) #input para o usuário digitar os elementos do polinômio 4
      print("\nP(x) =",imprimirPoli(grau,poli)) #imprime o polinômio 1
      print("Q(x) =",imprimirPoli(grau4,poli4)) #imprime o polinômio 4
      print("\nP(x) * Q(x) =",multi(poli,poli4)) #imprime o polinômio resultante da multiplicação dos polinômios 1 e 4
      
    if opc < 1 or opc > 4: #condicional para caso a opção que o usuário digita seja menor que 1 ou maior que 4
      print("\nOpção inválida")

  print("\nFim do programa")

main() #chama a função principal
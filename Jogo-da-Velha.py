def initialize(Mat):
  for i in range(3):
    linha=[""]*3
    Mat.append(linha)
  return Mat

def printMat(Mat):  
  
  print("\t0    1    2\n") 
  for j in range(3):
    print(j,"",end='')
    for k in range(3):
      if Mat[j][k]=="":
        print(" |_|",end=' ')
      elif Mat[j][k]==1:
        print(" |X|",end=' ')
      elif Mat[j][k]==-1:
        print(" |O|",end=' ')
    print("\n")
  return Mat

def step(Mat,lin,col,cod):
  if Mat[lin][col]!="":
    return False  
  else:
    if cod=="O":
      Mat[lin][col]=-1 
    else: 
      Mat[lin][col]=1
    return True
    
def status(Mat,cod):
  cont=0
  if Mat[0][0]==-1 and Mat[0][1]==-1 and Mat[0][2]==-1:
    return 1
  elif Mat[1][0]==-1 and Mat[1][1]==-1 and Mat[1][2]==-1:
    return 1
  elif Mat[2][0]==-1 and Mat[2][1]==-1 and Mat[2][2]==-1:
    return 1
  elif Mat[0][0]==-1 and Mat[1][0]==-1 and Mat[2][0]==-1:
    return 1
  elif Mat[0][1]==-1 and Mat[1][1]==-1 and Mat[2][1]==-1:
    return 1
  elif Mat[0][2]==-1 and Mat[1][2]==-1 and Mat[2][2]==-1:
    return 1
  elif Mat[0][0]==-1 and Mat[1][1]==-1 and Mat[2][2]==-1:
    return 1
  elif Mat[0][2]==-1 and Mat[1][1]==-1 and Mat[2][0]==-1:
    return 1
  elif Mat[0][0]==1 and Mat[0][1]==1 and Mat[0][2]==1:
    return 2
  elif Mat[1][0]==1 and Mat[1][1]==1 and Mat[1][2]==1:
    return 2
  elif Mat[2][0]==1 and Mat[2][1]==1 and Mat[2][2]==1:
    return 2
  elif Mat[0][0]==1 and Mat[1][0]==1 and Mat[2][0]==1:
    return 2
  elif Mat[0][1]==1 and Mat[1][1]==1 and Mat[2][1]==1:
    return 2
  elif Mat[0][2]==1 and Mat[1][2]==1 and Mat[2][2]==1:
    return 2
  elif Mat[0][0]==1 and Mat[1][1]==1 and Mat[2][2]==1:
    return 2
  elif Mat[0][2]==1 and Mat[1][1]==1 and Mat[2][0]==1:
    return 2
  for m in range(3):
    for n in range(3):
      if Mat[m][n]==1 or Mat[m][n]==-1:
        cont+=1
  if cont == 9:
    return 0
  else:
    return -1      

  
def game():
  Mat=[]
  initialize(Mat)
  stop=""
  while stop=="":
    jog=0
    printMat(Mat)
    while stop=="":
      if jog%2==0:
        print("Vez do jogador O")
        cod="O"
      else: 
        print("\nVez do jogador X")
        cod="X"
      lin=int(input("\nDigite a linha: "))
      col=int(input("Digite a coluna: "))
      while lin<0 or lin>2:
        print("Linha inválida")
        lin=int(input("Digite a linha novamente: "))
      while col<0 or col>2:
        print("Coluna inválida")
        col=int(input("Digite a coluna novamente: "))
        print("\n")
      if step(Mat,lin,col,cod)==False:
        jog-=1
        print("Posição inválida")
      else:
        printMat(Mat)  
      if status(Mat,cod)==1:
        print("\nO jogador O venceu")
        stop=True
      elif status(Mat,cod)==2:
        print("\nO jogador X venceu")
        stop=True
      elif status(Mat,cod)==0:
        print("\nO jogo empatou")
        stop=True 
      jog+=1
  stop+=1


game()

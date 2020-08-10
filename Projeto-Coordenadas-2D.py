import math #importa a biblioteca math

distMenor=1000
distMaior=0
pMenorx=0
pMenory=0
pMaiorx=0
pMaiory=0
cont_1quad=0
cont_2quad=0
cont_3quad=0
cont_4quad=0

def menor_distancia(): #função para calcular a menor distância
  global distMenor
  global pMenorx
  global pMenory
  global dist_xy

  dist_xy=math.sqrt(((X-px)**2)+(Y-py)**2) #armazena a equação em uma variável

  if dist_xy<distMenor: #condicional para caso a distância calculada seja menor que a atual menor distância
    distMenor=dist_xy #armazena a nova menor distância na variável de menor distância
    pMenorx=px #armazena o menor ponto x na variável de menor ponto x
    pMenory=py #armazena o menor ponto y na variável de menor ponto y

def maior_distancia(): #função para calcular a maior distância
  global distMaior
  global pMaiorx
  global pMaiory

  if dist_xy>distMaior: #condicional para caso a distância calculada seja maior que a atual maior distância
    distMaior=dist_xy #armanzena a nova maior distância na variável de maior distância
    pMaiorx=px #armazena o maior ponto x na variável de maior ponto x
    pMaiory=py #armazena o maior ponto y na variável de maior ponto y    

def percentual(): #função para calcular o percentual de pontos em cada quadrante
  global porcent1
  global porcent2
  global porcent3
  global porcent4

  porcent1=(cont_1quad/N)*100 #equação para calcular a porcentagem de pontos no 1º quadrante
  porcent2=(cont_2quad/N)*100 #equação para calcular a porcentagem de pontos no 2º quadrante
  porcent3=(cont_3quad/N)*100 #equação para calcular a porcentagem de pontos no 3º quadrante	
  porcent4=(cont_4quad/N)*100 #equação para calcular a porcentagem de pontos no 4º quadrante

N=int(input("Digite a quantidade de pontos do seu plano cartesiano: ")) #variável para o usuário preencher quantos pontos quer no seu plano
X=int(input("\nDigite a coordenada X da sua origem translada: ")) #variável para o usuário preencher o novo ponto de origem da abcissa
Y=int(input("Digite a coordenada Y da sua origem translada: ")) #variável para o usuário preencher o novo ponto de origem da ordenada

for i in range(N): #repetição para o usuário preencher os pontos do plano, e rodar as condicionais de cada quadrante   
  px=(int(input("\nDigite a coordenada x do seu ponto: "))) #variável para o usuário preencher o ponto da abcissa
  py=(int(input("Digite a coordenada y do seu ponto: "))) #variável para o usuário preencher o ponto da ordenada

  if px>X and py>Y: #condicional para caso o ponto esteja no 1º quadrante
    cont_1quad+=1 #contador para marcar quantos pontos estão no 1º quadrante
    print("\nO ponto (",px,",",py,") faz parte do 1º quadrante.")

  elif px<X and py>Y: #condicional para caso o ponto esteja no 2º quadrante
    cont_2quad+=1 #contador para marcar quantos pontos estão no 2º quadrante 
    print("\nO ponto (",px,",",py,") faz parte do 2º quadrante.") 

  elif px<X and py<Y: #condicional para caso o ponto esteja no 3º quadrante
    cont_3quad+=1 #contador para marcar quantos pontos estão no 3º quadrante
    print("\nO ponto (",px,",",py,") faz parte do 3º quadrante.")

  elif px>X and py<Y: #condicional para caso o ponto esteja no 4º quadrante
    cont_4quad+=1 #contador para marcar quantos pontos estão no 4° quadrante   
    print("\nO ponto (",px,",",py,") faz parte do 4º quadrante.")

  elif px==X or py==Y: #condicional para caso o ponto esteja na origem
    print("\nO ponto (",px,",",py,") faz parte da origem.")

  else: #condicional para caso o ponto não esteja em nenhuma das outras posições 
    print("\nPonto inválido.")

  menor_distancia() #chama a função
  maior_distancia() #chama a função
  percentual() #chama a função

print("\nA menor distância é a do ponto (",pMenorx,",",pMenory,") de",(format(distMenor,".2f")))
print("\nA maior distância é a do ponto (",pMaiorx,",",pMaiory,") de",(format(distMaior,".2f")))
print("\nA porcentagem de pontos no 1º quadrante é de: ",porcent1,"%")
print("\nA porcentagem de pontos no 2º quadrante é de: ",porcent2,"%")
print("\nA porcentagem de pontos no 3º quadrante é de: ",porcent3,"%")
print("\nA porcentagem de pontos no 4º quadrante é de: ",porcent4,"%")
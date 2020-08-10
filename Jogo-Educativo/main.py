#JogoEdVest.py 
#Autores: Caroline Taus, Isabela Marim, Nathalia Papst, Rebecca Mello

import qs_fuv
import qs_mack
import tab
import sys
import time

c = 0
pontos = 0



def nivel():     #Função para selecionar nível
    print("Você deseja jogar o Nível FUVEST ou Nível MACKENZIE?") 
    print("Digite 1 para FUVEST")
    print("Digite 2 para MACKENZIE")
    FuvouMack= input()
    while FuvouMack != "1" and FuvouMack != "2":
        print("Digite 1 para FUVEST")
        print("Digite 2 para MACKENZIE")
        FuvouMack= input()

    if FuvouMack == "1":
        nivelFUV()

    elif FuvouMack == "2":
        nivelMACK()


def fuvest():    #Função para nível Fuvest
  return qs_fuv.perguntas()


def mack():    #Função para nível Mack
  return qs_mack.perguntas()


def tabuleiro():
  global c
  if c == 0:
    print(tab.Tab0())
  elif c == 3:
    print(tab.Tab3())
  elif c == 6:
    print(tab.Tab6())
  elif c == 9:
    print(tab.Tab9())
  elif c == 12:
    print(tab.Tab12())
  elif c == 15:
    print(tab.Tab15())
  elif c == 18:
    print(tab.Tab18())
  elif c == 21:
    print(tab.Tab21())
  elif c == 24:
    print(tab.Tab24())
  elif c == 27:
    print(tab.Tab27())
  elif c == 30:
    print(tab.Tab30())

  return "\n"


def nivelFUV():
  global c
  tabuleiro()
  for i in range (10):
    time.sleep(1)
    fuvest()
    casa = qs_fuv.casinha()
    pontos = qs_fuv.pontinho()
    
    c = casa
    time.sleep(2)
    tabuleiro()
  print("\033[1;32m") 
  print("Você acertou",pontos,"de 10 perguntas!")
  print("\033[0;0m")
  print() 
  print("-----------------------------------------------")
  print()
  if pontos >= 0 and pontos <=4:
    finalruim()
  elif pontos == 5 or pontos == 6:
    finalmed() 
  elif pontos >=7:
    finalbom()
  

def nivelMACK():
  global c
  tabuleiro()
  for i in range (10):
    time.sleep(1)
    mack()
    casa = qs_mack.casinha()
    pontos = qs_mack.pontinho()
    c = casa
    time.sleep(2)
    tabuleiro() 
  print("\033[1;32m")
  print("Você acertou",pontos,"de 10 perguntas!")
  print("\033[0;0m")
  print() 
  print("-----------------------------------------------")
  print()
  if pontos >= 0 and pontos <=4:
    finalruim()
  elif pontos == 5 or pontos == 6:
    finalmed() 
  elif pontos >=7:
    finalbom()




def regras():
  print("Esse jogo é voltado para alunos vestibulandos que desejam treinar seus conhecimentos de química, física e biologia com questões da Fuvest ou do Mackenzie.")
  print("")
  time.sleep(1)
  print("Digite 1 para JOGAR ou 2 para SAIR:")
  d = int(input())
  while d != 1 and d != 2:
    print("Digite 1 para JOGAR ou 2 para SAIR:")
    d = int(input())
  if d == 2:
    sys.exit()

  print("\n")
  
def historia():
  
  print("Você acorda em uma sala desconhecida, com nada além de escuridão a sua volta. Ao olhar para o chão você percebe que está em pé sobre um quadrado escrito 'INÍCIO'. Esse quadrado está conectado a diversos outros quadrados, cada um com um número em ordem crescente. Ao tentar caminhar para frente você se depara com uma força invisível, proibindo seu avanço. A sua frente uma mensagem aparece como um holograma.")
  time.sleep(2)
  print("\033[36m")
  print(" __________________________________________")
  print("|                                          |")
  print("| Para escapar você deve responder         | ")
  print("| 10 perguntas, sendo que cada certa você  |")
  print("| avança 3 casas. Seu objetivo é chegar ao |")
  print("| final do tabuleiro.                      | ")
  print("| Você pode escolher o nível das perguntas |")
  print("| que responderá. Boa sorte!               |")
  print("|________________________________________ _|")
  print("")
  print("\033[0m")

def finalbom(): #acerto de 7 a 10 perguntas
  time.sleep(2)
  print("\033[36m")
  print("Você acorda repentimente e percebe que dormiu sentado em sua escrivaninha com a cabeça apoiada em livros enquanto estudava. Você tem uma vaga lembrança de um sonho, que se dissipa em segundos. Mesmo com a soneca acidental você acha que a sessão de estudos rendeu, e se sente um pouco mais preparado para o vestibular. ")
  print("\033[0m")

def finalmed(): #acerto de 5 ou 6 perguntas
  time.sleep(2)
  print("\033[36m")
  print("Você acorda repentimente e percebe que dormiu sentado em sua escrivaninha com a cabeça apoiada em livros enquanto estudava. Você tem uma vaga lembrança de um sonho, que se dissipa em segundos. Você sente que ainda terá muitas noites cansativas de estudos como essa para se preparar para o vestibular, mas que está no caminho certo. ")
  print("\033[0m")

def finalruim(): #acerto de 0 a 4 perguntas 
  time.sleep(2)
  print("\033[36m")
  print("Você acorda repentimente e percebe que dormiu sentado em sua escrivaninha com a cabeça apoiada em livros enquanto estudava. Você tem uma vaga lembrança de um pesadelo, que se dissipa em segundos. Você se sente inseguro e despreparado para o vestibular, e, não querendo perder mais tempo, decide continuar os estudos. ")
  print("\033[0m")

def main():

  regras()
  historia()
  nivel()

main()
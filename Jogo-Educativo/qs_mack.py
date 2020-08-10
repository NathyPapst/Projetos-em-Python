import random
import time
casa = 0
pontos = 0

#QUESTÕES MACK
#BANCO DE QUESTÕES 
#1 a 10 fisica, 11 a 20 bio 21 a 29 quim

def pergunta1():
    global casa
    global pontos
    print("Um navio flutua porque")
    print()
    time.sleep(1)
    print("A- seu peso é pequeno quando comparado com seu volume.")
    print("B- seu volume é igual ao volume do líquido deslocado.") 
    print("C- o peso do volume do líquido deslocado é igual ao peso do navio.") #alt certa
    print("D- o peso do navio é menor que o peso do líquido deslocado.")
    print("E- o peso do navio é maior que o peso do líquido deslocado.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "C":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é C.")
    return "\n"

def pergunta2():
    global casa
    global pontos
    print("Considere as seguintes afirmações, admitindo que em uma região do espaço está presente uma carga geradora de campo elétrico (Q) e uma carga de prova (q) nas suas proximidades.")
    print()
    print("I. Quando a carga de prova tem sinal negativo (q<0), os vetores força e campo elétrico têm mesma direção e sentido.")
    print("II. Quando a carga de prova tem sinal positivo (q>0), os vetores força e campo elétrico têm mesma direção e sentido.")
    print("III. Quando a carga geradora do campo tem sinal positivo (Q>0), o vetor campo elétrico tem, sentido de afastamento da carga geradora e quando tem sinal negativo (Q<0), tem sentido de aproximação, independente do sinal que possua a carga da prova.")
    print()
    print("Assinale")
    print()
    time.sleep(1)
    print("A- se todas as afirmações são verdadeiras.") #alt certa
    print("B- se apenas as afirmações I e II são verdadeiras.") 
    print("C- se apenas a afirmação III é verdadeira.")
    print("D- se apenas as afirmações II e III são verdadeiras.")
    print("E- se todas as afirmações são falsas.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "A":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é A.")
    return "\n"

def pergunta3():
    global casa
    global pontos
    print("Uma pessoa abre a geladeira, verifica o que há dentro e depois fecha a porta dessa geladeira. Em seguida, ela tenta abrir novamente, mas só consegue depois de exercer uma força mais intensa do que o habitual.")
    print("A dificuldade extra para abrir a geladeira ocorre porque o(a)")
    print()
    time.sleep(1)
    print("A- O volume de ar dentro da geladeira diminuiu.")
    print("B- O motor da geladeira está funcionando com potência máxima.") 
    print("C- Força exercida pelo ímã na porta da geladeira aumenta.")
    print("D- Pressão no interior da geladeira está abaixo da pressão externa.") #alt certa
    print("E- Nenhuma das alternativas.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "D":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é D.")
    return "\n"

def pergunta4():
    global casa
    global pontos
    print("Se todos os outros fatores são mantidos constantes, a resistência elétrica de um fio de seção transversal uniforme:")
    print()
    time.sleep(1)
    print("A- Aumenta se o comprimento do fio diminuir.")
    print("B- Diminui se a área da seção transversal do fio diminuir") 
    print("C- Aumenta se a área da seção transversal do fio diminuir.") #alt certa
    print("D- Diminui se o comprimento do fio aumentar.")
    print("E- Não varia se o comprimento do fio aumentar.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "C":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é C.")
    return "\n"


def pergunta5():
    global casa
    global pontos
    print("Três lâmpadas, L1, L2 e L3, com potências de 4 W, 12 W e 8 W, respectivamente, são conectadas em série através de uma bateria de 12 V . Podemos afirmar que a voltagem na lâmpada L2 vale:")
    print()
    time.sleep(1)
    print("A- 8 V.")
    print("B- 4 V.") 
    print("C- 3 V.")
    print("D- 6 V.") #alt certa
    print("E- 2 V.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "D":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é D.")
    return "\n"

def pergunta6():
    global casa
    global pontos
    print("Duas rodas são acopladas de modo que suas bandas de rodagem sejam tangentes, como ilustra a figura acima. O movimento ocorre devido ao atrito entre as superfícies em contato. Considerando que não haja escorregamento relativo entre as rodas, o raio da roda menor (R2) é a metade do raio da roda maior (R1) e elas realizam um movimento circular uniforme, podemos afirmar que")
    print()
    time.sleep(1)
    print("A- o deslocamento angular da roda maior é a metade da roda menor e seu sentido de rotação é oposto ao da roda menor.") #alt certa
    print("B- o deslocamento angular da roda maior é o dobro da roda menor e seu sentido de rotação é oposto ao da roda menor.") 
    print("C- o deslocamento angular da roda maior é a metade da roda menor e de mesmo sentido de rotação da roda menor.")
    print("D- o deslocamento angular da roda maior é o dobro da roda menor e de mesmo sentido de rotação da roda menor.")
    print("E- o deslocamento angular da roda maior é o mesmo da roda menor e de mesmo sentido de rotação da roda menor.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "A":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é A.")
    return "\n"

def pergunta7():
    global casa
    global pontos
    print("Dois corpos A e B de massas ma= 1,0 kg e mb = 1,0.10^3 kg, respectivamente, são abandonados de uma mesma altura h, no interior de um tubo vertical onde existe o vácuo. Para percorrer a altura h,")
    print()
    time.sleep(1)
    print("A- o tempo de queda do corpo é igual que o do corpo B.") #alt certa
    print("B- o tempo de queda do corpo A é maior que o do corpo B.") 
    print("C- o tempo de que dado corpo A é menor que o do corpo B.")
    print("D- o tempo de queda depende do volume dos corpos A e B.")
    print("E- Ao tempo de queda depende da forma geométrica dos corpos A e B.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "A":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é A.")
    return "\n"

def pergunta8():
    global casa
    global pontos
    print("Uma garota encontra-se diante de um espelho esférico côncavo e observa que a imagem direita de seu rosto é ampliada duas vezes. O rosto da garota só pode estar")
    print()
    time.sleep(1)
    print("A- entre o centro de curvatura e o foco do espelho côncavo.")
    print("B- sobre o centro de curvatura do espelho côncavo.") 
    print("C- entre o foco e o vértice do espelho côncavo.") #alt certa
    print("D- sobre o foco do espelho côncavo.")
    print("E- antes do centro de curvatura do espelho côncavo.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "C":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é C.")
    return "\n"

def pergunta9():
    global casa
    global pontos
    print("Uma garota encontra-se diante de um espelho esférico côncavo e observa que a imagem direita de seu rosto é ampliada duas vezes. O rosto da garota só pode estar")
    print()
    time.sleep(1)
    print("A- entre o centro de curvatura e o foco do espelho côncavo.")
    print("B- sobre o centro de curvatura do espelho côncavo.") 
    print("C- entre o foco e o vértice do espelho côncavo.")
    print("D- sobre o foco do espelho côncavo.")
    print("E- antes do centro de curvatura do espelho côncavo.") #alt certa
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "E":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é E.")
    return "\n"

def pergunta10():
    global casa
    global pontos
    print("A lupa é um instrumento óptico conhecido popularmente por Lente de Aumento, mas também denominada microscópio simples. Ela consiste de uma lente __________ de pequena distância focal e, para ser utilizada com o seu fim específico, o objeto a ser observado por meio dela deverá ser colocado sobre o eixo principal, entre o seu __________ e o seu __________. As lacunas são preenchidas corretamente quando se utilizam, na ordem de leitura, as informações")
    print()
    time.sleep(1)
    print("A- convergente, centro óptico e foco principal objeto.") #alt certa
    print("B- convergente, ponto antiprincipal objeto e foco principal objeto.") 
    print("C- divergente, centro óptico e foco principal objeto.")
    print("D- divergente, ponto antiprincipal objeto e foco principal objeto.")
    print("E- convergente, ponto antiprincipal imagem e foco principal imagem.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "A":
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é A.")
    return "\n"

#BIOLOGIA

def pergunta11(): 
    global casa
    global pontos
    print("Assinale a alternativa correta a respeito do ciclo de vida das plantas criptógamas (briófitas e pteridófitas) e fanerógamas (gimnospermas e angiospermas).")
    print()
    time.sleep(1)
    print("A- Apresentam alternância de gerações, sendo que a fase esporofítica predomina sobre a gametofitica.")
    print("B- Somente as angiospermas formam tubo polínico a partir do grão-de-pólen.") 
    print("C- Nas angiospermas, ocorre dupla fecundação, originando um embrião 2n e endosperma 3n.") #alt certa 
    print("D- Nas fanerógamas, o óvulo dá origem à semente e o ovário dá origem ao fruto.")
    print("E- Nas angiospermas, as flores são sempre monoclinas (de sexos separados).")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "C": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é C.") 
    return "\n"

def pergunta12(): #pode deixar aqui como MOD msm
    global casa
    global pontos
    print("Hepatite é toda e qualquer inflamação do fígado, que pode resultar desde uma simples alteração fisiológica, até uma doença fulminante e fatal. Os tipos mais conhecidos são as hepatites A, Be €. A grande maioria das hepatites agudas é assintomática ou leva a sintomas inespecíficos como febre, mal estar, desânimo e dores musculares. Outras doenças, como a leptospirose, a malária a febre amarela, têm sintomas semelhantes.") 
    print("Hepatite A, leptospirose, malária e febre amarela são causadas, respectivamente, por:")
    time.sleep(1)
    print("A- bactéria, bactéria, protozoário e bactéria.")
    print("B- bactéria, vírus, protozoário e vírus.")  
    print("C- vírus, bactéria, protozoário e bactéria.")
    print("D- vírus, bactéria, protozoário e vírus.") #alt certa
    print("E- bactéria, protozoário, protozoário e vírus.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "D": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é D.") 
    return "\n"

def pergunta13(): 
    global casa
    global pontos
    print("A dengue, a zika e a chikungunya são 3 doenças que circulam no Brasil transmitidas pelo mesmo vetor, o mosquito Áedes aegypti. A respeito dessas doenças, considere as seguintes afirmações:")
    print()
    print("I. A picada do mosquito é a única forma de transmissão dos vírus que causam essas doenças.")
    print("II. A transmissão do vírus ocorre somente pela picada da fêmea do mosquito.")
    print("III. A fémea do mosquito “prefere” postar seus ovos em água parada e suja.")
    print("IV. O combate ao mosquito é, atualmente, a melhor forma de erradicar essas doenças.")
    print()
    print("Estão corretas, apenas,") 
    print()
    time.sleep(1)
    print("A- II e IV.") #alt certa
    print("B- I e II.")  
    print("C- II e III.")
    print("D- I, II e III.")
    print("E- I, II e IV")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "A": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é A.") 
    return "\n"

def pergunta14(): 
    global casa
    global pontos
    print("Um estudo coordenado por um hospital paulista está acompanhando os pacientes submetidos à cirurgia de substituição de válvulas cardíacas. Um estudo semelhante já havia sido realizado para avaliação do uso de stents, “molas” que mantêm as coronárias abertas. É correto afirmar que")
    print()
    time.sleep(1)
    print("A- as coronárias são vasos que conduzem sangue do coração para os pulmões.")
    print("B- no coração são encontradas válvulas entre os átrios e ventrículos e na base das artérias.") #alt certa 
    print("C-  as válvulas são responsáveis pelo controle da frequência cardíaca.")
    print("D- na circulação periférica as válvulas são abundantes nas artérias.")
    print("o uso de stents é uma alternativa para as cirurgias de troca de válvulas.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "B": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é B.") 
    return "\n"

def pergunta15(): 
    global casa
    global pontos
    print("A respeito do pâncreas, assinale a alternativa correta.") 
    print()
    time.sleep(1)
    print("A- É a única glândula mista existente no organismo.")
    print("B- Um de seus hormônios é responsável pelo controle da quantidade de água eliminada pela urina.") 
    print("C- O controle da secreção de seus hormônios é realizado por hormônios hipofisários.")
    print("D- A deficiência na produção de um de seus hormônios na infância causa o nanismo.")
    print("E- É responsável pela produção de enzimas digestivas que são secretadas no duodeno.") #alt certa 
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "E": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é E.") 
    return "\n"

def pergunta16(): 
    global casa
    global pontos
    print("Um ecossistema pode ser representado sob a forma de pirâmides ecológicas de três tipos: de número, de biomassa e de energia. A esse respeito, são feitas as seguintes afirmações:")
    print() 
    print("I. Em todas elas, os produtores ocupam a sua base.")
    print("II. Em um ecossistema equilibrado, a pirâmide de energia sempre apresenta a base maior do que o topo.")
    print("III. A pirâmide de número nunca se apresenta na forma invertida.")
    print("IV. Os decompositores não são mostrados na pirâmide, pois não representam parcela importante no ecossistema.")
    print("Assinale se estão corretas, apenas,")
    print()
    time.sleep(1)
    print("A- I e II.") #alt certa
    print("B- I e III.")  
    print("C- I e IV.")
    print("D- II e III.")
    print("E- II e IV.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "B": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é B.") 
    return "\n"

def pergunta17(): 
    global casa
    global pontos
    print("Um homem daltônico e normal para a miopia tem uma filha também daltônica, mas míope. Sabendo que a mãe da menina não é míope, assinale a alternativa correta.")
    print()
    time.sleep(1)
    print("A- A mãe é certamente daltônica.")
    print("B- A menina é homozigota para ambos os genes.") #alt certa 
    print("C- A miopia é condicionada por um gene dominante.")
    print("D- Todos os filhos do sexo masculino desse homem serão daltônicos.")
    print("E- Essa menina poderá ter filhos de sexo masculino não daltônicos.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "B": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é B.") 
    return "\n"

def pergunta18(): 
    global casa
    global pontos
    print("Os fungos constituem um grupo de organismos com características que lembram um vegetal, mas com outras que lembram um animal. Foram, no passado, considerados como vegetais e, atualmente, são colocados em um reino próprio, o Reino Fungi. A respeito deles é correto afirmar que são seres")
    print()
    time.sleep(1)
    print("A- procariontes, uni ou pluricelulares, sempre autótrofos.")
    print("B- procariontes, uni ou pluricelulares, autótrofos e heterótrofos.")  
    print("C- eucariontes, uni ou pluricelulares, sempre heterótrofos.") #alt certa
    print("D- eucariontes, pluricelulares, autótrofos e heterótrofos.")
    print("E- eucariontes, pluricelulares, sempre autótrofos.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "C": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é C.") 
    return "\n"

def pergunta19(): 
    global casa
    global pontos
    print("A atmosfera terrestre é constituída por vários tipos de gases. O oxigênio, o gás carbônico e o nitrogênio são os mais envolvidos no metabolismo dos seres vivos. Os únicos organismos, capazes de utilizar esses gases diretamente da atmosfera,pertencem ao Reino") 
    print()
    time.sleep(1)
    print("A- Metafita")
    print("B- Metazoa") 
    print("C- Fungi")
    print("D- Monera") #alt certa 
    print("E- Protista")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "D": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é D.")
    return "\n"

def pergunta20(): 
    global casa
    global pontos
    print("O aumento da perda de água por transpiração tem como principal consequência") 
    print()
    time.sleep(1)
    print("A- o aumento da produção de células sanguíneas, visando provocar aumento de pressão arterial.")
    print("B- a diminuição da frequência respiratória, visando diminuir a perda de água na respiração.") 
    print("C- o aumento da reabsorção de água pelo intestino.")
    print("D- a diminuição da velocidade dos movimentos peristálticos.")
    print("E- o aumento da produção de ADH, visando diminuir a produção de urina.") #alt certa
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "E": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é E.") 
    return "\n"



def pergunta21(): 
    global casa
    global pontos
    print("Considere as seguintes substâncias orgânicas:\nI. CH3COOH\nII. CH2ClCOOH\nIII. CH3CH2COOH\nIV. CCl3COOH\nAssinale a alternativa correta para a ordem crescente de caráter ácido dessas substâncias") 
    print()
    time.sleep(1)
    print("A- III<I<II<IV")#alt certa
    print("B- I<III<II<IV")  
    print("C- IV<II<I<III")
    print("D- II<IV<III<I")
    print("E- IV<III<II<I")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "A": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é A.") 
    return "\n"

def pergunta22(): 
    global casa
    global pontos
    print("As reações entre ácidos e bases produzem sal e água e são classificadas como reações de neutralização, que pode ser parcial ou total. Abaixo estão representadas três equações incompletas entre um ácido e uma base.\nI. H3PO4 + KOH →\nII. HNO3 + Ca(OH)2 →\nIII. H2SO4 + NaOH →\nSendo assim, as fórmulas químicas dos sais obtidos, sob condições ideais de reação, a partir da neutralização entre iguais quantidades em mols de cada uma das espécies representadas nas equações acima, são, respectivamente,")  
    print()
    time.sleep(1)
    print("A- K2HPO4 ; Ca(OH)NO3 ; NaHSO4")
    print("B- KHPO4 ; CaHNO3 ; Na(OH)SO4") 
    print("C- KH2PO4 ; Ca(OH)NO3 ; NaHSO4")#alt certa
    print("D- K3PO4 ; Ca(NO3)2 ; Na2SO4")
    print("E- KH2PO3 ; Ca(OH)NO3 ; NaHSO4")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "C": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é C.") 
    return "\n"

def pergunta23(): 
    global casa
    global pontos
    print("Assinale (V) para verdadeiro e (F) para falso, para as afirmações abaixo.\n( ) Os metais apresentam alta condutividade elétrica, mas baixa condutividade térmica.\n( ) O bronze é uma liga formada por cobre e estanho.\n( ) Compostos iônicos conduzem corrente elétrica em meio aquoso e quando fundidos.\n( ) A ligação covalente ocorre entre metais e não metais. O KBr é um exemplo.\n( ) O dióxido de carbono é uma molécula apolar, mas que possui ligações covalentes polares.\nA sequência correta de preenchimento dos parênteses, de cima para baixo é")  
    print()
    time.sleep(1)
    print("A- F, F, V, F e V.")
    print("B- F, V, V, F e V.") #alt certa 
    print("C- V, F, V, F e V.")
    print("D- F, F, V, F e F.")
    print("E- V, V, F, V e F")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "B": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é B.") 
    return "\n"

def pergunta24(): 
    global casa
    global pontos
    print("Certa massa fixa de um gás ideal, sob temperatura de 30 °C e pressão de 2 atm. foi submetida a uma transformação isocórica. em que sua temperatura foi aumentada em 150 unidades. Dessa forma, é correto afirmar que, durante a transformação,")  
    print()
    time.sleep(1)
    print("A- além do volume, a pressão manteve-se constante.")
    print("B- apenas o volume permaneceu constante, e no final, a pressão exercida por essa massa gasosa, foi aumentada para aproximadamente 12 atm.") 
    print("C- apenas o volume permaneceu constante, e no final, a pressão exercida por essa massa gasosa, foi aumentada para aproximadamente 3 atm.")#alt certa 
    print("D- apenas o volume permaneceu constante, e no final, a pressão exercida por essa massa gasosa, foi diminuída para aproximadamente 1 atm.")
    print("E- apenas o volume permaneceu constante, e no final, a pressão exercida por essa massa gasosa, foi diminuída para aproximadamente 0,33 atm.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "C": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é C.") 
    return "\n"


def pergunta25(): 
    global casa
    global pontos
    print("A respeito da combustão completa de 1 mol de gás propano, no estado padrão, são feitas as seguintes afirmações:\nI. Trata-se de um processo endotérmico.\nII. Ocorre com liberação de energia para o meio externo.\nIII. Há a formação de 3 mols de dióxido de carbono e 4 mols de água.\nIV. São consumidos 5 mols de gás oxigênio.\nAnalisando-se as afirmações acima, estão corretas somente") 
    print()
    time.sleep(1)
    print("A- I e II.")
    print("B- I, II e III.") 
    print("C- II, III e IV.") #alt certa 
    print("D- I, III e IV.")
    print("E- II e IV.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "C": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é C.") 
    return "\n"

def pergunta26(): 
    global casa
    global pontos
    print("Os alcanos, sob condições adequadas de reação, reagem com o gás cloro (halogenação) formando uma mistura de isômeros de posição monoclorados. Assim, o número de isômeros de posição, com carbono quiral, obtidos a partir da monocloração do 2,5-dimetilexano, em condições adequadas é")  
    print()
    time.sleep(1)
    print("A- 1")
    print("B- 2") #alt certa 
    print("C- 3")
    print("D- 4")
    print("E- 5")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "B": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é B.") 
    return "\n"

def pergunta27(): 
    global casa
    global pontos
    print("Considere a nomenclatura IUPAC dos seguintes hidrocarbonetos.\nI. metil-ciclobutano.\nII. 3-metil-pentano.\nIII. pentano.\nIV. ciclo-hexano.\nV. pent-2-eno.\nA alternativa que relaciona corretamente compostos isoméricos é?")  
    print()
    time.sleep(1)
    print("A- I e III.")
    print("B- III e V.") 
    print("C- I e V.") #alt certa 
    print("D- II e IV.")
    print("E- II e III.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "C": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é C.") 
    return "\n"

def pergunta28(): 
    global casa
    global pontos
    print("Diesel S10 chega aos postos\nVendido a partir do início de janeiro, o diesel S10 substitui o já conhecido diesel S50. O “S” vem de enxofre e o número 10 sinaliza a quantidade desse elemento no combustível, ou seja, o novo diesel contém 10 partes por milhão de enxofre, uma mudança radical se comparado ao diesel S1800, com 1800 partes por milhão de enxofre, comercializado anteriormente. Trata-se de um hidrocarboneto combustível de última geração, já vendido na Europa e fundamental para reduzir a emissão de poluentes (materiais particulados e SO2). A respeito do diesel S10, são feitas as seguintes afirmações:\nI. A combustão completa do diesel S10 produz gás carbônico, água e uma quantidade menor de SO2 em relação ao tipo de diesel anteriormente utilizado comercialmente.\nII. Por gerar energia, a classificação termoquímica do processo de combustão do diesel S10 é endotérmica.\nIII. Considerando a combustão completa, o diesel S10 emite 180 vezes mais gases poluentes derivados do enxofre do que o diesel S1800.\nQuanto às afirmativas,")  
    print()
    time.sleep(1)
    print("A- apenas I é verdadeira.") #alt certa
    print("B- apenas II é verdadeira.")  
    print("C- apenas III é verdadeira.")
    print("D- apenas I e II são verdadeiras.")
    print("E- apenas I e III são verdadeiras.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "A": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é A.") 
    return "\n"

def pergunta29(): 
    global casa
    global pontos
    print("Existe uma classe muito comum de fertilizantes minerais mistos denominada NPK. Essa sigla deve-se à presença na composição desses fertilizantes de substâncias, contendo nitrogênio, fósforo e potássio. O nitrogênio age nas folhas das plantas, bem como em seu crescimento, o fósforo atua na floração e no amadurecimento de frutos além do crescimento das raízes e, finalmente, o potássio, responsável pelo equilíbrio da água no vegetal como também em seu crescimento. Nas embalagens comerciais desses fertilizantes, após a sigla NPK, é citada uma sequência numérica que expressa os percentuais em massa de nitrogênio, fósforo e potássio, respectivamente. Considerando um fertilizante NPK 04-14-08, é correto dizer que, para uma embalagem comercial de 500 g, há:") 
    print()
    time.sleep(1)
    print("A- 40 g de nitrogênio, 140 g de fósforo e 80 g de potássio.")
    print("B- 20 g de nitrogênio, 70 g de fósforo e 40 g de potássio.") #alt certa 
    print("C- 2 g de nitrogênio, 7 g de fósforo e 4 g de potássio.")
    print("D- 4 g de nitrogênio, 14 g de fósforo e 8 g de potássio.")
    print("E- 0,4 g de nitrogênio, 1,4 g de fósforo e 0,8 g de potássio.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "B": 
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é B.") 
    return "\n"

#FUNÇÃO QUE CHAMA PERGUNTAS MACK

def perguntas():
    per = random.randrange(1, 30)

    if per == 1:
        pergunta1()
    elif per == 2:
        pergunta2()
    elif per == 3:
        pergunta3()
    elif per == 4:
        pergunta4()
    elif per == 5:
        pergunta5()
    elif per == 6:
        pergunta6()
    elif per == 7:
        pergunta7()
    elif per == 8:
        pergunta8()
    elif per == 9:
        pergunta9()
    elif per == 10:
        pergunta10()
    elif per == 11:
        pergunta11()
    elif per == 12:
        pergunta12()
    elif per == 13:
        pergunta13()
    elif per == 14:
        pergunta14()
    elif per == 15:
        pergunta15()
    elif per == 16:
        pergunta16()
    elif per == 17:
        pergunta17()
    elif per == 18:
        pergunta18()
    elif per == 19:
        pergunta19()
    elif per == 20:
        pergunta20()
    elif per == 21:
        pergunta21()
    elif per == 22:
        pergunta22()
    elif per == 23:
        pergunta23()
    elif per == 24:
        pergunta24()  
    elif per == 25:
        pergunta25()
    elif per == 26:
        pergunta26()  
    elif per == 27:
        pergunta27()
    elif per == 28:
        pergunta28()
    elif per == 29:
        pergunta29()

    return "\n"

#FUNÇÃO QUE CHAMA CASA
def casinha():
  return casa

#FUNÇÃO QUE CHAMA PONTOS
def pontinho():
  return pontos
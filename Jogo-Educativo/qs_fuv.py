import random
import time
casa = 0
pontos = 0
#QUESTÕES FUVEST
#BANCO DE QUESTÕES 
#perg 1 a 3 bio, 4 a 13 fis, 14 a 23 bio, 24 a 32 quim

def pergunta1():
    global casa
    global pontos
    
    print("Uma ideia comum às teorias da evolução propostas por Darwin e por Lamarck é que a adaptação resulta")
    print()
    time.sleep(1)
    print("A- do sucesso reprodutivo diferencial.")
    print("B- de uso e desuso de estruturas anatômicas.") 
    print("C- da interação entre os organismos e seus ambientes.") #alt certa
    print("D- da manutenção das melhores combinações gênicas.")
    print("E- de mutações gênicas induzidas pelo ambiente.")
    print()
    
    print("Insira a letra referente à sua resposta:")
    alt = input()
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

    print("O anúncio do sequenciamento do genoma humano, em 21 de junho de 2000, significa que os cientistas determinaram ")
    print()
    time.sleep(1)
  
    print("A- a sequência de nucleotídeos dos cromossomos humanos. ") #alt certa
    print("B- todos os tipos de proteína codificados pelos genes humanos. ") 
    print("C- a sequência de aminoácidos do DNA humano. ") 
    print("D- a sequência de aminoácidos de todas as proteínas humanas. ")
    print("E- o número correto de cromossomos da espécie humana.")
    print()

    print("Insira a letra referente à sua resposta:")
    alt = input()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "A":
        print("Você acertou!")
        casa = casa + 3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A resposta correta é A.")
    return "\n"

def pergunta3():
    global casa
    global pontos

    print("Uma pessoa passará a excretar maior quantidade de uréia se aumentar, em sua dieta alimentar, a quantidade de")
    print()
    time.sleep(1)
    print("A- amido.")
    print("B- cloreto de sódio.") 
    print("C- glicídios.")
    print("D- lipídios.")
    print("E- proteínas.") #alt certa
    print()

    print("Insira a letra referente à sua resposta:")
    alt = input()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "E":
        print("Você acertou!")
        casa = casa + 3
        pontos = pontos +1
    else:
        print("Resposta incorreta! A resposta correta é E.")
    return "\n"

def pergunta4():
    global casa
    global pontos
    print("Dirigindo-se a uma cidade próxima, por uma auto-estrada plana, um motorista estima seu tempo de viagem, considerando que consiga manter uma velocidade média de 90 km/h. Ao ser surpreendido pela chuva, decide reduzir sua velocidade média para 60 km/h, permanecendo assim até a chuva parar, quinze minutos mais tarde, quando retorna sua velocidade média inicial. Essa redução temporária aumenta seu tempo de viagem, com relação à estimativa inicial, em:")
    print()
    time.sleep(1)
    print("A- 5 minutos") #alt certa
    print("B- 7,5 minutos") 
    print("C- 10 minutos")
    print("D- 15 minutos")
    print("E- 30 minutos")
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

def pergunta5():
    global casa
    global pontos
    print("Satélites utilizados para telecomunicações são colocados em órbitas geoestacionárias ao redor da Terra, ou seja, de tal forma que permaneçam sempre acima de um mesmo ponto da superfície da Terra. Considere algumas condições que poderiam corresponder a esses satélites:") 
    print()
    print("I – Ter o mesmo período, de cerca de 24 horas")

    print("II – Ter aproximadamente a mesma massa")

    print("III – Estar aproximadamente à mesma altitude")

    print("IV – Manter-se num plano que contenha o círculo do equador terrestre")
    print()
    time.sleep(1)
    print("A- I e III")
    print("B- I, II e III") #alt certa
    print("C- I, III e IV")
    print("D- II e III")
    print("E- II e IV")
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

def pergunta6():
    global casa
    global pontos
    print("Imagine que, no final do século XXI, os habitantes da Lua vivam em um grande complexo pressurizado, em condições equivalentes às da Terra, tendo como única diferença a aceleração da gravidade, que é menor na Lua. Considere as situações imaginadas bem como as possíveis descrições de seus resultados, realizadas dentro desse complexo, na Lua:")
    print()
    print("I – Ao saltar, atinge-se uma altura maior do que quando o salto é realizado na Terra.")
    print("II – Se uma bola está boiando em uma piscina, essa bola manterá maior volume fora da água do que quando a experiência é realizada na Terra.")
    print("III – Em pista horizontal, um carro, com velocidade Vo, consegue parar completamente em uma distância maior do que quando o carro é freado na Terra.")
    print()
    print("Assim, pode-se afirmar que estão corretos apenas os resultados propostos em")
    print()
    time.sleep(1)
    print("A- I")
    print("B- I e II") 
    print("C- I e III") #alt certa
    print("D- II e III")
    print("E- I, II e III")
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

def pergunta7():
    global casa
    global pontos
    print("Um avião, com velocidade constante e horizontal, voando em meio a uma tempestade, repentinamente perde altitude, sendo tragado para baixo e permanecendo com aceleração constante vertical de módulo a > g, em relação ao solo, durante um intervalo de tempo Dt. Pode-se afirmar que, durante esse período, uma bola de futebol que se encontrava solta sobre uma poltrona desocupada")
    print()
    time.sleep(1)
    print("A- permanecerá sobre a poltrona, sem alteração de sua posição inicial.")
    print("B- flutuará no espaço interior do avião, sem aceleração em relação ao mesmo, durante o intervalo de tempo Dt") 
    print("C- será acelerada para cima, em relação ao avião, sem poder se chocar com o teto, independentemente do intervalo de tempo Dt.")
    print("D- será acelerada para cima, em relação ao avião, podendo se chocar com o teto, dependendo do intervalo de tempo Dt.") #alt certa
    print("E- será pressionada contra a poltrona durante o intervalo de tempo Dt.")
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

def pergunta8():
    global casa
    global pontos
    print("Um feixe de elétrons, todos com mesma velocidade, penetra em uma região do espaço onde há um campo elétrico uniforme entre duas placas condutoras, planas e paralelas, uma delas carregada positivamente e a outra, negativamente. Durante todo o percurso, na região entre as placas, os elétrons têm trajetória retilínea, perpendicular ao campo elétrico. Ignorando efeitos gravitacionais, esse movimento é possível se entre as placas houver, além do campo elétrico, também um campo magnético, com intensidade adequada e")
    print()
    time.sleep(1)
    print("A- perpendicular ao campo elétrico e à trajetória dos elétrons.") #alt certa
    print("B- paralelo e de sentido oposto ao do campo elétrico.") 
    print("C- paralelo e de mesmo sentido que o do campo elétrico.")
    print("D- paralelo e de sentido oposto ao da velocidade dos elétrons.")
    print("E- paralelo e de mesmo sentido que o da velocidade dos elétrons.")
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

def pergunta9():
    global casa
    global pontos
    print("Duas esferas metálicas A e B estão próximas uma da outra. A esfera A está ligada à Terra , cujo potencial é nulo, por um fio condutor. A esfera B está isolada e carregada com carga +Q. Considere as seguintes afirmações:")
    print()
    print("I. O potencial da esfera A é nulo.")
    print("II. A carga total da esfera A é nula.")
    print("III. A força elétrica total sobre a esfera A é nula.")
    print()
    print("Está correto apenas o que se afirma em:")
    print()
    time.sleep(1)
    print("A- I") #alt certa
    print("B- I e II") 
    print("C- I e III")
    print("D- II e III")
    print("E- I, II e III")
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

def pergunta10():
    global casa
    global pontos
    print("A lei de conservação da carga elétrica pode ser enunciada como segue:")
    print()
    time.sleep(1)
    print("A- A soma algébrica dos valores das cargas positivas e negativas em um sistema isolado é constante.") #alt certa
    print("B- Um objeto eletrizado positivamente ganha elétrons ao ser aterrado.") 
    print("C- A carga elétrica de um corpo eletrizado é igual a um número inteiro multiplicado pela carga do elétron.")
    print("D- O número de átomos existentes no universo é constante.")
    print("E- As cargas elétricas do próton e do elétron são, em módulo, iguais.")
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

def pergunta11():
    global casa
    global pontos
    print("Em agosto de 1999 ocorreu o último eclipse solar total do século. Um estudante imaginou, então, uma forma de simular eclipses. Pensou em usar um balão esférico e opaco, de 40 m de diâmetro, que ocultaria o Sol quando seguro por uma corda a uma altura de 200 m. Faria as observações, protegendo devidamente sua vista, quando o centro do Sol e o centro do balão estivessem verticalmente colocados sobre ele em um dia de céu claro. Considere as afirmações a seguir em relação aos possíveis resultados dessa proposta, caso as observações fossem realmente feitas, sabendo que a distância da terra ao Sol é de 150.10^6 km e que o Sol tem um diâmetro de 0,75.10^6 km, aproximadamente.")
    print()
    print("I-O balão ocultaria todo o Sol: o estudante não veria diretamente nenhuma parte do Sol.")
    print("II-O balão é pequeno demais: o estudante continuaria a ver diretamente partes do Sol.")
    print("III-O céu ficaria escuro para o estudante, como se fosse noite.")
    print()
    print("Está correto apenas o que se afirma em:")
    print()
    time.sleep(1)
    print("A- I") #alt certa
    print("B- II") 
    print("C- III")
    print("D- I e III")
    print("E- II e III")
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

def pergunta12():
    global casa
    global pontos
    print("Em uma sala fechada e isolada termicamente, uma geladeira, em funcionamento, tem, num dado instante, sua porta completamente aberta. Antes da abertura dessa porta, a temperatura da sala é maior que a do interior da geladeira. Após a abertura da porta, a temperatura da sala,")
    print()
    time.sleep(1)
    print("A- diminui até que o equilíbrio térmico seja estabelecido.")
    print("B- diminui continuamente enquanto a porta permanecer aberta.") 
    print("C- diminui inicialmente, mas, posteriormente, será maior do que quando a porta foi aberta.") #alt certa
    print("D- aumenta inicialmente, mas, posteriormente, será menor do que quando a porta foi aberta.")
    print("E- não se altera, pois se trata de um sistema fechado e termicamente isolado.")
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

def pergunta13():
    global casa
    global pontos
    print("Um amolador de facas, ao operar um esmeril, é atingido por fagulhas incandescentes, mas não se queima. Isso acontece porque as fagulhas:")
    print()
    time.sleep(1)
    print("A- tem calor específico muito grande.")
    print("B- em temperatura muito baixa.") 
    print("C- tem capacidade térmica muito pequena.") #alt certa
    print("D- estão em mudança de estado.")
    print("E- não transportam energia.")
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

def pergunta14(): 
    global casa
    global pontos
    print("No sistema circulatório humano,")
    print()
    time.sleep(1)
    print("A- a veia cava superior transporta sangue pobre em oxigênio, coletado da cabeça, dos braços e da parte superior do tronco, e chega ao átrio esquerdo do coração.")
    print("B- a veia cava inferior transporta sangue pobre em oxigênio, coletado da parte inferior do tronco e dos membros inferiores, e chega ao átrio direito do coração.") #alt certa 
    print("C- a artéria pulmonar transporta sangue rico em oxigênio, do coração até os pulmões.")
    print("D- as veias pulmonares transportam sangue rico em oxigênio, dos pulmões até o átrio direito do coração.")
    print("E- a artéria aorta transporta sangue rico em oxigênio para o corpo, por meio da circulação sistêmica, e sai do ventrículo direito do coração.")
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
    print("Analise as três afirmações sobre o controle da respiração em humanos.") 
    print()
    print("I. Impulsos nervosos estimulam a contração do diafragma e dos músculos intercostais, provocando a inspiração.")
    print("II. A concentração de dióxido de carbono no sangue influencia o ritmo respiratório.")
    print("III. O ritmo respiratório pode ser controlado voluntariamente, mas na maior parte do tempo tem controle involuntário.")
    print()
    print("Está correto o que se afirma em")
    print()
    time.sleep(1)
    print("A- I, II e III.") #alt certa 
    print("B- I, apenas.") 
    print("C- I e III, apenas.")
    print("D- III, apenas.")
    print("E- II e III, apenas.")
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

def pergunta16(): 
    global casa
    global pontos
    print("Muitas plantas adaptadas a ambientes terrestres secos e com alta intensidade luminosa apresentam folhas")
    print()
    time.sleep(1)
    print("A- grandes com estômatos concentrados na parte inferior, poucos tricomas claros, cutícula impermeável e parênquima aerífero.")
    print("B- pequenas com estômatos concentrados na parte superior, ausência de tricomas, cera sobre a epiderme foliar e parênquima aquífero.") 
    print("C- pequenas com estômatos concentrados na parte inferior, muitos tricomas claros, cutícula impermeável e parênquima aquífero.") #alt certa 
    print("D- grandes com estômatos igualmente distribuídos em ambas as partes, ausência de tricomas, ausência de cera sobre a epiderme foliar e parênquima aerífero.")
    print("E- pequenas com estômatos concentrados na parte superior, muitos tricomas claros, cera sobre a epiderme foliar e parênquima aerífero.")
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

def pergunta17():
    global casa
    global pontos
    print("Células de embrião de drosófila (2n=8), que estavam em divisão, foram tratadas com uma substância que inibe a formação do fuso, impedindo que a divisão celular prossiga. Após esse tratamento, quantos cromossomos e quantas cromátides, respectivamente, cada célula terá?")
    print()
    time.sleep(1)
    print("A- 4 e 4")
    print("B- 4 e 8")  
    print("C- 8 E 8")
    print("D- 8 E 16") #alt certa
    print("E- 16 E 16")
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

def pergunta18(): 
    global casa
    global pontos
    print("A levedura Saccharomyces cerevisiae pode obter energia na ausência de oxigênio, de acordo com a equação")
    print("C6H12O6 → 2CO2 + 2CH3CH2OH + 2 ATP")
    print("Produtos desse processo são utilizados na indústria de alimentos e bebidas. Esse processo ocorre _____________ da levedura e seus produtos são utilizados na produção de _____________.")
    print("As lacunas dessa frase devem ser preenchidas por:") 
    print()
    time.sleep(1)
    print("A- nas mitocôndrias; cerveja e vinagre.")
    print("B- nas mitocôndrias; cerveja e pão.") 
    print("C- no citosol; iogurte e vinagre.")
    print("D- no citosol e nas mitocôndrias; cerveja e iogurte.")
    print("E- no citosol; cerveja e pão.") #alt certa
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

def pergunta19():
    global casa
    global pontos
    print("Na história evolutiva dos metazoários, o processo digestivo")
    print()
    time.sleep(1)
    print("A- passa de completamente intracelular a completamente extracelular, a partir dos nematelmintos.") #alt certa
    print("B- é intracelular, com hidrólise enzimática de moléculas de grande tamanho, a partir dos equinodermas.")  
    print("C- é extracelular, já nos poríferos, passando a compltamente intracelular, a partir dos artrópodes.")
    print("D- é completamente extracelular nos vertebrados, o que os distingue dos demais grupos de animais.")
    print("E- passa de completamente extracelular a completamente intracelular, a partir dos anelídeos.")
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

def pergunta20(): 
    global casa
    global pontos
    print("As briófitas, no reino vegetal, e os anfíbios, entre os vertebrados, são considerados os primeiros grupos a conquistar o ambiente terrestre. Comparando-os, é correto afirmar que,")
    print()
    time.sleep(1)
    print("A- nos anfíbios e nas briófitas, o sistema vascular é pouco desenvolvido; isso faz com que, nos anfíbios, a temperatura não seja controlada internamente.")
    print("B- nos anfíbios, o produto imediato da meiose são os gametas; nas briófitas, a meiose origina um indivíduo haploide que posteriormente produz os gametas.") #alt certa 
    print("C- nos anfíbios e nas briófitas, a fecundação ocorre em meio seco; o desenvolvimento dos embriões se dá na água.")
    print("D- nos anfíbios, a fecundação origina um indivíduo diploide e, nas briófitas, um indivíduo haploide; nos dois casos, o indivíduo formado passa por metamorfoses até tornar-se adulto.")
    print("E- nos anfíbios e nas briófitas, a absorção de água se dá pela epiderme; o transporte de água é feito por difusão, célula por célula, às demais partes do corpo.")
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

def pergunta21(): 
    global casa
    global pontos
    print("No morango, os frutos verdadeiros são as estruturas escuras e rígidas que se encontram sobre a parte vermelha e suculenta. Cada uma dessas estruturas resulta, diretamente,")
    print()
    time.sleep(1)
    print("A- da fecundação do óvulo pelo núcleo espermático do grão de pólen.")
    print("B- da fecundação de várias flores de uma mesma inflorescência.")  
    print("C- do desenvolvimento do ovário, que contém a semente com o embrião.") #alt certa
    print("D- da dupla fecundação, que é exclusiva das angiospermas.")
    print("E- do desenvolvimento do endosperma que nutrirá o embrião.")
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

def pergunta22(): 
    global casa
    global pontos
    print("Louis Pasteur realizou experimentos pioneiros em Microbiologia. Para tornar estéril um meio de cultura, o qual poderia estar contaminado com agentes causadores de doenças, Pasteur mergulhava o recipiente que o continha em um banho de água aquecida à ebulição e à qual adicionava cloreto de sódio.")
    print("Com a adição de cloreto de sódio, a temperatura de ebulição da água do banho, com relação à da água pura, era _________. O aquecimento do meio de cultura provocava _________.")
    print("As lacunas podem ser corretamente preenchidas, respectivamente, por:")
    print()
    time.sleep(1)
    print("A- menor; rompimento da membrana celular das bactérias presentes.")
    print("B- a mesma; desnaturação das proteínas das bactérias.") 
    print("C- maior; rompimento da membrana celular dos vírus.")
    print("D- maior; desnaturação das proteínas das bactérias presentes.") #alt certa 
    print("E- menor; alterações no DNA dos vírus e das bactérias.")
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

def pergunta23(): 
    global casa
    global pontos
    print("Uma das consequências do “efeito estufa” é o aquecimento dos oceanos. Esse aumento de temperatura provoca") 
    print()
    time.sleep(1)
    print("A- menor dissolução de O2 nas águas oceânicas, o que leva ao consumo de maior quantidade de CO2 pelo fitoplâncton, contribuindo, assim, para a redução do efeito estufa global.")
    print("B- menor dissolução de CO2 e O2 nas águas oceânicas, o que leva ao consumo de maior quantidade de O2 pelo fitoplâncton, contribuindo, assim, para a redução do efeito estufa global.") 
    print("C- maior dissolução de CO2 nas águas oceânicas, o que leva ao consumo de maior quantidade desse gás pelo fitoplâncton, contribuindo, assim, para a redução do efeito estufa global.")
    print("D- maior dissolução de O2 nas águas oceânicas, o que leva à liberação de maior quantidade de CO2 pelo fitoplâncton, contribuindo, assim, para o aumento do efeito estufa global.")
    print("E- menor dissolução de CO2 nas águas oceânicas, o que leva ao consumo de menor quantidade desse gás pelo fitoplâncton, contribuindo, assim, para o aumento do efeito estufa global.") #alt certa
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

def pergunta24(): 
    global casa
    global pontos
    print("O rótulo de uma lata de desodorante em aerosol apresenta, entre outras, as seguintes informações: “Propelente: gás butano. Mantenha longe do fogo”. A principal razão dessa advertência é:") 
    print()
    time.sleep(1)
    print("A- O aumento da temperatura faz aumentar a pressão do gás no interior da lata, o que pode causar uma explosão.") #alt certa
    print("B- A lata é feita de alumínio, que, pelo aquecimento, pode reagir com o oxigênio do ar.") 
    print("C- O aquecimento provoca o aumento do volume da lata, com a consequente condensação do gás em seu interior.")
    print("D- O aumento da temperatura provoca a polimerização do gás butano, inutilizando o produto.")
    print("E- A lata pode se derreter e reagir com as substâncias contidas em seu interior, inutilizando o produto.")
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



def pergunta25(): 
    global casa
    global pontos
    print("O craqueamento catalítico é um processo utilizado na indústria petroquímica para converter algumas frações do petróleo que são mais pesadas (isto é, constituídas por compostos de massa molar elevada) em frações mais leves, como a gasolina e o GLP, por exemplo. Nesse processo, algumas ligações químicas nas moléculas de grande massa molecular são rompidas, sendo geradas moléculas menores.\nA respeito desse processo, foram feitas as seguintes afirmações:\nI. O craqueamento é importante economicamente, pois converte frações mais pesadas de petróleo em compostos de grande demanda.\nII. O craqueamento libera grande quantidade de energia, proveniente da ruptura de ligações químicas nas moléculas de grande massa molecular.\nIII. A presença de catalisador permite que as transformações químicas envolvidas no craqueamento ocorram mais rapidamente.\nEstá correto o que se afirma em")  
    print()
    time.sleep(1)
    print("A- I, apenas.")
    print("B- II, apenas.")  
    print("C- I e III, apenas.")#alt certa
    print("D- II e III, apenas.")
    print("E- I, II e III")
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
    print("Na obra O poço do Visconde, de Monteiro Lobato, há o seguinte diálogo entre o Visconde de Sabugosa e a boneca Emília:\n— Senhora Emília, explique-me o que é hidrocarboneto. A atrapalhadeira não se atrapalhou e respondeu:\n— São misturinhas de uma coisa chamada hidrogênio com outra coisa chamada carbono. Os carocinhos de um se ligam aos carocinhos de outro.\nNesse trecho, a personagem Emília usa o vocabulário informal que a caracteriza. Buscando-se uma terminologia mais adequada ao vocabulário utilizado em Química, devem-se substituir as expressões “misturinhas”, “coisa” e “carocinhos”, respectivamente, por:") 
    print()
    time.sleep(1)
    print("A- compostos, elemento, átomos.")#alt certa 
    print("B- misturas, substância, moléculas.") 
    print("C- substâncias compostas, molécula, íons.")
    print("D- misturas, substância, átomos.")
    print("E- misturas, substância, átomos.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "A": #COLOCAR ALT CERTA
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é A.") 
    return "\n"

def pergunta27(): 
    global casa
    global pontos
    print("Quando começaram a ser produzidos em larga escala, em meados do século XX, objetos de plástico eram considerados substitutos de qualidade inferior para objetos feitos de outros materiais. Com o tempo, essa concepção mudou bastante. Por exemplo, canecas eram feitas de folha de flandres, uma liga metálica, mas, hoje, também são feitas de louça ou de plástico. Esses materiais podem apresentar vantagens e desvantagens para sua utilização em canecas, como as listadas a seguir:\nI. ter boa resistência a impactos, mas não poder ser levado diretamente ao fogo;\nII. poder ser levado diretamente ao fogo, mas estar sujeito a corrosão;\nIII. apresentar pouca reatividade química, mas ter pouca resistência a impactos.\nOs materiais utilizados na confecção de canecas os quais apresentam as propriedades I, II e III são, respectivamente,")  
    print()
    time.sleep(1)
    print("A- metal, plástico, louça.")
    print("B- metal, louça, plástico.")  
    print("C- louça, metal, plástico.")
    print("D- plástico, louça, metal.")
    print("E- plástico, metal, louça.")#alt certa
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

def pergunta28(): 
    global casa
    global pontos
    print("'São animadores os números da safra de grãos do Brasil, que deverá colher neste ano o recorde histórico de 120 milhões de toneladas. Com isto, o Brasil deverá tornar-se o maior exportador mundial de soja, suplantando os Estados Unidos'. (Folha de S. Paulo, 2003)\nO acréscimo de produção de soja citado acarretará\nI. aumento do 'buraco na camada de ozônio', pois nas plantações de soja são utilizados clorofluorocarbonetos como fertilizantes.\nII. maior consumo de água, necessária à irrigação, que, em parte, será absorvida pelo vegetal.\nIII. aumento de quantidade de CO2 atmosférico, diretamente produzido pela fotossíntese.\nIV. aumento da área de solos ácidos, gerados pela calagem, em que se utiliza calcário com altos teores de óxido de cálcio e óxido de magnésio.\nDessas afirmações,")  
    print()
    time.sleep(1)
    print("A- somente I é correta.")
    print("B- somente II é correta.") #alt certa 
    print("C- somente II e III são corretas.")
    print("D- somente III e IV são corretas.")
    print("E- todas são corretas.")
    print()
    print("Insira a letra referente à sua resposta:")
    alt = input()
    print()
    time.sleep(1)
    while alt.upper() != "A" and alt.upper() != "B" and alt.upper() != "C" and alt.upper() != "D" and alt.upper() != "E":
        print("Letra inválida. Insira a letra referente à sua resposta:")
        alt = input()
    if alt.upper() == "B": #COLOCAR ALT CERTA
        print("Você acertou!")
        casa = casa +3
        pontos = pontos + 1
    else:
        print("Resposta incorreta! A Resposta correta é B.") 
    return "\n"

def pergunta29(): 
    global casa
    global pontos
    print("Um hidrocarboneto gasoso [que pode ser eteno, etino, propano, etano ou metano] está contido em um recipiente de 1L, a 25°C e 1 atm. A combustão total desse hidrocarboneto requer exatamente 5L de O2, medidos nas mesmas condições de temperatura e pressão. Portanto, esse hidrocarboneto deve ser:")  
    print()
    time.sleep(1)
    print("A- eteno")
    print("B- etino")  
    print("C- propano") #alt certa
    print("D- etano")
    print("E- metano")
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

def pergunta30(): 
    global casa
    global pontos
    print("No preparo de certas massas culinárias, como pães, é comum adicionar-se um fermento que, dependendo da receita, pode ser o químico, composto principalmente por hidrogenocarbo- nato de sódio (NaHCO3), ou o fermento biológico, formado por leveduras. Os fermentos adicionados, sob certas condições, são responsáveis pela produção de dióxido de carbono, o que auxilia a massa a crescer.\nPara explicar a produção de dióxido de carbono, as seguintes afirmações foram feitas.\nI. Tanto o fermento químico quanto o biológico reagem com os carboidratos presentes na massa culinária, sendo o dióxido de carbono um dos produtos dessa reação.\nII. O hidrogenocarbonato de sódio, presente no fermento químico, pode se decompor com o aquecimento, ocorrendo a formação de carbonato de sódio (Na2CO3), água e dióxido de carbono.\nIII. As leveduras, que formam o fermento biológico, metabolizam os carboidratos presentes na massa culinária, produzindo, entre outras substâncias, o dióxido de carbono.\nIV. Para que ambos os fermentos produzam dióxido de carbono, é necessário que a massa culinária seja aquecida a temperaturas altas (cerca de 200 oC), alcançadas nos fornos domésticos e industriais.\nDessas afirmações, as que explicam corretamente a produção de dióxido de carbono pela adição de fermento à massa culinária são, apenas,")  
    print()
    time.sleep(1)
    print("A- I e II.")
    print("B- II e III.") #alt certa 
    print("C- III e IV. ")
    print("D- I, II e IV.")
    print("E- I, III e IV.")
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

def pergunta31(): 
    global casa
    global pontos
    print("Nas mesmas condições de pressão e temperatura, 50L de gás propano (C3H8) e 250L de ar foram colocados em um reator, ao qual foi fornecida energia apenas suficiente para iniciar a reação de combustão. Após algum tempo, não mais se observou a liberação de calor, o que indicou que a reação havia-se encerrado. Com base nessas observações experimentais, três afirmações foram feitas:\nI. Se tivesse ocorrido apenas combustão incompleta, restaria propano no reator.\nII. Para que todo o propano reagisse, considerando a combustão completa, seriam necessários, no mínimo, 750 L de ar.\nIII. É provável que, nessa combustão, tenha se formado fuligem.\nEstá correto apenas o que se afirma em\nNote e adote: Composição aproximada do ar em volume: 80% de N2 e 20% de O2.")  
    print()
    time.sleep(1)
    print("A- I.")
    print("B- III.") 
    print("C- I e II.")
    print("D- I e III.") #alt certa 
    print("E- II e III.")
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

def pergunta32(): 
    global casa
    global pontos
    print("Plantas não conseguem aproveitar direta- mente o nitrogênio do ar atmosférico para sintetizar _______. Esse componente do ar precisa ser transformado em compostos. Isso ocorre, na atmosfera, durante as tempestades com relâmpagos, quando se forma _______. Na raiz das leguminosas, bactérias transformam o nitrogênio em _______. que são fertilizantes naturais. Tais fertilizantes podem ser obtidos industrialmente, a partir do nitrogênio, em um processo cuja primeira etapa é a síntese de _______. As lacunas do texto acima são adequadamente preenchidas, na seqüência em que aparecem, respectivamente, por")  
    print()
    time.sleep(1)
    print("A- proteínas – amônia – sais de amônio – ozônio")
    print("B- açúcares – óxido nítrico – carbonatos – amônia") 
    print("C- proteínas – ozônio – fosfatos – sais de amônio")
    print("D- açúcares – amônia – carbonatos – óxido nítrico")
    print("E- proteínas – óxido nítrico – nitratos – amônia") #alt certa 
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






#FUNÇÃO QUE CHAMA PERGUNTAS FUVEST

def perguntas():
    per = random.randrange(1, 33)

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
    elif per == 30:
        pergunta30()
    elif per == 31:
        pergunta31()  
    elif per == 32:
        pergunta32()                  

    return "\n"


#FUNÇÃO QUE CHAMA CASA
def casinha():
  return casa

#FUNÇÃO QUE CHAMA PONTOS
def pontinho():
  return pontos
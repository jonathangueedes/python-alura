import random
def jogar():

    print("************************************")
    print("* Bem vindo ao jogo da adivinhação *")
    print("************************************")

    numero_secreto = random.randrange(1,101)
    # numero_de_tentativas = 0
    pontos = 1000
    rodada = 0

    print("Qual o nive de dificuldade?")
    print("(1) Fácil  (2) Médio  (3) Difícil")
    
    nivel = int(input("Define o nivel: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    while(rodada <= total_de_tentativas):
        chute_str = input("Digite o seu numero: ")
        chute = int(chute_str)
        if(chute < 1 or chute > 100):
            print("Digite um número valido")
            continue
        if (chute != numero_secreto):
            pontos = pontos - chute
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))

        certo = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (certo):
            print("Você acertou e obteve: " + str(pontos) + "pontos !!!")
            break
        else:
            if(maior):
                print("Você errou, chutou um valor maior que o número secreto")
            elif(menor):
                print("Você errou, chutou um valor menor que o número secreto")

        rodada = rodada + 1

    print("Fim do jogo")
    pontos_rodada = abs(chute - numero_secreto)
    pontos = pontos - pontos_rodada

    rodada = rodada + 1

if(__name__ == "__main__"):
    jogar()


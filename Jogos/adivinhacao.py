import random

print("************************************")
print("* Bem vindo ao jogo da adivinhação *")
print("************************************")

numero_secreto = random.randrange(1,101)
numero_de_tentativas = 0
rodada = 1
pontos = 1000

print("Digite o nivel de difiuldade:")
print("1 - Facil | 2 - medio | 3 dificil")
dificuldade = int(input())

if(dificuldade == 1):
    numero_de_tentativas = 20
elif(dificuldade == 2):
    numero_de_tentativas = 10
else:
    numero_de_tentativas = 5

while(rodada <= numero_de_tentativas):
    chute_str = input("Digite o seu numero: ")
    chute = int(chute_str)
    if(chute < 1 or chute > 100):
        print("Digite um número valido")
        continue
    print("Tentativa {} de {}".format(rodada,numero_de_tentativas))

    certo = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (certo):
        print("Você acertou e fez {} pontos".format(pontos))
        
        break
    else:
        if(maior):
            print("Você errou, chutou um valor maior que o número secreto")
        elif(menor):
            print("Você errou, chutou um valor menor que o número secreto")

    pontos_rodada = abs(chute - numero_secreto)
    pontos = pontos - pontos_rodada

    rodada = rodada + 1

print("Fim do jogo")


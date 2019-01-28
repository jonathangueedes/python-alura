print("************************************")
print("* Bem vindo ao jogo da adivinhação *")
print("************************************")

numero_secreto = 42
numero_de_tentativas = 3
rodada = 1

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
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou, chutou um valor maior que o número secreto")
        elif(menor):
            print("Você errou, chutou um valor menor que o número secreto")

    rodada = rodada + 1

print("Fim do jogo")


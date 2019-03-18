import random
def jogar_forca():

    print("********************************")
    print("** Bem vindo ao jogo da Forca **")
    print("********************************")

    print("A sua palavra está logo abaixo, Boa sorte!!!")
    print()

    arquivo = open("/home/jonathan/python-alura/Jogos/palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    
    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append("_")
    print(letras_acertadas)

    print()

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual a letra? ")
        chute = chute.strip().upper()
        

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index = index + 1
        
        else:
            erros = erros + 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)



    if(acertou):
        print("Voce acertou")
    else:
        print("voce errou")

    print()    
    print("______________")
    print("Fim de Jogo")


        








if(__name__ == "__main__"):
    jogar_forca()


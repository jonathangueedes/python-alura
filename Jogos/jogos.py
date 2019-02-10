import forca
import adivinhacao

print("******************************")
print("***** Escolha o seu jogo *****")
print("******************************")

print("( 1 ) Adivinhação  |   ( 2 ) Forca ")

jogo = int(input())

if (jogo == 1):
    print("Jogando adivinhação")
    adivinhacao.jogar()
elif (jogo == 2):
    print("Jogando forca")
    forca.jogar_forca()





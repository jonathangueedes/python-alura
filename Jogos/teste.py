testefor = 1
for testefor in range(1, 10):
    chute = input("Digite um valor do chute entre 1 e 100: ")
    testefor = int(chute)
    print(testefor)
    
    if(testefor <= 0 or testefor > 100):
        print("O valor informado é invalido")
        continue
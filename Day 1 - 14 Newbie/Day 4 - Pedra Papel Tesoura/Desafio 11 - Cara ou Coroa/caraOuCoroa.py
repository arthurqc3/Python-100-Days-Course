import random

def verificar(resposta):
    numero = random.randint(0,1)
    if numero == 1:
        print("Deu Cara")
    else:
        print("Deu Coroa")
    if resposta == numero:
        print(f"Voce Ganhou")
    else:
        print(f"Voce Perdeu!")

escolha = input("Escolha Cara ou Coroa:\n").title()

if escolha == "Cara":
    escolha = 1
    verificar(escolha)
elif escolha == "Coroa":
    escolha = 0
    verificar(escolha)

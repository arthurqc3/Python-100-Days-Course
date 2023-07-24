from art import *
import random

def computer(escolha):
    if escolha == 0:
        rock()
    elif escolha == 1:
        paper()
    elif escolha == 2:
        scissors()

choice = int(input("O que voce escolhe? Digite 0 para Pedra, 1 para Papel e 2 para Tesoura: "))
computerChoice = random.randint(0,2)

if choice == 0 and computerChoice == 2:
    rock()
    print(f"Escolha do seu oponente: \n")
    computer(computerChoice)
    print("Voce Ganhou!")
elif choice == 1 and computerChoice == 0:
    paper()
    print(f"Escolha do seu oponente: \n")
    computer(computerChoice)
    print("Voce Ganhou!")
elif choice == 2 and computerChoice == 1:
    scissors()
    print(f"Escolha do seu oponente: \n")
    computer(computerChoice)
    print("Voce Ganhou!")
else:
    computer(choice)                       # Usando a mesma def para verificar a decisão do usuário tambem
    print(f"Escolha do seu oponente: \n")
    computer(computerChoice)
    print("Você Perdeu")
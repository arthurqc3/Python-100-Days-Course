#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
contador = 0
for caracter in letters:                                 # adiciona as letras a lista "password"
    aleatorio = random.randint(0, len(letters) - 1)      # baseado em um int aleatorio e no seu numero de elementos
    if contador < nr_letters:                            # casuamente dava erro "list index out of range"
        password.append(letters[aleatorio])              # resolvido ao colocar - 1 no range do randint
        contador += 1
        
contador = 0

for caracter in numbers:                                 # adiciona os numeros a lista "password"
    aleatorio = random.randint(0, len(numbers) - 1)
    if contador < nr_numbers:
        password.append(numbers[aleatorio])
        contador += 1
        
contador = 0

for caracter in symbols:                                 # adiciona os simbolos a listas "password"
    aleatorio = random.randint(0, len(symbols) - 1)
    if contador < nr_symbols:
        password.append(symbols[aleatorio])
        contador += 1        

random.shuffle(password)                                 # colocar todos os itens da lista de forma aleatória
password = ''.join(password)                             # retirar as aspas entre os itens 
print(password)
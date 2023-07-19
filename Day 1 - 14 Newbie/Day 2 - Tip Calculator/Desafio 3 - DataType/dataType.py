# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

num = list(input("numero: "))
numLista = []
 
for numero in num:
    numLista.append(int(numero))

soma = sum(numLista)

print(soma)
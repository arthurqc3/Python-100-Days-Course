# Programa que faz uma lista de nomes para escolher uma pessoa para pagar a conta

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

payment = random.randint(0, len(names))

print(f"{names[payment]} is going to buy the meal today!")
# Programa baseado em um antigo jogo onde usando as palavras TRUE LOVE se calcula a porcentagem
# de amor entre duas pessoas

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1 = list(name1.upper())
name2 = list(name2.upper())

countL1 = name1.count('T')
countL1 += name1.count('R')
countL1 += name1.count('U')
countL1 += name1.count('E')
countL2 = name1.count('L')
countL2 += name1.count('O')
countL2 += name1.count('V')
countL2 += name1.count('E')

countL1 += name2.count('T')
countL1 += name2.count('R')
countL1 += name2.count('U')
countL1 += name2.count('E')
countL2 += name2.count('L')
countL2 += name2.count('O')
countL2 += name2.count('V')
countL2 += name2.count('E')

loveScore = int(str(countL1) + str(countL2))

if loveScore <= 10 or loveScore >= 90:
  print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
  print(f"Your score is {loveScore}, you are alright together.")
else:
  print(f"Your score is {loveScore}.")
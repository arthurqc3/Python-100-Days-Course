# Programa que diz quantos dias, semanas e meses faltam para você completar 90 anos

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = 90 - int(age)
days = 365 * age
weeks = 52 * age
months = 12 * age

print("You have", days, "days,", weeks,"weeks, and", months,"months left.")
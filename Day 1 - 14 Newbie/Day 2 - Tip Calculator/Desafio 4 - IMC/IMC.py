# Programa que mosta o calculo de IMC

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height = float(height)
weight = int(weight)

imc = weight/(height*height)

print(round(imc))

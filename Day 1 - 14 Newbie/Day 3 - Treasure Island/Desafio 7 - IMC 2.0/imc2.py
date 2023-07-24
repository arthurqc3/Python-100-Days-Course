# IMC 2.0 agora mostra tambem seu indice 

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

imc = weight/(height*height)

if imc < 18.5:
    print(f"Your BMI is {round(imc)}, you are underweight.")
if imc > 18.5 and imc < 25:
    print(f"Your BMI is {round(imc)}, you have a normal weight.")
if imc > 25 and imc < 30:
    print(f"Your BMI is {round(imc)}, you are slightly overweight.")
if imc > 30 and imc < 35: 
    print(f"Your BMI is {round(imc)}, you are obese.")
if imc > 35:
    print(f"Your BMI is {round(imc)}, you are clinically obese.")
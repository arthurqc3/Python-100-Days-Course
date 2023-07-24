# Programa que mostra a maior pontuação da classe usando listas e For loop

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
score = 0
for num in student_scores:
    if score < num:
        score = num

print(f"The highest score in the class is: {score}")
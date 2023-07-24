# Programa que mostra a altura media usando listas e For loop

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇

height = 0
temp = 0
for num in student_heights:
    temp += 1
    height += num

print(round(height/temp))

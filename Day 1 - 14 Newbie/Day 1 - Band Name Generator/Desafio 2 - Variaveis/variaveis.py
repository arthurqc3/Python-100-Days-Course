# Write a program that switches the values stored in the variables a and b.

a = input("a: ")
b = input("b: ")

print("a: " + a + " b: " + b)

temp = a
a = b
b = temp 

print("a: " + a + " b: " + b)
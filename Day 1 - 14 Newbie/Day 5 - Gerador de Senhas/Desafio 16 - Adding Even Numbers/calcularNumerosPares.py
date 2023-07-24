# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100

#Write your code below this row 👇
even = 0
for num in range (0,101):
    if num % 2 == 0:
        even += num

print(even)

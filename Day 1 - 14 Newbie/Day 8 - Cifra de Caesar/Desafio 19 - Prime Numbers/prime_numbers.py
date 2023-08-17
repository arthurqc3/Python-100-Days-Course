def prime_checker(number):
    temp = 0
    for num in range(1, number):
        if number % num == 0:
            temp += 1

    if temp == 2:
        print("Prime")
    else:
        print("Not Prime")

n = int(input("Check this number: "))
prime_checker(number=n)

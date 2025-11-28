from math import sqrt

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(sqrt(num)) + 1):
        if (num % i) == 0:
            print(num, "is not prime number")
            break
        else:
            print("The number is  a prime number")
else:
    print(num, "is not a prime number")

number = int(input("Enter a number: "))
digits = len(str(number))
result = 0
temp = number
while temp > 0:
    digit = temp % 10
    result += digit ** digits
    temp //= 10
if result == number:
    print("The number is an Armstrong number")
else:
    print(number, "is not an Armstrong number")



def print_factors(number):
    print("The factors of the number are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
number = int(input("Enter a number to find its factors: "))
print_factors(number)

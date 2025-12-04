try:
    number = int(input("Enter a number: "))

    n = abs(number)
    if 10 <= n <= 99:
        def is_prime(x: int) -> bool:
            if x <= 1:
                return False
            if x <= 3:
                return True
            if x % 2 == 0:
                return False
            import math
            limit = int(math.isqrt(x))
            for i in range(3, limit + 1, 2):
                if x % i == 0:
                    return False
            return True

        if is_prime(n):
            print("Yes it is prime number")
        else:
            print("Not a prime number")
    else:
        print(f"{number} is not a two-digit number.")
except ValueError:
    print("Invalid input. Please enter an integer.")
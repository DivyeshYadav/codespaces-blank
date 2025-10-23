def func1(n):
    return n * (n + 1)//2
print(func1(10))

def func2(n):
    sum = 0
    for x in range(1,n+1):
        sum = sum+x
    return sum
print(func2(10))

def func3(n):
    sum  = 0
    for j in range(1,n+1):
        for i in range(1,j+1):
            sum = sum + 1
    return sum
print(func3(10))
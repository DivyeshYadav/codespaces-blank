input1 = int(input("Enter first number: "))
input2 = int(input("Enter second number: "))

def func1(input1, input2):
    return input1 * input2

print(func1(input1, input2))

def func_multiply_final(A, B):
    product = 0
    for _ in range(B): 
        product = product + A  
    return product

result = func_multiply_final(input1, input2)
print(f"{result}")

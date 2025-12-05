num1 = 10
num2 = 4

#AND Operator
print("num1 & num2 =", num1 & num2)
#OR Operator
print("num1 | num2 =", num1 | num2)
#XOR Operator
print("num1 ^ num2 =", num1 ^ num2)
#NOT Operator
print("~num1 =", ~num1)
#Left Shift Operator
print("num1 << 2 =", num1 << 2)
#Right Shift Operator
print("num1 >> 2 =", num1 >> 2)


#Find Number of bits
def countSetBits(n):
    count = 0
    while (n):
        count += 1
        n >>= 1
    return count

num1 = int(input("Enter a number to find set bits: "))
print("Number of set bits in num1 =", countSetBits(num1))
